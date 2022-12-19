"""
Python mapping for the ModelIO framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
import Quartz
from ModelIO import _metadata, _ModelIO

sys.modules["ModelIO"] = mod = objc.ObjCLazyModule(
    "ModelIO",
    "com.apple.ModelIO",
    objc.pathForFramework("/System/Library/Frameworks/ModelIO.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_ModelIO, Cocoa, Quartz),
)


del sys.modules["ModelIO._metadata"]
