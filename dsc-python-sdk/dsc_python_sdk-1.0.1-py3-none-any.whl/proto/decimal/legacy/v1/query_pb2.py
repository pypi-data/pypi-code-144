# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: decimal/legacy/v1/query.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from decimal.legacy.v1 import legacy_pb2 as decimal_dot_legacy_dot_v1_dot_legacy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='decimal/legacy/v1/query.proto',
  package='decimal.legacy.v1',
  syntax='proto3',
  serialized_options=b'\n\025com.decimal.legacy.v1B\nQueryProtoP\001Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\242\002\003DLX\252\002\021Decimal.Legacy.V1\312\002\021Decimal\\Legacy\\V1\342\002\035Decimal\\Legacy\\V1\\GPBMetadata\352\002\023Decimal::Legacy::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x64\x65\x63imal/legacy/v1/query.proto\x12\x11\x64\x65\x63imal.legacy.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x64\x65\x63imal/legacy/v1/legacy.proto\"]\n\x13QueryRecordsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x9a\x01\n\x14QueryRecordsResponse\x12\x39\n\x07records\x18\x01 \x03(\x0b\x32\x19.decimal.legacy.v1.RecordB\x04\xc8\xde\x1f\x00R\x07records\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"U\n\x12QueryRecordRequest\x12?\n\x0elegacy_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\rlegacyAddress\"N\n\x13QueryRecordResponse\x12\x37\n\x06record\x18\x01 \x01(\x0b\x32\x19.decimal.legacy.v1.RecordB\x04\xc8\xde\x1f\x00R\x06record\"+\n\x11QueryCheckRequest\x12\x16\n\x06pubkey\x18\x01 \x01(\x0cR\x06pubkey\"M\n\x12QueryCheckResponse\x12\x37\n\x06record\x18\x01 \x01(\x0b\x32\x19.decimal.legacy.v1.RecordB\x04\xc8\xde\x1f\x00R\x06record2\xfe\x02\n\x05Query\x12v\n\x07Records\x12&.decimal.legacy.v1.QueryRecordsRequest\x1a\'.decimal.legacy.v1.QueryRecordsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/legacy/v1/records\x12\x83\x01\n\x06Record\x12%.decimal.legacy.v1.QueryRecordRequest\x1a&.decimal.legacy.v1.QueryRecordResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/legacy/v1/record/{legacy_address}\x12w\n\x05\x43heck\x12$.decimal.legacy.v1.QueryCheckRequest\x1a%.decimal.legacy.v1.QueryCheckResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/legacy/v1/check/{pubkey}B\xc1\x01\n\x15\x63om.decimal.legacy.v1B\nQueryProtoP\x01Z6bitbucket.org/decimalteam/go-smart-node/x/legacy/types\xa2\x02\x03\x44LX\xaa\x02\x11\x44\x65\x63imal.Legacy.V1\xca\x02\x11\x44\x65\x63imal\\Legacy\\V1\xe2\x02\x1d\x44\x65\x63imal\\Legacy\\V1\\GPBMetadata\xea\x02\x13\x44\x65\x63imal::Legacy::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,decimal_dot_legacy_dot_v1_dot_legacy__pb2.DESCRIPTOR,])




_QUERYRECORDSREQUEST = _descriptor.Descriptor(
  name='QueryRecordsRequest',
  full_name='decimal.legacy.v1.QueryRecordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='decimal.legacy.v1.QueryRecordsRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=207,
  serialized_end=300,
)


_QUERYRECORDSRESPONSE = _descriptor.Descriptor(
  name='QueryRecordsResponse',
  full_name='decimal.legacy.v1.QueryRecordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='decimal.legacy.v1.QueryRecordsResponse.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='records', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='decimal.legacy.v1.QueryRecordsResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pagination', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=303,
  serialized_end=457,
)


_QUERYRECORDREQUEST = _descriptor.Descriptor(
  name='QueryRecordRequest',
  full_name='decimal.legacy.v1.QueryRecordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='legacy_address', full_name='decimal.legacy.v1.QueryRecordRequest.legacy_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', json_name='legacyAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=459,
  serialized_end=544,
)


_QUERYRECORDRESPONSE = _descriptor.Descriptor(
  name='QueryRecordResponse',
  full_name='decimal.legacy.v1.QueryRecordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='decimal.legacy.v1.QueryRecordResponse.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='record', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=546,
  serialized_end=624,
)


