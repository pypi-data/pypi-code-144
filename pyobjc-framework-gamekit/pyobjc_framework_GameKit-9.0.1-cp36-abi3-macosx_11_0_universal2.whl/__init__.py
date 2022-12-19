"""
Python mapping for the GameKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from GameKit import _metadata
from GameKit import _GameKit

sys.modules["GameKit"] = mod = objc.ObjCLazyModule(
    "GameKit",
    "com.apple.GameKit",
    objc.pathForFramework("/System/Library/Frameworks/GameKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_GameKit, Cocoa),
)


del sys.modules["GameKit._metadata"]
