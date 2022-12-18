# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0f\x61nalytics.proto"\xe7\x02\n\tAnalytics\x12\x11\n\tsystem_id\x18\x01 \x02(\t\x12\x39\n\x13online_content_apps\x18\x02 \x01(\x0b\x32\x1c.Analytics.OnlineContentApps\x12\x30\n\x0eonline_workers\x18\x03 \x01(\x0b\x32\x18.Analytics.OnlineWorkers\x12(\n\ncomponents\x18\x04 \x03(\x0b\x32\x14.Analytics.Component\x12\x1a\n\x12postgresql_version\x18\x05 \x01(\r\x1a\x35\n\x11OnlineContentApps\x12\x11\n\tprocesses\x18\x01 \x01(\r\x12\r\n\x05hosts\x18\x02 \x01(\r\x1a\x31\n\rOnlineWorkers\x12\x11\n\tprocesses\x18\x01 \x01(\r\x12\r\n\x05hosts\x18\x02 \x01(\r\x1a*\n\tComponent\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\t'
)


_ANALYTICS = DESCRIPTOR.message_types_by_name["Analytics"]
_ANALYTICS_ONLINECONTENTAPPS = _ANALYTICS.nested_types_by_name["OnlineContentApps"]
_ANALYTICS_ONLINEWORKERS = _ANALYTICS.nested_types_by_name["OnlineWorkers"]
_ANALYTICS_COMPONENT = _ANALYTICS.nested_types_by_name["Component"]
Analytics = _reflection.GeneratedProtocolMessageType(
    "Analytics",
    (_message.Message,),
    {
        "OnlineContentApps": _reflection.GeneratedProtocolMessageType(
            "OnlineContentApps",
            (_message.Message,),
            {
                "DESCRIPTOR": _ANALYTICS_ONLINECONTENTAPPS,
                "__module__": "analytics_pb2"
                # @@protoc_insertion_point(class_scope:Analytics.OnlineContentApps)
            },
        ),
        "OnlineWorkers": _reflection.GeneratedProtocolMessageType(
            "OnlineWorkers",
            (_message.Message,),
            {
                "DESCRIPTOR": _ANALYTICS_ONLINEWORKERS,
                "__module__": "analytics_pb2"
                # @@protoc_insertion_point(class_scope:Analytics.OnlineWorkers)
            },
        ),
        "Component": _reflection.GeneratedProtocolMessageType(
            "Component",
            (_message.Message,),
            {
                "DESCRIPTOR": _ANALYTICS_COMPONENT,
                "__module__": "analytics_pb2"
                # @@protoc_insertion_point(class_scope:Analytics.Component)
            },
        ),
        "DESCRIPTOR": _ANALYTICS,
        "__module__": "analytics_pb2"
        # @@protoc_insertion_point(class_scope:Analytics)
    },
)
_sym_db.RegisterMessage(Analytics)
_sym_db.RegisterMessage(Analytics.OnlineContentApps)
_sym_db.RegisterMessage(Analytics.OnlineWorkers)
_sym_db.RegisterMessage(Analytics.Component)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ANALYTICS._serialized_start = 20
    _ANALYTICS._serialized_end = 379
    _ANALYTICS_ONLINECONTENTAPPS._serialized_start = 231
    _ANALYTICS_ONLINECONTENTAPPS._serialized_end = 284
    _ANALYTICS_ONLINEWORKERS._serialized_start = 286
    _ANALYTICS_ONLINEWORKERS._serialized_end = 335
    _ANALYTICS_COMPONENT._serialized_start = 337
    _ANALYTICS_COMPONENT._serialized_end = 379
# @@protoc_insertion_point(module_scope)
