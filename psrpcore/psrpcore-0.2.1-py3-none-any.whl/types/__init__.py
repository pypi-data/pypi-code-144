# -*- coding: utf-8 -*-
# Copyright: (c) 2021", Jordan Borean (@jborean93) <jborean93@gmail.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

"""The .NET type code.

Contains the public entrypoint for all the .NET/Pwsh type code that is used to
exchange objects between Python and PowerShell.
"""

import logging

from psrpcore.types._base import (
    PSAliasProperty,
    PSCryptoProvider,
    PSNoteProperty,
    PSObject,
    PSPropertyInfo,
    PSScriptProperty,
    PSType,
    add_alias_property,
    add_member,
    add_note_property,
    add_script_property,
    ps_isinstance,
)
from psrpcore.types._collection import (
    PSDict,
    PSDictBase,
    PSIEnumerable,
    PSList,
    PSListBase,
    PSQueue,
    PSQueueBase,
    PSStack,
    PSStackBase,
)
from psrpcore.types._complex import (
    ApartmentState,
    CommandMetadataCount,
    CommandOrigin,
    CommandTypes,
    ConsoleColor,
    DebugRecord,
    ErrorCategory,
    ErrorCategoryInfo,
    ErrorDetails,
    ErrorRecord,
    InformationalRecord,
    InformationRecord,
    InvocationInfo,
    NETException,
    PipelineResultTypes,
    ProgressRecord,
    ProgressRecordType,
    PSCredential,
    PSCredentialTypes,
    PSCredentialUIOptions,
    PSCustomObject,
    PSInvocationState,
    PSPrimitiveDictionary,
    PSThreadOptions,
    RemoteStreamOptions,
    RunspacePoolState,
    ScriptExtent,
    ScriptPosition,
    SessionStateEntryVisibility,
    VerboseRecord,
    WarningRecord,
)
from psrpcore.types._enum import PSEnumBase, PSFlagBase
from psrpcore.types._host import (
    BufferCell,
    BufferCellType,
    ChoiceDescription,
    ControlKeyStates,
    Coordinates,
    FieldDescription,
    HostDefaultData,
    HostInfo,
    HostMethodIdentifier,
    KeyInfo,
    ReadKeyOptions,
    Rectangle,
    Size,
)
from psrpcore.types._primitive import (
    PSBool,
    PSByte,
    PSByteArray,
    PSChar,
    PSDateTime,
    PSDecimal,
    PSDouble,
    PSDuration,
    PSGuid,
    PSInt,
    PSInt16,
    PSInt64,
    PSNull,
    PSSByte,
    PSScriptBlock,
    PSSecureString,
    PSSingle,
    PSString,
    PSUInt,
    PSUInt16,
    PSUInt64,
    PSUri,
    PSVersion,
    PSXml,
)
from psrpcore.types._psrp import (
    ApplicationPrivateData,
    ConnectRunspacePool,
    CreatePipeline,
    DebugRecordMsg,
    EncryptedSessionKey,
    EndOfPipelineInput,
    ErrorRecordMsg,
    GetAvailableRunspaces,
    GetCommandMetadata,
    InformationRecordMsg,
    InitRunspacePool,
    PipelineHostCall,
    PipelineHostResponse,
    PipelineInput,
    PipelineOutput,
    PipelineState,
    ProgressRecordMsg,
    PSRPMessageType,
    PublicKey,
    PublicKeyRequest,
    ResetRunspaceState,
    RunspaceAvailability,
    RunspacePoolHostCall,
    RunspacePoolHostResponse,
    RunspacePoolInitData,
    RunspacePoolStateMsg,
    SessionCapability,
    SetMaxRunspaces,
    SetMinRunspaces,
    UserEvent,
    VerboseRecordMsg,
    WarningRecordMsg,
)
from psrpcore.types._serializer import deserialize, serialize

logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = [
    "ApartmentState",
    "ApplicationPrivateData",
    "BufferCell",
    "BufferCellType",
    "ChoiceDescription",
    "CommandMetadataCount",
    "CommandOrigin",
    "CommandTypes",
    "ConnectRunspacePool",
    "ConsoleColor",
    "ControlKeyStates",
    "Coordinates",
    "CreatePipeline",
    "DebugRecord",
    "DebugRecordMsg",
    "EncryptedSessionKey",
    "EndOfPipelineInput",
    "ErrorCategory",
    "ErrorCategoryInfo",
    "ErrorDetails",
    "ErrorRecord",
    "ErrorRecordMsg",
    "FieldDescription",
    "GetAvailableRunspaces",
    "GetCommandMetadata",
    "HostDefaultData",
    "HostInfo",
    "HostMethodIdentifier",
    "InformationRecord",
    "InformationRecordMsg",
    "InformationalRecord",
    "InitRunspacePool",
    "InvocationInfo",
    "KeyInfo",
    "NETException",
    "PSAliasProperty",
    "PSBool",
    "PSByte",
    "PSByteArray",
    "PSChar",
    "PSCredential",
    "PSCredentialTypes",
    "PSCredentialUIOptions",
    "PSCryptoProvider",
    "PSCustomObject",
    "PSDateTime",
    "PSDecimal",
    "PSDict",
    "PSDictBase",
    "PSDouble",
    "PSDuration",
    "PSEnumBase",
    "PSFlagBase",
    "PSGuid",
    "PSIEnumerable",
    "PSInt",
    "PSInt16",
    "PSInt64",
    "PSInvocationState",
    "PSList",
    "PSListBase",
    "PSNoteProperty",
    "PSNull",
    "PSObject",
    "PSPrimitiveDictionary",
    "PSPropertyInfo",
    "PSQueue",
    "PSQueueBase",
    "PSRPMessageType",
    "PSSByte",
    "PSScriptBlock",
    "PSScriptProperty",
    "PSSecureString",
    "PSSingle",
    "PSStack",
    "PSStackBase",
    "PSString",
    "PSThreadOptions",
    "PSType",
    "PSUInt",
    "PSUInt16",
    "PSUInt64",
    "PSUri",
    "PSVersion",
    "PSXml",
    "PipelineHostCall",
    "PipelineHostResponse",
    "PipelineInput",
    "PipelineOutput",
    "PipelineResultTypes",
    "PipelineState",
    "ProgressRecord",
    "ProgressRecordMsg",
    "ProgressRecordType",
    "PublicKey",
    "PublicKeyRequest",
    "ReadKeyOptions",
    "Rectangle",
    "RemoteStreamOptions",
    "ResetRunspaceState",
    "RunspaceAvailability",
    "RunspacePoolHostCall",
    "RunspacePoolHostResponse",
    "RunspacePoolInitData",
    "RunspacePoolState",
    "RunspacePoolStateMsg",
    "ScriptExtent",
    "ScriptPosition",
    "SessionCapability",
    "SessionStateEntryVisibility",
    "SetMaxRunspaces",
    "SetMinRunspaces",
    "Size",
    "UserEvent",
    "VerboseRecord",
    "VerboseRecordMsg",
    "WarningRecord",
    "WarningRecordMsg",
    "add_alias_property",
    "add_member",
    "add_note_property",
    "add_script_property",
    "deserialize",
    "ps_isinstance",
    "serialize",
]
