# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:54:52 2022
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
constants = """$IMKCandidatesOpacityAttributeName$IMKCandidatesSendServerKeyEventFirst$IMKControllerClass$IMKDelegateClass$IMKModeDictionary$kIMKCommandClientName$kIMKCommandMenuItemName$"""
enums = """$kIMKAnnotation@1$kIMKLocateCandidatesAboveHint@1$kIMKLocateCandidatesBelowHint@2$kIMKLocateCandidatesLeftHint@3$kIMKLocateCandidatesRightHint@4$kIMKMain@0$kIMKScrollingGridCandidatePanel@2$kIMKSingleColumnScrollingCandidatePanel@1$kIMKSingleRowSteppingCandidatePanel@3$kIMKSubList@2$"""
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"IMKCandidates", b"dismissesAutomatically", {"retval": {"type": "Z"}})
    r(b"IMKCandidates", b"isVisible", {"retval": {"type": "Z"}})
    r(b"IMKCandidates", b"selectCandidateWithIdentifier:", {"retval": {"type": b"Z"}})
    r(
        b"IMKCandidates",
        b"selectionKeysKeylayout",
        {"retval": {"type": "^{__TISInputSource=}"}},
    )
    r(
        b"IMKCandidates",
        b"setDismissesAutomatically:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"IMKCandidates",
        b"setSelectionKeysKeylayout:",
        {"arguments": {2: {"type": "^{__TISInputSource=}"}}},
    )
    r(
        b"IMKInputController",
        b"doCommandBySelector:commandDictionary:",
        {"arguments": {2: {"type": ":", "sel_of_type": b"v@:@"}}},
    )
    r(b"IMKServer", b"lastKeyEventWasDeadKey", {"retval": {"type": b"Z"}})
    r(b"IMKServer", b"paletteWillTerminate", {"retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"activateServer:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"candidates:",
        {"retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"commitComposition:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"composedString:",
        {"retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"deactivateServer:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didCommandBySelector:client:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type": ":"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"handleEvent:client:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"inputText:client:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"inputText:key:modifiers:client:",
        {
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"q"},
                4: {"type": b"Q"},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"modes:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"mouseDownOnCharacterIndex:coordinate:withModifier:continueTracking:client:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": sel32or64(b"I", b"Q")},
                3: {"type": sel32or64(b"{_NSPoint=ff}", b"{CGPoint=dd}")},
                4: {"type": sel32or64(b"I", b"Q")},
                5: {"type": "^Z", "type_modifier": b"o"},
                6: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"mouseMovedOnCharacterIndex:coordinate:withModifier:client:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": sel32or64(b"I", b"Q")},
                3: {"type": sel32or64(b"{_NSPoint=ff}", b"{CGPoint=dd}")},
                4: {"type": sel32or64(b"I", b"Q")},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"mouseUpOnCharacterIndex:coordinate:withModifier:client:",
        {
            "required": True,
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": sel32or64(b"I", b"Q")},
                3: {"type": sel32or64(b"{_NSPoint=ff}", b"{CGPoint=dd}")},
                4: {"type": sel32or64(b"I", b"Q")},
                5: {"type": b"@"},
            },
        },
    )
    r(
        b"NSObject",
        b"originalString:",
        {"retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"recognizedEvents:",
        {"required": True, "retval": {"type": b"Q"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setValue:forTag:client:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"q"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"showPreferences:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"valueForTag:client:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"q"}, 3: {"type": b"@"}},
        },
    )
finally:
    objc._updatingMetadata(False)
protocols = {
    "IMKServerInput": objc.informal_protocol(
        "IMKServerInput",
        [
            objc.selector(None, b"inputText:client:", b"Z@:@@", isRequired=False),
            objc.selector(None, b"candidates:", b"@@:@", isRequired=False),
            objc.selector(
                None, b"didCommandBySelector:client:", b"Z@::@", isRequired=False
            ),
            objc.selector(None, b"handleEvent:client:", b"Z@:@@", isRequired=False),
            objc.selector(None, b"composedString:", b"@@:@", isRequired=False),
            objc.selector(
                None, b"inputText:key:modifiers:client:", b"Z@:@qQ@", isRequired=False
            ),
            objc.selector(None, b"commitComposition:", b"v@:@", isRequired=False),
            objc.selector(None, b"originalString:", b"@@:@", isRequired=False),
        ],
    )
}
expressions = {}

# END OF FILE
