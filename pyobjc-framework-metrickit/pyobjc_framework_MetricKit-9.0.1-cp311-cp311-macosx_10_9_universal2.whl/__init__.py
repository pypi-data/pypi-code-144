"""
Python mapping for the MetricKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Foundation
import objc
from . import _metadata, _MetricKit

sys.modules["MetricKit"] = mod = objc.ObjCLazyModule(
    "MetricKit",
    "com.apple.MetricKit",
    objc.pathForFramework("/System/Library/Frameworks/MetricKit.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (Foundation, _MetricKit),
)


del sys.modules["MetricKit._metadata"]
