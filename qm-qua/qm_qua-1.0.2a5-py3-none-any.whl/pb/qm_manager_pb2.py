# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qm/pb/qm_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from qm.pb import inc_qua_config_pb2 as qm_dot_pb_dot_inc__qua__config__pb2
from qm.pb import general_messages_pb2 as qm_dot_pb_dot_general__messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qm/pb/qm_manager.proto',
  package='qm.grpc.qm_manager',
  syntax='proto3',
  serialized_options=b'\n\021qm.grpc.qmManagerB\016QmManagerProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16qm/pb/qm_manager.proto\x12\x12qm.grpc.qm_manager\x1a\x1aqm/pb/inc_qua_config.proto\x1a\x1cqm/pb/general_messages.proto\"\x9c\x01\n\x19OpenQuantumMachineRequest\x12-\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x1d.qm.grpc.qua_config.QuaConfig\x12\x0f\n\x05never\x18\x02 \x01(\x08H\x00\x12\x10\n\x06\x61lways\x18\x03 \x01(\x08H\x00\x12\x12\n\x08ifNeeded\x18\x04 \x01(\x08H\x00\x42\x19\n\x17oneOfCloseOtherMachines\"\x99\x02\n\x1aOpenQuantumMachineResponse\x12\x11\n\tmachineID\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12K\n\x16\x63onfigValidationErrors\x18\x03 \x03(\x0b\x32+.qm.grpc.qm_manager.ConfigValidationMessage\x12O\n\x18physicalValidationErrors\x18\x04 \x03(\x0b\x32-.qm.grpc.qm_manager.PhysicalValidationMessage\x12\x39\n\x0eopenQmWarnings\x18\x05 \x03(\x0b\x32!.qm.grpc.qm_manager.OpenQmWarning\"/\n\x1a\x43loseQuantumMachineRequest\x12\x11\n\tmachineID\x18\x01 \x01(\t\"f\n\x1b\x43loseQuantumMachineResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x36\n\x06\x65rrors\x18\x02 \x03(\x0b\x32&.qm.grpc.general_messages.ErrorMessage\"-\n\x18GetQuantumMachineRequest\x12\x11\n\tmachineID\x18\x01 \x01(\t\"\xa6\x01\n\x19GetQuantumMachineResponse\x12\x11\n\tmachineID\x18\x01 \x01(\t\x12-\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x1d.qm.grpc.qua_config.QuaConfig\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x36\n\x06\x65rrors\x18\x04 \x03(\x0b\x32&.qm.grpc.general_messages.ErrorMessage\")\n\x14GetRunningJobRequest\x12\x11\n\tmachineID\x18\x01 \x01(\t\"9\n\x15GetRunningJobResponse\x12\x11\n\tmachineID\x18\x01 \x01(\t\x12\r\n\x05jobId\x18\x02 \x01(\t\"5\n\x1fListOpenQuantumMachinesResponse\x12\x12\n\nmachineIDs\x18\x01 \x03(\t\"j\n\x1f\x43loseAllQuantumMachinesResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x36\n\x06\x65rrors\x18\x02 \x03(\x0b\x32&.qm.grpc.general_messages.ErrorMessage\"M\n\x16GetControllersResponse\x12\x33\n\x0b\x63ontrollers\x18\x01 \x03(\x0b\x32\x1e.qm.grpc.qm_manager.Controller\"\x1a\n\nController\x12\x0c\n\x04name\x18\x01 \x01(\t\"~\n\x17\x43onfigValidationMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x35\n\x05level\x18\x04 \x01(\x0e\x32&.qm.grpc.general_messages.MessageLevel\"\x80\x01\n\x19PhysicalValidationMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x35\n\x05level\x18\x04 \x01(\x0e\x32&.qm.grpc.general_messages.MessageLevel\".\n\rOpenQmWarning\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\tB+\n\x11qm.grpc.qmManagerB\x0eQmManagerProtoP\x01\xa2\x02\x03HLWb\x06proto3'
  ,
  dependencies=[qm_dot_pb_dot_inc__qua__config__pb2.DESCRIPTOR,qm_dot_pb_dot_general__messages__pb2.DESCRIPTOR,])




