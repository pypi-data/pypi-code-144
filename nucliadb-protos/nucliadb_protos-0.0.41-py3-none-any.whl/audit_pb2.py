# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/audit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nucliadb_protos import nodereader_pb2 as nucliadb__protos_dot_nodereader__pb2
try:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_noderesources__pb2
except AttributeError:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.noderesources_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.utils_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.utils_pb2
from nucliadb_protos import resources_pb2 as nucliadb__protos_dot_resources__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_resources__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_resources__pb2.nucliadb_protos.utils_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bnucliadb_protos/audit.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a nucliadb_protos/nodereader.proto\x1a\x1fnucliadb_protos/resources.proto\"\xda\x01\n\nAuditField\x12\'\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x17.AuditField.FieldAction\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x12\n\nsize_delta\x18\x03 \x01(\x05\x12\x10\n\x08\x66ield_id\x18\x04 \x01(\t\x12(\n\nfield_type\x18\x05 \x01(\x0e\x32\x14.resources.FieldType\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\"3\n\x0b\x46ieldAction\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\"\xd9\x03\n\x0c\x41uditRequest\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.AuditRequest.AuditType\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12\x0e\n\x06userid\x18\x04 \x01(\t\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ields\x18\x06 \x03(\t\x12)\n\x06search\x18\x07 \x01(\x0b\x32\x19.nodereader.SearchRequest\x12\x0e\n\x06timeit\x18\x08 \x01(\x02\x12\x0e\n\x06origin\x18\t \x01(\t\x12\x0b\n\x03rid\x18\n \x01(\t\x12\x0c\n\x04task\x18\x0b \x01(\t\x12\x11\n\tresources\x18\x0c \x01(\x05\x12*\n\x0e\x66ield_metadata\x18\r \x03(\x0b\x32\x12.resources.FieldID\x12!\n\x0c\x66ields_audit\x18\x0e \x03(\x0b\x32\x0b.AuditField\"\x81\x01\n\tAuditType\x12\x0b\n\x07VISITED\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x07\n\x03NEW\x10\x03\x12\x0b\n\x07STARTED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\n\n\x06SEARCH\x10\x06\x12\r\n\tPROCESSED\x10\x07\x12\x0e\n\nKB_DELETED\x10\x08\x62\x06proto3')



_AUDITFIELD = DESCRIPTOR.message_types_by_name['AuditField']
_AUDITREQUEST = DESCRIPTOR.message_types_by_name['AuditRequest']
_AUDITFIELD_FIELDACTION = _AUDITFIELD.enum_types_by_name['FieldAction']
_AUDITREQUEST_AUDITTYPE = _AUDITREQUEST.enum_types_by_name['AuditType']
AuditField = _reflection.GeneratedProtocolMessageType('AuditField', (_message.Message,), {
  'DESCRIPTOR' : _AUDITFIELD,
  '__module__' : 'nucliadb_protos.audit_pb2'
  # @@protoc_insertion_point(class_scope:AuditField)
  })
_sym_db.RegisterMessage(AuditField)

AuditRequest = _reflection.GeneratedProtocolMessageType('AuditRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUDITREQUEST,
  '__module__' : 'nucliadb_protos.audit_pb2'
  # @@protoc_insertion_point(class_scope:AuditRequest)
  })
_sym_db.RegisterMessage(AuditRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUDITFIELD._serialized_start=132
  _AUDITFIELD._serialized_end=350
  _AUDITFIELD_FIELDACTION._serialized_start=299
  _AUDITFIELD_FIELDACTION._serialized_end=350
  _AUDITREQUEST._serialized_start=353
  _AUDITREQUEST._serialized_end=826
  _AUDITREQUEST_AUDITTYPE._serialized_start=697
  _AUDITREQUEST_AUDITTYPE._serialized_end=826
# @@protoc_insertion_point(module_scope)
