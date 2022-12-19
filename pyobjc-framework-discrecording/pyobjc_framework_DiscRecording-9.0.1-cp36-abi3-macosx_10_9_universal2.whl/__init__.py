"""
Python mapping for the DiscRecording framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys
from math import floor

import Foundation
import objc
from DiscRecording import _DiscRecording, _metadata

sys.modules["DiscRecording"] = mod = objc.ObjCLazyModule(
    "DiscRecording",
    "com.apple.DiscRecording",
    objc.pathForFramework("/System/Library/Frameworks/DiscRecording.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (_DiscRecording, Foundation),
)


del sys.modules["DiscRecording._metadata"]


def DRDeviceKPSForCDXFactor(xfactor):
    return float(xfactor) * mod.kDRDeviceBurnSpeedCD1x


def DRDeviceKPSForDVDXFactor(xfactor):
    return float(xfactor) * mod.kDRDeviceBurnSpeedDVD1x


def DRDeviceCDXFactorForKPS(kps):
    return floor(kps / mod.kDRDeviceBurnSpeedCD1x + 0.5)


def DRDeviceDVDXFactorForKPS(kps):
    return floor(kps / mod.kDRDeviceBurnSpeedDVD1x + 0.5)


mod.DRDeviceKPSForCDXFactor = DRDeviceKPSForCDXFactor
mod.DRDeviceKPSForDVDXFactor = DRDeviceKPSForDVDXFactor
mod.DRDeviceCDXFactorForKPS = DRDeviceCDXFactorForKPS
mod.DRDeviceDVDXFactorForKPS = DRDeviceDVDXFactorForKPS
