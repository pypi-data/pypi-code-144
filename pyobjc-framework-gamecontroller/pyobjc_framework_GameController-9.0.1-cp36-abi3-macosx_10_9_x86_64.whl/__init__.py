"""
Python mapping for the GameController framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import objc
from GameController import _metadata
from GameController import _GameController

sys.modules["GameController"] = mod = objc.ObjCLazyModule(
    "GameController",
    "com.apple.GameController",
    objc.pathForFramework("/System/Library/Frameworks/GameController.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_GameController, Cocoa),
)


del sys.modules["GameController._metadata"]