_OPENQUANTUMMACHINEREQUEST = _descriptor.Descriptor(
  name='OpenQuantumMachineRequest',
  full_name='qm.grpc.qm_manager.OpenQuantumMachineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='qm.grpc.qm_manager.OpenQuantumMachineRequest.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='never', full_name='qm.grpc.qm_manager.OpenQuantumMachineRequest.never', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='always', full_name='qm.grpc.qm_manager.OpenQuantumMachineRequest.always', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifNeeded', full_name='qm.grpc.qm_manager.OpenQuantumMachineRequest.ifNeeded', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='oneOfCloseOtherMachines', full_name='qm.grpc.qm_manager.OpenQuantumMachineRequest.oneOfCloseOtherMachines',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=105,
  serialized_end=261,
)


_OPENQUANTUMMACHINERESPONSE = _descriptor.Descriptor(
  name='OpenQuantumMachineResponse',
  full_name='qm.grpc.qm_manager.OpenQuantumMachineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='qm.grpc.qm_manager.OpenQuantumMachineResponse.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='qm.grpc.qm_manager.OpenQuantumMachineResponse.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configValidationErrors', full_name='qm.grpc.qm_manager.OpenQuantumMachineResponse.configValidationErrors', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='physicalValidationErrors', full_name='qm.grpc.qm_manager.OpenQuantumMachineResponse.physicalValidationErrors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='openQmWarnings', full_name='qm.grpc.qm_manager.OpenQuantumMachineResponse.openQmWarnings', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=545,
)


_CLOSEQUANTUMMACHINEREQUEST = _descriptor.Descriptor(
  name='CloseQuantumMachineRequest',
  full_name='qm.grpc.qm_manager.CloseQuantumMachineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='qm.grpc.qm_manager.CloseQuantumMachineRequest.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=594,
)


_CLOSEQUANTUMMACHINERESPONSE = _descriptor.Descriptor(
  name='CloseQuantumMachineResponse',
  full_name='qm.grpc.qm_manager.CloseQuantumMachineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='qm.grpc.qm_manager.CloseQuantumMachineResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='qm.grpc.qm_manager.CloseQuantumMachineResponse.errors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=596,
  serialized_end=698,
)


_GETQUANTUMMACHINEREQUEST = _descriptor.Descriptor(
  name='GetQuantumMachineRequest',
  full_name='qm.grpc.qm_manager.GetQuantumMachineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='qm.grpc.qm_manager.GetQuantumMachineRequest.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=745,
)


_GETQUANTUMMACHINERESPONSE = _descriptor.Descriptor(
  name='GetQuantumMachineResponse',
  full_name='qm.grpc.qm_manager.GetQuantumMachineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='qm.grpc.qm_manager.GetQuantumMachineResponse.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='qm.grpc.qm_manager.GetQuantumMachineResponse.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='qm.grpc.qm_manager.GetQuantumMachineResponse.success', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='qm.grpc.qm_manager.GetQuantumMachineResponse.errors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=748,
  serialized_end=914,
)


_GETRUNNINGJOBREQUEST = _descriptor.Descriptor(
  name='GetRunningJobRequest',
  full_name='qm.grpc.qm_manager.GetRunningJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='qm.grpc.qm_manager.GetRunningJobRequest.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=916,
  serialized_end=957,
)


_GETRUNNINGJOBRESPONSE = _descriptor.Descriptor(
  name='GetRunningJobResponse',
  full_name='qm.grpc.qm_manager.GetRunningJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='qm.grpc.qm_manager.GetRunningJobResponse.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jobId', full_name='qm.grpc.qm_manager.GetRunningJobResponse.jobId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=959,
  serialized_end=1016,
)


