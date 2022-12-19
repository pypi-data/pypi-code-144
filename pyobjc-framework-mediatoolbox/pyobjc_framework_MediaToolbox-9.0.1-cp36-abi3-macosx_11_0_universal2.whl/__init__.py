"""
Python mapping for the MediaToolbox framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import MediaToolbox._MediaToolbox
import objc
from MediaToolbox import _metadata

sys.modules["MediaToolbox"] = mod = objc.ObjCLazyModule(
    "MediaToolbox",
    "com.apple.MediaToolbox",
    objc.pathForFramework("/System/Library/Frameworks/MediaToolbox.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation,),
)


for nm in dir(MediaToolbox._MediaToolbox):
    setattr(mod, nm, getattr(MediaToolbox._MediaToolbox, nm))


del sys.modules["MediaToolbox._metadata"]
