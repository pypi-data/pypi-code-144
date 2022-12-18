# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

"""Control of and utilities for debugging."""

import contextlib
import functools
import inspect
import io
import itertools
import os
import pprint
import reprlib
import sys
import types
import _thread

from coverage.misc import isolate_module

os = isolate_module(os)


# When debugging, it can be helpful to force some options, especially when
# debugging the configuration mechanisms you usually use to control debugging!
# This is a list of forced debugging options.
FORCED_DEBUG = []
FORCED_DEBUG_FILE = None


class DebugControl:
    """Control and output for debugging."""

    show_repr_attr = False      # For AutoReprMixin

    def __init__(self, options, output):
        """Configure the options and output file for debugging."""
        self.options = list(options) + FORCED_DEBUG
        self.suppress_callers = False

        filters = []
        if self.should('pid'):
            filters.append(add_pid_and_tid)
        self.output = DebugOutputFile.get_one(
            output,
            show_process=self.should('process'),
            filters=filters,
        )
        self.raw_output = self.output.outfile

    def __repr__(self):
        return f"<DebugControl options={self.options!r} raw_output={self.raw_output!r}>"

    def should(self, option):
        """Decide whether to output debug information in category `option`."""
        if option == "callers" and self.suppress_callers:
            return False
        return (option in self.options)

    @contextlib.contextmanager
    def without_callers(self):
        """A context manager to prevent call stacks from being logged."""
        old = self.suppress_callers
        self.suppress_callers = True
        try:
            yield
        finally:
            self.suppress_callers = old

    def write(self, msg):
        """Write a line of debug output.

        `msg` is the line to write. A newline will be appended.

        """
        self.output.write(msg+"\n")
        if self.should('self'):
            caller_self = inspect.stack()[1][0].f_locals.get('self')
            if caller_self is not None:
                self.output.write(f"self: {caller_self!r}\n")
        if self.should('callers'):
            dump_stack_frames(out=self.output, skip=1)
        self.output.flush()


class DebugControlString(DebugControl):
    """A `DebugControl` that writes to a StringIO, for testing."""
    def __init__(self, options):
        super().__init__(options, io.StringIO())

    def get_output(self):
        """Get the output text from the `DebugControl`."""
        return self.raw_output.getvalue()


class NoDebugging:
    """A replacement for DebugControl that will never try to do anything."""
    def should(self, option):               # pylint: disable=unused-argument
        """Should we write debug messages?  Never."""
        return False


def info_header(label):
    """Make a nice header string."""
    return "--{:-<60s}".format(" "+label+" ")


def info_formatter(info):
    """Produce a sequence of formatted lines from info.

    `info` is a sequence of pairs (label, data).  The produced lines are
    nicely formatted, ready to print.

    """
    info = list(info)
    if not info:
        return
    label_len = 30
    assert all(len(l) < label_len for l, _ in info)
    for label, data in info:
        if data == []:
            data = "-none-"
        if isinstance(data, tuple) and len(repr(tuple(data))) < 30:
            # Convert to tuple to scrub namedtuples.
            yield "%*s: %r" % (label_len, label, tuple(data))
        elif isinstance(data, (list, set, tuple)):
            prefix = "%*s:" % (label_len, label)
            for e in data:
                yield "%*s %s" % (label_len+1, prefix, e)
                prefix = ""
        else:
            yield "%*s: %s" % (label_len, label, data)


def write_formatted_info(write, header, info):
    """Write a sequence of (label,data) pairs nicely.

    `write` is a function write(str) that accepts each line of output.
    `header` is a string to start the section.  `info` is a sequence of
    (label, data) pairs, where label is a str, and data can be a single
    value, or a list/set/tuple.

    """
    write(info_header(header))
    for line in info_formatter(info):
        write(f" {line}")


def short_stack(limit=None, skip=0):
    """Return a string summarizing the call stack.

    The string is multi-line, with one line per stack frame. Each line shows
    the function name, the file name, and the line number:

        ...
        start_import_stop : /Users/ned/coverage/trunk/tests/coveragetest.py @95
        import_local_file : /Users/ned/coverage/trunk/tests/coveragetest.py @81
        import_local_file : /Users/ned/coverage/trunk/coverage/backward.py @159
        ...

    `limit` is the number of frames to include, defaulting to all of them.

    `skip` is the number of frames to skip, so that debugging functions can
    call this and not be included in the result.

    """
    stack = inspect.stack()[limit:skip:-1]
    return "\n".join("%30s : %s:%d" % (t[3], t[1], t[2]) for t in stack)


