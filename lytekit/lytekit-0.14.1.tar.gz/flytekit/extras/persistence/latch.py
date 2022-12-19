import base64
import hashlib
import math
import mimetypes
import os as _os
import time
import traceback
from queue import Empty, Queue
from threading import Thread
from typing import List, Optional
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter, Retry

from flytekit.configuration import DataConfig, LatchConfig
from flytekit.core.data_persistence import DataPersistence, DataPersistencePlugins
from flytekit.exceptions.user import FlyteUserException

"""
Thread Utils For Downloading Directories
"""


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""

    def __init__(self, num_threads):
        self.tasks: Queue = Queue(-1)
        self.threads: List[Worker] = []
        self.cache_accum = bytearray([0] * 32)
        for _ in range(num_threads):
            self.threads.append(Worker(self.tasks))

    def start(self):
        for t in self.threads:
            t.start()

    def join(self):
        for t in self.threads:
            t.join()

            for i in range(len(self.cache_accum)):
                self.cache_accum[i] ^= t.cache_accum[i]

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """Add a list of tasks to the queue"""
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        try:
            self.tasks.join()
        finally:
            self.join()


class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks: Queue):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.cache_accum = bytearray([0] * 32)

    def run(self):
        while True:
            try:
                func, args, kargs = self.tasks.get_nowait()
            except Empty:
                break

            try:
                attempts = 0
                while True:
                    try:
                        res = func(*args, **kargs)

                        if res is not None and res["cache"] is not None:
                            hash = hashlib.sha256(res["cache"].encode("utf-8")).digest()
                            for i in range(len(self.cache_accum)):
                                self.cache_accum[i] ^= hash[i]

                        break
                    except Exception as e:
                        attempts += 1
                        if attempts >= 5:
                            raise e
                        time.sleep(0.1 * 2**attempts)
            except Exception:
                traceback.print_exc()
            finally:
                self.tasks.task_done()


def urlretrieve(url, path):
    with open(path, "wb") as f:
        r = _session.get(url, stream=True)

        for chunk in r.iter_content(1024):
            f.write(chunk)


def get(args):
    urlretrieve(args[0], args[1])


def _enforce_trailing_slash(path: str):
    if path[-1] != "/":
        path += "/"
    return path


_session = requests.Session()

_adapter = HTTPAdapter(max_retries=Retry(status_forcelist=[429, 500, 502, 503, 504], backoff_factor=1))
_session.mount("https://", _adapter)
_session.mount("http://", _adapter)