_LISTOPENQUANTUMMACHINESRESPONSE = _descriptor.Descriptor(
  name='ListOpenQuantumMachinesResponse',
  full_name='qm.grpc.qm_manager.ListOpenQuantumMachinesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineIDs', full_name='qm.grpc.qm_manager.ListOpenQuantumMachinesResponse.machineIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1018,
  serialized_end=1071,
)


_CLOSEALLQUANTUMMACHINESRESPONSE = _descriptor.Descriptor(
  name='CloseAllQuantumMachinesResponse',
  full_name='qm.grpc.qm_manager.CloseAllQuantumMachinesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='qm.grpc.qm_manager.CloseAllQuantumMachinesResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='qm.grpc.qm_manager.CloseAllQuantumMachinesResponse.errors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1073,
  serialized_end=1179,
)


_GETCONTROLLERSRESPONSE = _descriptor.Descriptor(
  name='GetControllersResponse',
  full_name='qm.grpc.qm_manager.GetControllersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='controllers', full_name='qm.grpc.qm_manager.GetControllersResponse.controllers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1181,
  serialized_end=1258,
)


_CONTROLLER = _descriptor.Descriptor(
  name='Controller',
  full_name='qm.grpc.qm_manager.Controller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='qm.grpc.qm_manager.Controller.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1260,
  serialized_end=1286,
)


_CONFIGVALIDATIONMESSAGE = _descriptor.Descriptor(
  name='ConfigValidationMessage',
  full_name='qm.grpc.qm_manager.ConfigValidationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='qm.grpc.qm_manager.ConfigValidationMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='qm.grpc.qm_manager.ConfigValidationMessage.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='qm.grpc.qm_manager.ConfigValidationMessage.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='qm.grpc.qm_manager.ConfigValidationMessage.level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1414,
)


_PHYSICALVALIDATIONMESSAGE = _descriptor.Descriptor(
  name='PhysicalValidationMessage',
  full_name='qm.grpc.qm_manager.PhysicalValidationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='qm.grpc.qm_manager.PhysicalValidationMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='qm.grpc.qm_manager.PhysicalValidationMessage.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='qm.grpc.qm_manager.PhysicalValidationMessage.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='qm.grpc.qm_manager.PhysicalValidationMessage.level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1417,
  serialized_end=1545,
)


_OPENQMWARNING = _descriptor.Descriptor(
  name='OpenQmWarning',
  full_name='qm.grpc.qm_manager.OpenQmWarning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='qm.grpc.qm_manager.OpenQmWarning.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='qm.grpc.qm_manager.OpenQmWarning.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1547,
  serialized_end=1593,
)

_OPENQUANTUMMACHINEREQUEST.fields_by_name['config'].message_type = qm_dot_pb_dot_inc__qua__config__pb2._QUACONFIG
_OPENQUANTUMMACHINEREQUEST.oneofs_by_name['oneOfCloseOtherMachines'].fields.append(
  _OPENQUANTUMMACHINEREQUEST.fields_by_name['never'])
_OPENQUANTUMMACHINEREQUEST.fields_by_name['never'].containing_oneof = _OPENQUANTUMMACHINEREQUEST.oneofs_by_name['oneOfCloseOtherMachines']
_OPENQUANTUMMACHINEREQUEST.oneofs_by_name['oneOfCloseOtherMachines'].fields.append(
  _OPENQUANTUMMACHINEREQUEST.fields_by_name['always'])
_OPENQUANTUMMACHINEREQUEST.fields_by_name['always'].containing_oneof = _OPENQUANTUMMACHINEREQUEST.oneofs_by_name['oneOfCloseOtherMachines']
_OPENQUANTUMMACHINEREQUEST.oneofs_by_name['oneOfCloseOtherMachines'].fields.append(
  _OPENQUANTUMMACHINEREQUEST.fields_by_name['ifNeeded'])
