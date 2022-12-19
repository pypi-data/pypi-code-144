# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

"""
Simple perf tests for aiosqlite and the asyncio run loop.
"""
import string
import sys
import tempfile
import time

if sys.version_info < (3, 8):
    from aiounittest import AsyncTestCase as TestCase
else:
    from unittest import IsolatedAsyncioTestCase as TestCase

import aiosqlite
from .smoke import setup_logger

TEST_DB = ":memory:"
TARGET = 2.0
RESULTS = {}


def timed(fn, name=None):
    """
    Decorator for perf testing a block of async code.

    Expects the wrapped function to return an async generator.
    The generator should do setup, then yield when ready to start perf testing.
    The decorator will then pump the generator repeatedly until the target
    time has been reached, then close the generator and print perf results.
    """

    name = name or fn.__name__

    async def wrapper(*args, **kwargs):
        gen = fn(*args, **kwargs)

        await gen.asend(None)
        count = 0
        before = time.time()

        while True:
            count += 1
            value = time.time() - before < TARGET
            try:
                if value:
                    await gen.asend(value)
                else:
                    await gen.aclose()
                    break

            except StopAsyncIteration:
                break

            except Exception as e:
                print(f"exception occurred: {e}")
                return

        duration = time.time() - before

        RESULTS[name] = (count, duration)

    return wrapper


class PerfTest(TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"Running perf tests for at least {TARGET:.1f}s each...")
        setup_logger()

    @classmethod
    def tearDownClass(cls):
        print(f"\n{'Perf Test':<25} Iterations  Duration  {'Rate':>11}")
        for name in sorted(RESULTS):
            count, duration = RESULTS[name]
            rate = count / duration
            name = name.replace("test_", "")
            print(f"{name:<25} {count:>10}  {duration:>7.1f}s  {rate:>9.1f}/s")

    @timed
    async def test_connection_memory(self):
        while True:
            yield
            async with aiosqlite.connect(TEST_DB):
                pass

    @timed
    async def test_connection_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            path = tf.name
            tf.close()

            async with aiosqlite.connect(path) as db:
                await db.execute(
                    "create table perf (i integer primary key asc, k integer)"
                )
                await db.execute("insert into perf (k) values (2), (3)")
                await db.commit()

            while True:
                yield
                async with aiosqlite.connect(path):
                    pass

    @timed
    async def test_atomics(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table perf (i integer primary key asc, k integer)")
            await db.execute("insert into perf (k) values (2), (3)")
            await db.commit()

            while True:
                yield
                async with db.execute("select last_insert_rowid()") as cursor:
                    await cursor.fetchone()

    @timed
    async def test_inserts(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table perf (i integer primary key asc, k integer)")
            await db.commit()

            while True:
                yield
                await db.execute("insert into perf (k) values (1), (2), (3)")
                await db.commit()

    @timed
    async def test_insert_ids(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table perf (i integer primary key asc, k integer)")
            await db.commit()

            while True:
                yield
                cursor = await db.execute("insert into perf (k) values (1)")
                await cursor.execute("select last_insert_rowid()")
                await cursor.fetchone()
                await db.commit()

    @timed
    async def test_insert_macro_ids(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table perf (i integer primary key asc, k integer)")
            await db.commit()

            while True:
                yield
                await db.execute_insert("insert into perf (k) values (1)")
                await db.commit()

    @timed
    async def test_select(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table perf (i integer primary key asc, k integer)")
            for i in range(100):
                await db.execute("insert into perf (k) values (%d)" % (i,))
            await db.commit()

            while True:
                yield
                cursor = await db.execute("select i, k from perf")
                assert len(await cursor.fetchall()) == 100

    @timed
    async def test_select_macro(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute("create table perf (i integer primary key asc, k integer)")
            for i in range(100):
                await db.execute("insert into perf (k) values (%d)" % (i,))
            await db.commit()

            while True:
                yield
                assert len(await db.execute_fetchall("select i, k from perf")) == 100

    async def test_iterable_cursor_perf(self):
        async with aiosqlite.connect(TEST_DB) as db:
            await db.execute(
                "create table ic_perf ("
                "i integer primary key asc, k integer, a integer, b integer, c char(16))"
            )
            for batch in range(128):  # add 128k rows
                r_start = batch * 1024
                await db.executemany(
                    "insert into ic_perf (k, a, b, c) values(?, 1, 2, ?)",
                    [
                        *[
                            (i, string.ascii_lowercase)
                            for i in range(r_start, r_start + 1024)
                        ]
                    ],
                )
                await db.commit()

            async def test_perf(chunk_size: int):
                while True:
                    async with db.execute("SELECT * FROM ic_perf") as cursor:
                        cursor.iter_chunk_size = chunk_size
                        async for _ in cursor:
                            yield

            for chunk_size in [2**i for i in range(4, 11)]:
                await timed(test_perf, f"iterable_cursor @ {chunk_size}")(chunk_size)