def dump_stack_frames(limit=None, out=None, skip=0):
    """Print a summary of the stack to stdout, or someplace else."""
    out = out or sys.stdout
    out.write(short_stack(limit=limit, skip=skip+1))
    out.write("\n")


def clipped_repr(text, numchars=50):
    """`repr(text)`, but limited to `numchars`."""
    r = reprlib.Repr()
    r.maxstring = numchars
    return r.repr(text)


def short_id(id64):
    """Given a 64-bit id, make a shorter 16-bit one."""
    id16 = 0
    for offset in range(0, 64, 16):
        id16 ^= id64 >> offset
    return id16 & 0xFFFF


def add_pid_and_tid(text):
    """A filter to add pid and tid to debug messages."""
    # Thread ids are useful, but too long. Make a shorter one.
    tid = f"{short_id(_thread.get_ident()):04x}"
    text = f"{os.getpid():5d}.{tid}: {text}"
    return text


class AutoReprMixin:
    """A mixin implementing an automatic __repr__ for debugging."""
    auto_repr_ignore = ['auto_repr_ignore', '$coverage.object_id']

    def __repr__(self):
        show_attrs = (
            (k, v) for k, v in self.__dict__.items()
            if getattr(v, "show_repr_attr", True)
            and not callable(v)
            and k not in self.auto_repr_ignore
        )
        return "<{klass} @0x{id:x} {attrs}>".format(
            klass=self.__class__.__name__,
            id=id(self),
            attrs=" ".join(f"{k}={v!r}" for k, v in show_attrs),
        )


def simplify(v):                                            # pragma: debugging
    """Turn things which are nearly dict/list/etc into dict/list/etc."""
    if isinstance(v, dict):
        return {k:simplify(vv) for k, vv in v.items()}
    elif isinstance(v, (list, tuple)):
        return type(v)(simplify(vv) for vv in v)
    elif hasattr(v, "__dict__"):
        return simplify({'.'+k: v for k, v in v.__dict__.items()})
    else:
        return v


def pp(v):                                                  # pragma: debugging
    """Debug helper to pretty-print data, including SimpleNamespace objects."""
    # Might not be needed in 3.9+
    pprint.pprint(simplify(v))


def filter_text(text, filters):
    """Run `text` through a series of filters.

    `filters` is a list of functions. Each takes a string and returns a
    string.  Each is run in turn.

    Returns: the final string that results after all of the filters have
    run.

    """
    clean_text = text.rstrip()
    ending = text[len(clean_text):]
    text = clean_text
    for fn in filters:
        lines = []
        for line in text.splitlines():
            lines.extend(fn(line).splitlines())
        text = "\n".join(lines)
    return text + ending


class CwdTracker:                                   # pragma: debugging
    """A class to add cwd info to debug messages."""
    def __init__(self):
        self.cwd = None

    def filter(self, text):
        """Add a cwd message for each new cwd."""
        cwd = os.getcwd()
        if cwd != self.cwd:
            text = f"cwd is now {cwd!r}\n" + text
            self.cwd = cwd
        return text