_OPENQUANTUMMACHINEREQUEST.fields_by_name['ifNeeded'].containing_oneof = _OPENQUANTUMMACHINEREQUEST.oneofs_by_name['oneOfCloseOtherMachines']
_OPENQUANTUMMACHINERESPONSE.fields_by_name['configValidationErrors'].message_type = _CONFIGVALIDATIONMESSAGE
_OPENQUANTUMMACHINERESPONSE.fields_by_name['physicalValidationErrors'].message_type = _PHYSICALVALIDATIONMESSAGE
_OPENQUANTUMMACHINERESPONSE.fields_by_name['openQmWarnings'].message_type = _OPENQMWARNING
_CLOSEQUANTUMMACHINERESPONSE.fields_by_name['errors'].message_type = qm_dot_pb_dot_general__messages__pb2._ERRORMESSAGE
_GETQUANTUMMACHINERESPONSE.fields_by_name['config'].message_type = qm_dot_pb_dot_inc__qua__config__pb2._QUACONFIG
_GETQUANTUMMACHINERESPONSE.fields_by_name['errors'].message_type = qm_dot_pb_dot_general__messages__pb2._ERRORMESSAGE
_CLOSEALLQUANTUMMACHINESRESPONSE.fields_by_name['errors'].message_type = qm_dot_pb_dot_general__messages__pb2._ERRORMESSAGE
_GETCONTROLLERSRESPONSE.fields_by_name['controllers'].message_type = _CONTROLLER
_CONFIGVALIDATIONMESSAGE.fields_by_name['level'].enum_type = qm_dot_pb_dot_general__messages__pb2._MESSAGELEVEL
_PHYSICALVALIDATIONMESSAGE.fields_by_name['level'].enum_type = qm_dot_pb_dot_general__messages__pb2._MESSAGELEVEL
DESCRIPTOR.message_types_by_name['OpenQuantumMachineRequest'] = _OPENQUANTUMMACHINEREQUEST
DESCRIPTOR.message_types_by_name['OpenQuantumMachineResponse'] = _OPENQUANTUMMACHINERESPONSE
DESCRIPTOR.message_types_by_name['CloseQuantumMachineRequest'] = _CLOSEQUANTUMMACHINEREQUEST
DESCRIPTOR.message_types_by_name['CloseQuantumMachineResponse'] = _CLOSEQUANTUMMACHINERESPONSE
DESCRIPTOR.message_types_by_name['GetQuantumMachineRequest'] = _GETQUANTUMMACHINEREQUEST
DESCRIPTOR.message_types_by_name['GetQuantumMachineResponse'] = _GETQUANTUMMACHINERESPONSE
DESCRIPTOR.message_types_by_name['GetRunningJobRequest'] = _GETRUNNINGJOBREQUEST
DESCRIPTOR.message_types_by_name['GetRunningJobResponse'] = _GETRUNNINGJOBRESPONSE
DESCRIPTOR.message_types_by_name['ListOpenQuantumMachinesResponse'] = _LISTOPENQUANTUMMACHINESRESPONSE
DESCRIPTOR.message_types_by_name['CloseAllQuantumMachinesResponse'] = _CLOSEALLQUANTUMMACHINESRESPONSE
DESCRIPTOR.message_types_by_name['GetControllersResponse'] = _GETCONTROLLERSRESPONSE
DESCRIPTOR.message_types_by_name['Controller'] = _CONTROLLER
DESCRIPTOR.message_types_by_name['ConfigValidationMessage'] = _CONFIGVALIDATIONMESSAGE
DESCRIPTOR.message_types_by_name['PhysicalValidationMessage'] = _PHYSICALVALIDATIONMESSAGE
DESCRIPTOR.message_types_by_name['OpenQmWarning'] = _OPENQMWARNING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenQuantumMachineRequest = _reflection.GeneratedProtocolMessageType('OpenQuantumMachineRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENQUANTUMMACHINEREQUEST,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.OpenQuantumMachineRequest)
  })