_QUERYCHECKREQUEST = _descriptor.Descriptor(
  name='QueryCheckRequest',
  full_name='decimal.legacy.v1.QueryCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='decimal.legacy.v1.QueryCheckRequest.pubkey', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pubkey', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=626,
  serialized_end=669,
)


_QUERYCHECKRESPONSE = _descriptor.Descriptor(
  name='QueryCheckResponse',
  full_name='decimal.legacy.v1.QueryCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='decimal.legacy.v1.QueryCheckResponse.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', json_name='record', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=671,
  serialized_end=748,
)

_QUERYRECORDSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYRECORDSRESPONSE.fields_by_name['records'].message_type = decimal_dot_legacy_dot_v1_dot_legacy__pb2._RECORD
_QUERYRECORDSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYRECORDRESPONSE.fields_by_name['record'].message_type = decimal_dot_legacy_dot_v1_dot_legacy__pb2._RECORD
_QUERYCHECKRESPONSE.fields_by_name['record'].message_type = decimal_dot_legacy_dot_v1_dot_legacy__pb2._RECORD
DESCRIPTOR.message_types_by_name['QueryRecordsRequest'] = _QUERYRECORDSREQUEST
DESCRIPTOR.message_types_by_name['QueryRecordsResponse'] = _QUERYRECORDSRESPONSE
DESCRIPTOR.message_types_by_name['QueryRecordRequest'] = _QUERYRECORDREQUEST
DESCRIPTOR.message_types_by_name['QueryRecordResponse'] = _QUERYRECORDRESPONSE
DESCRIPTOR.message_types_by_name['QueryCheckRequest'] = _QUERYCHECKREQUEST
DESCRIPTOR.message_types_by_name['QueryCheckResponse'] = _QUERYCHECKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryRecordsRequest = _reflection.GeneratedProtocolMessageType('QueryRecordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRECORDSREQUEST,
  '__module__' : 'decimal.legacy.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.QueryRecordsRequest)
  })
_sym_db.RegisterMessage(QueryRecordsRequest)

QueryRecordsResponse = _reflection.GeneratedProtocolMessageType('QueryRecordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRECORDSRESPONSE,
  '__module__' : 'decimal.legacy.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.QueryRecordsResponse)
  })
_sym_db.RegisterMessage(QueryRecordsResponse)

QueryRecordRequest = _reflection.GeneratedProtocolMessageType('QueryRecordRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRECORDREQUEST,
  '__module__' : 'decimal.legacy.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.QueryRecordRequest)
  })
_sym_db.RegisterMessage(QueryRecordRequest)

QueryRecordResponse = _reflection.GeneratedProtocolMessageType('QueryRecordResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRECORDRESPONSE,
  '__module__' : 'decimal.legacy.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.QueryRecordResponse)
  })
_sym_db.RegisterMessage(QueryRecordResponse)

QueryCheckRequest = _reflection.GeneratedProtocolMessageType('QueryCheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCHECKREQUEST,
  '__module__' : 'decimal.legacy.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.QueryCheckRequest)
  })
_sym_db.RegisterMessage(QueryCheckRequest)

QueryCheckResponse = _reflection.GeneratedProtocolMessageType('QueryCheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCHECKRESPONSE,
  '__module__' : 'decimal.legacy.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:decimal.legacy.v1.QueryCheckResponse)
  })
_sym_db.RegisterMessage(QueryCheckResponse)


DESCRIPTOR._options = None
_QUERYRECORDSRESPONSE.fields_by_name['records']._options = None
_QUERYRECORDREQUEST.fields_by_name['legacy_address']._options = None
_QUERYRECORDRESPONSE.fields_by_name['record']._options = None
_QUERYCHECKRESPONSE.fields_by_name['record']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='decimal.legacy.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=751,
  serialized_end=1133,
  methods=[
  _descriptor.MethodDescriptor(
    name='Records',
    full_name='decimal.legacy.v1.Query.Records',
    index=0,
    containing_service=None,
    input_type=_QUERYRECORDSREQUEST,
    output_type=_QUERYRECORDSRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/legacy/v1/records',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Record',
    full_name='decimal.legacy.v1.Query.Record',
    index=1,
    containing_service=None,
    input_type=_QUERYRECORDREQUEST,
    output_type=_QUERYRECORDRESPONSE,
    serialized_options=b'\202\323\344\223\002$\022\"/legacy/v1/record/{legacy_address}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Check',
    full_name='decimal.legacy.v1.Query.Check',
    index=2,
    containing_service=None,
    input_type=_QUERYCHECKREQUEST,
    output_type=_QUERYCHECKRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/legacy/v1/check/{pubkey}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