class DebugOutputFile:                              # pragma: debugging
    """A file-like object that includes pid and cwd information."""
    def __init__(self, outfile, show_process, filters):
        self.outfile = outfile
        self.show_process = show_process
        self.filters = list(filters)

        if self.show_process:
            self.filters.insert(0, CwdTracker().filter)
            self.write(f"New process: executable: {sys.executable!r}\n")
            self.write("New process: cmd: {!r}\n".format(getattr(sys, 'argv', None)))
            if hasattr(os, 'getppid'):
                self.write(f"New process: pid: {os.getpid()!r}, parent pid: {os.getppid()!r}\n")

    SYS_MOD_NAME = '$coverage.debug.DebugOutputFile.the_one'
    SINGLETON_ATTR = 'the_one_and_is_interim'

    @classmethod
    def get_one(cls, fileobj=None, show_process=True, filters=(), interim=False):
        """Get a DebugOutputFile.

        If `fileobj` is provided, then a new DebugOutputFile is made with it.

        If `fileobj` isn't provided, then a file is chosen
        (COVERAGE_DEBUG_FILE, or stderr), and a process-wide singleton
        DebugOutputFile is made.

        `show_process` controls whether the debug file adds process-level
        information, and filters is a list of other message filters to apply.

        `filters` are the text filters to apply to the stream to annotate with
        pids, etc.

        If `interim` is true, then a future `get_one` can replace this one.

        """
        if fileobj is not None:
            # Make DebugOutputFile around the fileobj passed.
            return cls(fileobj, show_process, filters)

        # Because of the way igor.py deletes and re-imports modules,
        # this class can be defined more than once. But we really want
        # a process-wide singleton. So stash it in sys.modules instead of
        # on a class attribute. Yes, this is aggressively gross.
        singleton_module = sys.modules.get(cls.SYS_MOD_NAME)
        the_one, is_interim = getattr(singleton_module, cls.SINGLETON_ATTR, (None, True))
        if the_one is None or is_interim:
            if fileobj is None:
                debug_file_name = os.environ.get("COVERAGE_DEBUG_FILE", FORCED_DEBUG_FILE)
                if debug_file_name in ("stdout", "stderr"):
                    fileobj = getattr(sys, debug_file_name)
                elif debug_file_name:
                    fileobj = open(debug_file_name, "a")
                else:
                    fileobj = sys.stderr
            the_one = cls(fileobj, show_process, filters)
            singleton_module = types.ModuleType(cls.SYS_MOD_NAME)
            setattr(singleton_module, cls.SINGLETON_ATTR, (the_one, interim))
            sys.modules[cls.SYS_MOD_NAME] = singleton_module
        return the_one

    def write(self, text):
        """Just like file.write, but filter through all our filters."""
        self.outfile.write(filter_text(text, self.filters))
        self.outfile.flush()

    def flush(self):
        """Flush our file."""
        self.outfile.flush()


def log(msg, stack=False):                                  # pragma: debugging
    """Write a log message as forcefully as possible."""
    out = DebugOutputFile.get_one(interim=True)
    out.write(msg+"\n")
    if stack:
        dump_stack_frames(out=out, skip=1)


def decorate_methods(decorator, butnot=(), private=False):  # pragma: debugging
    """A class decorator to apply a decorator to methods."""
    def _decorator(cls):
        for name, meth in inspect.getmembers(cls, inspect.isroutine):
            if name not in cls.__dict__:
                continue
            if name != "__init__":
                if not private and name.startswith("_"):
                    continue
            if name in butnot:
                continue
            setattr(cls, name, decorator(meth))
        return cls
    return _decorator


def break_in_pudb(func):                                    # pragma: debugging
    """A function decorator to stop in the debugger for each call."""
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        import pudb
        sys.stdout = sys.__stdout__
        pudb.set_trace()
        return func(*args, **kwargs)
    return _wrapper


OBJ_IDS = itertools.count()
CALLS = itertools.count()
OBJ_ID_ATTR = "$coverage.object_id"

def show_calls(show_args=True, show_stack=False, show_return=False):    # pragma: debugging
    """A method decorator to debug-log each call to the function."""
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(self, *args, **kwargs):
            oid = getattr(self, OBJ_ID_ATTR, None)
            if oid is None:
                oid = f"{os.getpid():08d} {next(OBJ_IDS):04d}"
                setattr(self, OBJ_ID_ATTR, oid)
            extra = ""
            if show_args:
                eargs = ", ".join(map(repr, args))
                ekwargs = ", ".join("{}={!r}".format(*item) for item in kwargs.items())
                extra += "("
                extra += eargs
                if eargs and ekwargs:
                    extra += ", "
                extra += ekwargs
                extra += ")"
            if show_stack:
                extra += " @ "
                extra += "; ".join(_clean_stack_line(l) for l in short_stack().splitlines())
            callid = next(CALLS)
            msg = f"{oid} {callid:04d} {func.__name__}{extra}\n"
            DebugOutputFile.get_one(interim=True).write(msg)
            ret = func(self, *args, **kwargs)
            if show_return:
                msg = f"{oid} {callid:04d} {func.__name__} return {ret!r}\n"
                DebugOutputFile.get_one(interim=True).write(msg)
            return ret
        return _wrapper
    return _decorator


def _clean_stack_line(s):                                   # pragma: debugging
    """Simplify some paths in a stack trace, for compactness."""
    s = s.strip()
    s = s.replace(os.path.dirname(__file__) + '/', '')
    s = s.replace(os.path.dirname(os.__file__) + '/', '')
    s = s.replace(sys.prefix + '/', '')
    return s