_sym_db.RegisterMessage(OpenQuantumMachineRequest)

OpenQuantumMachineResponse = _reflection.GeneratedProtocolMessageType('OpenQuantumMachineResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENQUANTUMMACHINERESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.OpenQuantumMachineResponse)
  })
_sym_db.RegisterMessage(OpenQuantumMachineResponse)

CloseQuantumMachineRequest = _reflection.GeneratedProtocolMessageType('CloseQuantumMachineRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEQUANTUMMACHINEREQUEST,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.CloseQuantumMachineRequest)
  })
_sym_db.RegisterMessage(CloseQuantumMachineRequest)

CloseQuantumMachineResponse = _reflection.GeneratedProtocolMessageType('CloseQuantumMachineResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEQUANTUMMACHINERESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.CloseQuantumMachineResponse)
  })
_sym_db.RegisterMessage(CloseQuantumMachineResponse)

GetQuantumMachineRequest = _reflection.GeneratedProtocolMessageType('GetQuantumMachineRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETQUANTUMMACHINEREQUEST,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.GetQuantumMachineRequest)
  })
_sym_db.RegisterMessage(GetQuantumMachineRequest)

GetQuantumMachineResponse = _reflection.GeneratedProtocolMessageType('GetQuantumMachineResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETQUANTUMMACHINERESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.GetQuantumMachineResponse)
  })
_sym_db.RegisterMessage(GetQuantumMachineResponse)

GetRunningJobRequest = _reflection.GeneratedProtocolMessageType('GetRunningJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNNINGJOBREQUEST,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.GetRunningJobRequest)
  })
_sym_db.RegisterMessage(GetRunningJobRequest)

GetRunningJobResponse = _reflection.GeneratedProtocolMessageType('GetRunningJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNNINGJOBRESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.GetRunningJobResponse)
  })
_sym_db.RegisterMessage(GetRunningJobResponse)

ListOpenQuantumMachinesResponse = _reflection.GeneratedProtocolMessageType('ListOpenQuantumMachinesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPENQUANTUMMACHINESRESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.ListOpenQuantumMachinesResponse)
  })
_sym_db.RegisterMessage(ListOpenQuantumMachinesResponse)

CloseAllQuantumMachinesResponse = _reflection.GeneratedProtocolMessageType('CloseAllQuantumMachinesResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEALLQUANTUMMACHINESRESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.CloseAllQuantumMachinesResponse)
  })
_sym_db.RegisterMessage(CloseAllQuantumMachinesResponse)

GetControllersResponse = _reflection.GeneratedProtocolMessageType('GetControllersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCONTROLLERSRESPONSE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.GetControllersResponse)
  })
_sym_db.RegisterMessage(GetControllersResponse)

Controller = _reflection.GeneratedProtocolMessageType('Controller', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLLER,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.Controller)
  })
_sym_db.RegisterMessage(Controller)

ConfigValidationMessage = _reflection.GeneratedProtocolMessageType('ConfigValidationMessage', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGVALIDATIONMESSAGE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.ConfigValidationMessage)
  })
_sym_db.RegisterMessage(ConfigValidationMessage)

PhysicalValidationMessage = _reflection.GeneratedProtocolMessageType('PhysicalValidationMessage', (_message.Message,), {
  'DESCRIPTOR' : _PHYSICALVALIDATIONMESSAGE,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.PhysicalValidationMessage)
  })
_sym_db.RegisterMessage(PhysicalValidationMessage)

OpenQmWarning = _reflection.GeneratedProtocolMessageType('OpenQmWarning', (_message.Message,), {
  'DESCRIPTOR' : _OPENQMWARNING,
  '__module__' : 'qm.pb.qm_manager_pb2'
  # @@protoc_insertion_point(class_scope:qm.grpc.qm_manager.OpenQmWarning)
  })
_sym_db.RegisterMessage(OpenQmWarning)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
