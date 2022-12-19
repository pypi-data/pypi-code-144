# This file is generated by objective.metadata
#
# Last update: Wed Oct 19 11:27:09 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
misc.update(
    {
        "CLLocationCoordinate2D": objc.createStructType(
            "CoreLocation.CLLocationCoordinate2D",
            b"{CLLocationCoordinate2D=dd}",
            ["latitude", "longitude"],
        )
    }
)
constants = """$CLLocationDistanceMax@d$CLLocationPushServiceErrorDomain$CLTimeIntervalMax@d$kCLDistanceFilterNone@d$kCLErrorDomain$kCLErrorUserInfoAlternateRegionKey$kCLHeadingFilterNone@d$kCLLocationAccuracyBest@d$kCLLocationAccuracyBestForNavigation@d$kCLLocationAccuracyHundredMeters@d$kCLLocationAccuracyKilometer@d$kCLLocationAccuracyNearestTenMeters@d$kCLLocationAccuracyReduced@d$kCLLocationAccuracyThreeKilometers@d$kCLLocationCoordinate2DInvalid@{CLLocationCoordinate2D=dd}$"""
enums = """$CLAccuracyAuthorizationFullAccuracy@0$CLAccuracyAuthorizationReducedAccuracy@1$CLActivityTypeAirborne@5$CLActivityTypeAutomotiveNavigation@2$CLActivityTypeFitness@3$CLActivityTypeOther@1$CLActivityTypeOtherNavigation@4$CLDeviceOrientationFaceDown@6$CLDeviceOrientationFaceUp@5$CLDeviceOrientationLandscapeLeft@3$CLDeviceOrientationLandscapeRight@4$CLDeviceOrientationPortrait@1$CLDeviceOrientationPortraitUpsideDown@2$CLDeviceOrientationUnknown@0$CLLocationPushServiceErrorMissingEntitlement@3$CLLocationPushServiceErrorMissingPushExtension@1$CLLocationPushServiceErrorMissingPushServerEnvironment@2$CLLocationPushServiceErrorUnknown@0$CLProximityFar@3$CLProximityImmediate@1$CLProximityNear@2$CLProximityUnknown@0$CLRegionStateInside@1$CLRegionStateOutside@2$CLRegionStateUnknown@0$kCLAuthorizationStatusAuthorized@3$kCLAuthorizationStatusAuthorizedAlways@3$kCLAuthorizationStatusAuthorizedWhenInUse@4$kCLAuthorizationStatusDenied@2$kCLAuthorizationStatusNotDetermined@0$kCLAuthorizationStatusRestricted@1$kCLErrorDeferredAccuracyTooLow@13$kCLErrorDeferredCanceled@15$kCLErrorDeferredDistanceFiltered@14$kCLErrorDeferredFailed@11$kCLErrorDeferredNotUpdatingLocation@12$kCLErrorDenied@1$kCLErrorGeocodeFoundPartialResult@9$kCLErrorHeadingFailure@3$kCLErrorHistoricalLocationError@19$kCLErrorLocationUnknown@0$kCLErrorNetwork@2$kCLErrorPromptDeclined@18$kCLErrorRangingFailure@17$kCLErrorRangingUnavailable@16$kCLErrorRegionMonitoringDenied@4$kCLErrorRegionMonitoringFailure@5$kCLErrorRegionMonitoringResponseDelayed@7$kCLErrorRegionMonitoringSetupDelayed@6$"""
misc.update(
    {
        "CLAccuracyAuthorization": NewType("CLAccuracyAuthorization", int),
        "CLError": NewType("CLError", int),
        "CLProximity": NewType("CLProximity", int),
        "CLActivityType": NewType("CLActivityType", int),
        "CLRegionState": NewType("CLRegionState", int),
        "CLDeviceOrientation": NewType("CLDeviceOrientation", int),
        "CLAuthorizationStatus": NewType("CLAuthorizationStatus", int),
        "CLLocationPushServiceError": NewType("CLLocationPushServiceError", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "CLLocationCoordinate2DIsValid": (b"Z{CLLocationCoordinate2D=dd}",),
    "CLLocationCoordinate2DMake": (b"{CLLocationCoordinate2D=dd}dd",),
}
aliases = {"kCLAuthorizationStatusAuthorized": "kCLAuthorizationStatusAuthorizedAlways"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"CLBeaconRegion", b"notifyEntryStateOnDisplay", {"retval": {"type": b"Z"}})
    r(
        b"CLBeaconRegion",
        b"setNotifyEntryStateOnDisplay:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CLCircularRegion",
        b"center",
        {"retval": {"type": b"{CLLocationCoordinate2D=dd}"}},
    )
    r(
        b"CLCircularRegion",
        b"containsCoordinate:",
        {
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"{CLLocationCoordinate2D=dd}"}},
        },
    )
    r(
        b"CLCircularRegion",
        b"initWithCenter:radius:identifier:",
        {"arguments": {2: {"type": b"{CLLocationCoordinate2D=dd}"}}},
    )
    r(
        b"CLGeocoder",
        b"geocodeAddressDictionary:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLGeocoder",
        b"geocodeAddressString:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLGeocoder",
        b"geocodeAddressString:inRegion:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLGeocoder",
        b"geocodeAddressString:inRegion:preferredLocale:completionHandler:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLGeocoder",
        b"geocodePostalAddress:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLGeocoder",
        b"geocodePostalAddress:preferredLocale:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"CLGeocoder", b"isGeocoding", {"retval": {"type": b"Z"}})
    r(
        b"CLGeocoder",
        b"reverseGeocodeLocation:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLGeocoder",
        b"reverseGeocodeLocation:preferredLocale:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"CLLocation", b"coordinate", {"retval": {"type": "{CLLocationCoordinate2D=dd}"}})
    r(
        b"CLLocation",
        b"initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:course:speed:timestamp:",
        {"arguments": {2: {"type": b"{CLLocationCoordinate2D=dd}"}}},
    )
    r(
        b"CLLocation",
        b"initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:",
        {"arguments": {2: {"type": "{CLLocationCoordinate2D=dd}"}}},
    )
    r(
        b"CLLocationManager",
        b"allowsBackgroundLocationUpdates",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"CLLocationManager",
        b"deferredLocationUpdatesAvailable",
        {"retval": {"type": b"Z"}},
    )
    r(b"CLLocationManager", b"headingAvailable", {"retval": {"type": b"Z"}})
    r(
        b"CLLocationManager",
        b"isAuthorizedForPreciseLocation",
        {"retval": {"type": "Z"}},
    )
    r(b"CLLocationManager", b"isAuthorizedForWidgetUpdates", {"retval": {"type": b"Z"}})
    r(
        b"CLLocationManager",
        b"isMonitoringAvailableForClass:",
        {"retval": {"type": b"Z"}},
    )
    r(b"CLLocationManager", b"isRangingAvailable", {"retval": {"type": b"Z"}})
    r(b"CLLocationManager", b"locationServicesEnabled", {"retval": {"type": "Z"}})
    r(
        b"CLLocationManager",
        b"pausesLocationUpdatesAutomatically",
        {"retval": {"type": b"Z"}},
    )
    r(b"CLLocationManager", b"regionMonitoringAvailable", {"retval": {"type": b"Z"}})
    r(b"CLLocationManager", b"regionMonitoringEnabled", {"retval": {"type": b"Z"}})
    r(
        b"CLLocationManager",
        b"requestHistoricalLocationsWithPurposeKey:sampleCount:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLLocationManager",
        b"requestTemporaryFullAccuracyAuthorizationWithPurposeKey:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CLLocationManager",
        b"requestTemporaryPreciseLocationAuthorizationWithPurposeKey:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CLLocationManager",
        b"setAllowsBackgroundLocationUpdates:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CLLocationManager",
        b"setPausesLocationUpdatesAutomatically:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CLLocationManager",
        b"setShowsBackgroundLocationIndicator:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CLLocationManager",
        b"showsBackgroundLocationIndicator",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"CLLocationManager",
        b"significantLocationChangeMonitoringAvailable",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"CLLocationManager",
        b"startMonitoringLocationPushesWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLLocationSourceInformation",
        b"initWithSoftwareSimulationState:andExternalAccessoryState:",
        {"arguments": {2: {"type": b"Z"}, 3: {"type": b"Z"}}},
    )
    r(
        b"CLLocationSourceInformation",
        b"isProducedByAccessory",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"CLLocationSourceInformation",
        b"isSimulatedBySoftware",
        {"retval": {"type": b"Z"}},
    )
    r(b"CLRegion", b"center", {"retval": {"type": b"{CLLocationCoordinate2D=dd}"}})
    r(
        b"CLRegion",
        b"containsCoordinate:",
        {
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"{CLLocationCoordinate2D=dd}"}},
        },
    )
    r(
        b"CLRegion",
        b"initCircularRegionWithCenter:radius:identifier:",
        {"arguments": {2: {"type": b"{CLLocationCoordinate2D=dd}"}}},
    )
    r(b"CLRegion", b"notifyOnEntry", {"retval": {"type": b"Z"}})
    r(b"CLRegion", b"notifyOnExit", {"retval": {"type": b"Z"}})
    r(b"CLRegion", b"setNotifyOnEntry:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CLRegion", b"setNotifyOnExit:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"NSObject",
        b"didReceiveLocationPushPayload:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"locationManager:didChangeAuthorizationStatus:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"i"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didDetermineState:forRegion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"q"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didEnterRegion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didExitRegion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didFailRangingBeaconsForConstraint:error:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didFailWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didFinishDeferredUpdatesWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didRangeBeacons:inRegion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didRangeBeacons:satisfyingConstraint:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didStartMonitoringForRegion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didUpdateHeading:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didUpdateLocations:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didUpdateToLocation:fromLocation:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:didVisit:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:monitoringDidFailForRegion:withError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManager:rangingBeaconsDidFailForRegion:withError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"locationManagerDidChangeAuthorization:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"locationManagerDidPauseLocationUpdates:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"locationManagerDidResumeLocationUpdates:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"locationManagerShouldDisplayHeadingCalibration:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"serviceExtensionWillTerminate",
        {"required": False, "retval": {"type": b"v"}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