class LatchPersistence(DataPersistence):
    PROTOCOL = "latch://"

    def __init__(self, default_prefix: Optional[str] = None, data_config: Optional[DataConfig] = None):
        super().__init__(name="latch", default_prefix=default_prefix)
        default_latch_config = data_config.latch if data_config else LatchConfig.auto()

        self._latch_endpoint = _os.environ.get("LATCH_AUTHENTICATION_ENDPOINT")
        if self._latch_endpoint is None:
            self._latch_endpoint = default_latch_config.endpoint
        if self._latch_endpoint is None:
            raise ValueError("LATCH_AUTHENTICATION_ENDPOINT must be set")

        self._chunk_size = default_latch_config.upload_chunk_size_bytes
        if self._chunk_size is None:
            raise ValueError("S3_UPLOAD_CHUNK_SIZE_BYTES must be set")

    @staticmethod
    def _split_s3_path_to_key(path: str) -> str:
        """
        :param str path:
        :rtype: str
        """
        url = urlparse(path)
        return url.path

    def exists(self, remote_path: str) -> bool:
        """
        :param str remote_path: remote latch:// path
        :rtype bool: whether the s3 file exists or not
        """
        if not remote_path.startswith(self.PROTOCOL):
            raise ValueError(f"expected a Latch URL (latch://...): {remote_path}")

        r = _session.post(
            self._latch_endpoint + "/api/object-exists-at-url",
            json={"object_url": remote_path, "execution_name": _os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")},
            timeout=90,
        )
        if r.status_code != 200:
            raise FlyteUserException("failed to check if object exists at url `{}`".format(remote_path))

        return r.json()["exists"]

    def download_directory(self, remote_path: str, local_path: str) -> bool:
        """
        :param str remote_path: remote latch:// path
        :param str local_path: directory to copy to
        """
        internal_execution_id = _os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")

        if internal_execution_id is not None:
            r = _session.post(
                self._latch_endpoint + "/api/get-presigned-urls-for-dir",
                json={"object_url": remote_path, "execution_name": internal_execution_id},
                timeout=90,
            )
            if r.status_code != 200:
                raise FlyteUserException("failed to download `{}`".format(remote_path))

            dir_key = self._split_s3_path_to_key(remote_path)[1:]
            dir_key = _enforce_trailing_slash(dir_key)
            key_to_url_map = r.json()["key_to_url_map"]

            task_tuples = []
            for key, url in key_to_url_map.items():
                local_file_path = _os.path.join(local_path, key.replace(dir_key, "", 1))
                dir = "/".join(local_file_path.split("/")[:-1])
                _os.makedirs(dir, exist_ok=True)
                task_tuples.append((url, local_file_path))

            pool = ThreadPool(100)
            pool.map(get, task_tuples)
            pool.start()
            pool.wait_completion()
            return True
        else:
            try:
                from latch_cli.services.cp import cp

                cp(remote_path, local_path)
            except Exception as e:
                raise FlyteUserException("failed to get presigned urls for `{}`".format(remote_path)) from e

    def download(self, remote_path: str, local_path: str) -> bool:
        """
        :param str remote_path: remote latch:// path
        :param str local_path: directory to copy to
        """
        internal_execution_id = _os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")

        if internal_execution_id is not None:
            r = _session.post(
                self._latch_endpoint + "/api/get-presigned-url",
                json={"object_url": remote_path, "execution_name": internal_execution_id},
                timeout=90,
            )
            if r.status_code != 200:
                raise FlyteUserException("failed to get presigned url for `{}`".format(remote_path))

            url = r.json()["url"]
            get((url, local_path))
            return _os.path.exists(local_path)
        else:
            try:
                from latch_cli.services.cp import cp

                cp(remote_path, local_path)
            except Exception as e:
                raise FlyteUserException("failed to get presigned url for `{}`".format(remote_path)) from e

    @staticmethod
    def __upload(args):
        return LatchPersistence._upload(args[0], args[1], args[2], args[3])

    @staticmethod
    def _upload(file_path: str, to_path: str, chunk_size: int, endpoint: str):
        file_size = _os.path.getsize(file_path)
        nrof_parts = math.ceil(float(file_size) / chunk_size)
        content_type = mimetypes.guess_type(file_path)[0]
        if content_type is None:
            content_type = "application/octet-stream"

        internal_execution_id = _os.environ.get("FLYTE_INTERNAL_EXECUTION_ID")

        if internal_execution_id is not None:
            r = _session.post(
                endpoint + "/api/begin-upload",
                json={
                    "object_url": to_path,
                    "nrof_parts": nrof_parts,
                    "content_type": content_type,
                    "execution_name": internal_execution_id,
                },
                timeout=90,
            )
            if r.status_code != 200:
                raise FlyteUserException("failed to get presigned upload urls for `{}`".format(to_path))

            data = r.json()
            presigned_urls = data["urls"]
            upload_id = data["upload_id"]
            f = open(file_path, "rb")
            parts = []
            for key, val in presigned_urls.items():
                blob = f.read(chunk_size)
                r = _session.put(val, data=blob, timeout=90)
                if r.status_code != 200:
                    print(r.status_code)
                    print(r.text)
                    print(r.headers)
                    raise RuntimeError("failed to upload part `{}` of file `{}`".format(key, file_path))
                etag = r.headers["ETag"]
                parts.append({"ETag": etag, "PartNumber": int(key) + 1})

            r = _session.post(
                endpoint + "/api/complete-upload",
                json={
                    "upload_id": upload_id,
                    "parts": parts,
                    "object_url": to_path,
                    "execution_name": _os.environ.get("FLYTE_INTERNAL_EXECUTION_ID"),
                },
                timeout=90,
            )
            if r.status_code != 200:
                raise RuntimeError("failed to complete upload for `{}`".format(to_path))

            data = r.json()
            return {"cache": data["VersionId"]}
        else:
            try:
                from latch_cli.services.cp import cp

                # todo(ayush) cache version ids
                cp(file_path, to_path)
            except Exception as e:
                raise FlyteUserException("failed to get presigned upload urls for `{}`".format(to_path)) from e

    def upload(self, file_path: str, to_path: str):
        """
        :param str file_path:
        :param str to_path:
        """
        return LatchPersistence._upload(file_path, to_path, self._chunk_size, self._latch_endpoint)

    def upload_directory(self, local_path: str, remote_path: str):
        """
        :param str local_path:
        :param str remote_path:
        """
        if remote_path == "latch://":
            remote_path = "latch:///"

        # ensure formatting
        local_path = _enforce_trailing_slash(local_path)
        remote_path = _enforce_trailing_slash(remote_path)

        task_tuples = []
        files_to_upload = [_os.path.join(dp, f) for dp, __, filenames in _os.walk(local_path) for f in filenames]
        for file_path in files_to_upload:
            relative_name = file_path.replace(local_path, "", 1)
            if relative_name.startswith("/"):
                relative_name = relative_name[1:]
            # TODO(aidan): change this to form data (all at once)
            task_tuples.append((file_path, remote_path + relative_name, self._chunk_size, self._latch_endpoint))

        pool = ThreadPool(100)
        pool.map(LatchPersistence.__upload, task_tuples)
        pool.start()
        pool.wait_completion()

        cache = base64.standard_b64encode(bytes(pool.cache_accum)).decode("ascii")
        return {"cache": cache}

    def construct_path(self, add_protocol: bool, add_prefix: bool, *paths: str) -> str:
        paths = list(paths)  # make type check happy
        if add_prefix:
            paths.insert(0, self.default_prefix)
        path = "/".join(paths)
        if add_protocol:
            return f"{self.PROTOCOL}{path}"
        return path

    def get(self, from_path: str, to_path: str, recursive: bool = False):
        if not from_path.startswith(self.PROTOCOL):
            raise ValueError(f"expected a Latch URL (latch://...): {from_path}")

        if recursive:
            return self.download_directory(from_path, to_path)

        return self.download(from_path, to_path)

    def put(self, from_path: str, to_path: str, recursive: bool = False):
        if not to_path.startswith(self.PROTOCOL):
            raise ValueError(f"expected a Latch URL (latch://...): {to_path}")

        if recursive:
            return self.upload_directory(from_path, to_path)

        return self.upload(from_path, to_path)


DataPersistencePlugins.register_plugin(LatchPersistence.PROTOCOL, LatchPersistence)
