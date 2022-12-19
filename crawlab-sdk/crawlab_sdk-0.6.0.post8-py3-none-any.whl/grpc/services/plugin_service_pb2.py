# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/plugin_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from crawlab.grpc.entity import plugin_request_pb2 as entity_dot_plugin__request__pb2
from crawlab.grpc.entity import response_pb2 as entity_dot_response__pb2
from crawlab.grpc.entity import stream_message_pb2 as entity_dot_stream__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/plugin_service.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=b'Z\006.;grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dservices/plugin_service.proto\x12\x04grpc\x1a\x1b\x65ntity/plugin_request.proto\x1a\x15\x65ntity/response.proto\x1a\x1b\x65ntity/stream_message.proto2\xb5\x01\n\rPluginService\x12\x31\n\x08Register\x12\x13.grpc.PluginRequest\x1a\x0e.grpc.Response\"\x00\x12\x39\n\tSubscribe\x12\x13.grpc.PluginRequest\x1a\x13.grpc.StreamMessage\"\x00\x30\x01\x12\x36\n\x04Poll\x12\x13.grpc.StreamMessage\x1a\x13.grpc.StreamMessage\"\x00(\x01\x30\x01\x42\x08Z\x06.;grpcb\x06proto3'
  ,
  dependencies=[entity_dot_plugin__request__pb2.DESCRIPTOR,entity_dot_response__pb2.DESCRIPTOR,entity_dot_stream__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PLUGINSERVICE = _descriptor.ServiceDescriptor(
  name='PluginService',
  full_name='grpc.PluginService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=121,
  serialized_end=302,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='grpc.PluginService.Register',
    index=0,
    containing_service=None,
    input_type=entity_dot_plugin__request__pb2._PLUGINREQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='grpc.PluginService.Subscribe',
    index=1,
    containing_service=None,
    input_type=entity_dot_plugin__request__pb2._PLUGINREQUEST,
    output_type=entity_dot_stream__message__pb2._STREAMMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Poll',
    full_name='grpc.PluginService.Poll',
    index=2,
    containing_service=None,
    input_type=entity_dot_stream__message__pb2._STREAMMESSAGE,
    output_type=entity_dot_stream__message__pb2._STREAMMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PLUGINSERVICE)

DESCRIPTOR.services_by_name['PluginService'] = _PLUGINSERVICE

# @@protoc_insertion_point(module_scope)
