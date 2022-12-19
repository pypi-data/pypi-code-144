# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/noderesources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nucliadb_protos import utils_pb2 as nucliadb__protos_dot_utils__pb2

from nucliadb_protos.utils_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#nucliadb_protos/noderesources.proto\x12\rnoderesources\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bnucliadb_protos/utils.proto\"/\n\x0fTextInformation\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06labels\x18\x02 \x03(\t\"j\n\rIndexMetadata\x12,\n\x08modified\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x15\n\x07ShardId\x12\n\n\x02id\x18\x01 \x01(\t\"/\n\x08ShardIds\x12#\n\x03ids\x18\x01 \x03(\x0b\x32\x16.noderesources.ShardId\"\x85\x04\n\x0cShardCreated\x12\n\n\x02id\x18\x01 \x01(\t\x12\x45\n\x10\x64ocument_service\x18\x02 \x01(\x0e\x32+.noderesources.ShardCreated.DocumentService\x12G\n\x11paragraph_service\x18\x03 \x01(\x0e\x32,.noderesources.ShardCreated.ParagraphService\x12\x41\n\x0evector_service\x18\x04 \x01(\x0e\x32).noderesources.ShardCreated.VectorService\x12\x45\n\x10relation_service\x18\x05 \x01(\x0e\x32+.noderesources.ShardCreated.RelationService\"3\n\x0f\x44ocumentService\x12\x0f\n\x0b\x44OCUMENT_V0\x10\x00\x12\x0f\n\x0b\x44OCUMENT_V1\x10\x01\"6\n\x10ParagraphService\x12\x10\n\x0cPARAGRAPH_V0\x10\x00\x12\x10\n\x0cPARAGRAPH_V1\x10\x01\"-\n\rVectorService\x12\r\n\tVECTOR_V0\x10\x00\x12\r\n\tVECTOR_V1\x10\x01\"3\n\x0fRelationService\x12\x0f\n\x0bRELATION_V0\x10\x00\x12\x0f\n\x0bRELATION_V1\x10\x01\"\xa8\x02\n\x0cShardCleaned\x12\x45\n\x10\x64ocument_service\x18\x02 \x01(\x0e\x32+.noderesources.ShardCreated.DocumentService\x12G\n\x11paragraph_service\x18\x03 \x01(\x0e\x32,.noderesources.ShardCreated.ParagraphService\x12\x41\n\x0evector_service\x18\x04 \x01(\x0e\x32).noderesources.ShardCreated.VectorService\x12\x45\n\x10relation_service\x18\x05 \x01(\x0e\x32+.noderesources.ShardCreated.RelationService\",\n\nResourceID\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"S\n\x05Shard\x12\x10\n\x08shard_id\x18\x01 \x01(\t\x12\x11\n\tresources\x18\x02 \x01(\x04\x12\x12\n\nparagraphs\x18\x03 \x01(\x04\x12\x11\n\tsentences\x18\x04 \x01(\x04\"1\n\tShardList\x12$\n\x06shards\x18\x01 \x03(\x0b\x32\x14.noderesources.Shard\"\x0f\n\rEmptyResponse\"\x0c\n\nEmptyQuery\" \n\x0eVectorSentence\x12\x0e\n\x06vector\x18\x01 \x03(\x02\"\x7f\n\x11ParagraphPosition\x12\r\n\x05index\x18\x01 \x01(\x04\x12\r\n\x05start\x18\x02 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x04\x12\x13\n\x0bpage_number\x18\x04 \x01(\x04\x12\x15\n\rstart_seconds\x18\x05 \x03(\r\x12\x13\n\x0b\x65nd_seconds\x18\x06 \x03(\r\"G\n\x11ParagraphMetadata\x12\x32\n\x08position\x18\x01 \x01(\x0b\x32 .noderesources.ParagraphPosition\"\xca\x02\n\x0eIndexParagraph\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05\x12\x0e\n\x06labels\x18\x03 \x03(\t\x12?\n\tsentences\x18\x04 \x03(\x0b\x32,.noderesources.IndexParagraph.SentencesEntry\x12\r\n\x05\x66ield\x18\x05 \x01(\t\x12\r\n\x05split\x18\x06 \x01(\t\x12\r\n\x05index\x18\x07 \x01(\x04\x12\x19\n\x11repeated_in_field\x18\x08 \x01(\x08\x12\x32\n\x08metadata\x18\t \x01(\x0b\x32 .noderesources.ParagraphMetadata\x1aO\n\x0eSentencesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.noderesources.VectorSentence:\x02\x38\x01\"G\n\x0bVectorSetID\x12%\n\x05shard\x18\x01 \x01(\x0b\x32\x16.noderesources.ShardId\x12\x11\n\tvectorset\x18\x02 \x01(\t\"I\n\rVectorSetList\x12%\n\x05shard\x18\x01 \x01(\x0b\x32\x16.noderesources.ShardId\x12\x11\n\tvectorset\x18\x02 \x03(\t\"\xa7\x01\n\x0fIndexParagraphs\x12\x42\n\nparagraphs\x18\x01 \x03(\x0b\x32..noderesources.IndexParagraphs.ParagraphsEntry\x1aP\n\x0fParagraphsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.noderesources.IndexParagraph:\x02\x38\x01\"\xc3\x07\n\x08Resource\x12+\n\x08resource\x18\x01 \x01(\x0b\x32\x19.noderesources.ResourceID\x12.\n\x08metadata\x18\x02 \x01(\x0b\x32\x1c.noderesources.IndexMetadata\x12\x31\n\x05texts\x18\x03 \x03(\x0b\x32\".noderesources.Resource.TextsEntry\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12\x36\n\x06status\x18\x05 \x01(\x0e\x32&.noderesources.Resource.ResourceStatus\x12;\n\nparagraphs\x18\x06 \x03(\x0b\x32\'.noderesources.Resource.ParagraphsEntry\x12\x1c\n\x14paragraphs_to_delete\x18\x07 \x03(\t\x12\x1b\n\x13sentences_to_delete\x18\x08 \x03(\t\x12\"\n\trelations\x18\t \x03(\x0b\x32\x0f.utils.Relation\x12,\n\x13relations_to_delete\x18\n \x03(\x0b\x32\x0f.utils.Relation\x12\x10\n\x08shard_id\x18\x0b \x01(\t\x12\x35\n\x07vectors\x18\x0c \x03(\x0b\x32$.noderesources.Resource.VectorsEntry\x12G\n\x11vectors_to_delete\x18\r \x03(\x0b\x32,.noderesources.Resource.VectorsToDeleteEntry\x1aL\n\nTextsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.noderesources.TextInformation:\x02\x38\x01\x1aQ\n\x0fParagraphsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.noderesources.IndexParagraphs:\x02\x38\x01\x1a\x42\n\x0cVectorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.utils.UserVectors:\x02\x38\x01\x1aN\n\x14VectorsToDeleteEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.utils.UserVectorsList:\x02\x38\x01\"N\n\x0eResourceStatus\x12\r\n\tPROCESSED\x10\x00\x12\t\n\x05\x45MPTY\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x12\x0b\n\x07PENDING\x10\x04P\x01\x62\x06proto3')



_TEXTINFORMATION = DESCRIPTOR.message_types_by_name['TextInformation']
_INDEXMETADATA = DESCRIPTOR.message_types_by_name['IndexMetadata']
_SHARDID = DESCRIPTOR.message_types_by_name['ShardId']
_SHARDIDS = DESCRIPTOR.message_types_by_name['ShardIds']
_SHARDCREATED = DESCRIPTOR.message_types_by_name['ShardCreated']
_SHARDCLEANED = DESCRIPTOR.message_types_by_name['ShardCleaned']
_RESOURCEID = DESCRIPTOR.message_types_by_name['ResourceID']
_SHARD = DESCRIPTOR.message_types_by_name['Shard']
_SHARDLIST = DESCRIPTOR.message_types_by_name['ShardList']
_EMPTYRESPONSE = DESCRIPTOR.message_types_by_name['EmptyResponse']
_EMPTYQUERY = DESCRIPTOR.message_types_by_name['EmptyQuery']
_VECTORSENTENCE = DESCRIPTOR.message_types_by_name['VectorSentence']
_PARAGRAPHPOSITION = DESCRIPTOR.message_types_by_name['ParagraphPosition']
_PARAGRAPHMETADATA = DESCRIPTOR.message_types_by_name['ParagraphMetadata']
_INDEXPARAGRAPH = DESCRIPTOR.message_types_by_name['IndexParagraph']
_INDEXPARAGRAPH_SENTENCESENTRY = _INDEXPARAGRAPH.nested_types_by_name['SentencesEntry']
_VECTORSETID = DESCRIPTOR.message_types_by_name['VectorSetID']
_VECTORSETLIST = DESCRIPTOR.message_types_by_name['VectorSetList']
_INDEXPARAGRAPHS = DESCRIPTOR.message_types_by_name['IndexParagraphs']
_INDEXPARAGRAPHS_PARAGRAPHSENTRY = _INDEXPARAGRAPHS.nested_types_by_name['ParagraphsEntry']
_RESOURCE = DESCRIPTOR.message_types_by_name['Resource']
_RESOURCE_TEXTSENTRY = _RESOURCE.nested_types_by_name['TextsEntry']
_RESOURCE_PARAGRAPHSENTRY = _RESOURCE.nested_types_by_name['ParagraphsEntry']
_RESOURCE_VECTORSENTRY = _RESOURCE.nested_types_by_name['VectorsEntry']
_RESOURCE_VECTORSTODELETEENTRY = _RESOURCE.nested_types_by_name['VectorsToDeleteEntry']
_SHARDCREATED_DOCUMENTSERVICE = _SHARDCREATED.enum_types_by_name['DocumentService']
_SHARDCREATED_PARAGRAPHSERVICE = _SHARDCREATED.enum_types_by_name['ParagraphService']
_SHARDCREATED_VECTORSERVICE = _SHARDCREATED.enum_types_by_name['VectorService']
_SHARDCREATED_RELATIONSERVICE = _SHARDCREATED.enum_types_by_name['RelationService']
_RESOURCE_RESOURCESTATUS = _RESOURCE.enum_types_by_name['ResourceStatus']
TextInformation = _reflection.GeneratedProtocolMessageType('TextInformation', (_message.Message,), {
  'DESCRIPTOR' : _TEXTINFORMATION,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.TextInformation)
  })
_sym_db.RegisterMessage(TextInformation)

IndexMetadata = _reflection.GeneratedProtocolMessageType('IndexMetadata', (_message.Message,), {
  'DESCRIPTOR' : _INDEXMETADATA,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.IndexMetadata)
  })
_sym_db.RegisterMessage(IndexMetadata)

ShardId = _reflection.GeneratedProtocolMessageType('ShardId', (_message.Message,), {
  'DESCRIPTOR' : _SHARDID,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ShardId)
  })
_sym_db.RegisterMessage(ShardId)

ShardIds = _reflection.GeneratedProtocolMessageType('ShardIds', (_message.Message,), {
  'DESCRIPTOR' : _SHARDIDS,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ShardIds)
  })
_sym_db.RegisterMessage(ShardIds)

ShardCreated = _reflection.GeneratedProtocolMessageType('ShardCreated', (_message.Message,), {
  'DESCRIPTOR' : _SHARDCREATED,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ShardCreated)
  })
_sym_db.RegisterMessage(ShardCreated)

ShardCleaned = _reflection.GeneratedProtocolMessageType('ShardCleaned', (_message.Message,), {
  'DESCRIPTOR' : _SHARDCLEANED,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ShardCleaned)
  })
_sym_db.RegisterMessage(ShardCleaned)

ResourceID = _reflection.GeneratedProtocolMessageType('ResourceID', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEID,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ResourceID)
  })
_sym_db.RegisterMessage(ResourceID)

Shard = _reflection.GeneratedProtocolMessageType('Shard', (_message.Message,), {
  'DESCRIPTOR' : _SHARD,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.Shard)
  })
_sym_db.RegisterMessage(Shard)

ShardList = _reflection.GeneratedProtocolMessageType('ShardList', (_message.Message,), {
  'DESCRIPTOR' : _SHARDLIST,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ShardList)
  })
_sym_db.RegisterMessage(ShardList)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)

EmptyQuery = _reflection.GeneratedProtocolMessageType('EmptyQuery', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYQUERY,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.EmptyQuery)
  })
_sym_db.RegisterMessage(EmptyQuery)

VectorSentence = _reflection.GeneratedProtocolMessageType('VectorSentence', (_message.Message,), {
  'DESCRIPTOR' : _VECTORSENTENCE,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.VectorSentence)
  })
_sym_db.RegisterMessage(VectorSentence)

ParagraphPosition = _reflection.GeneratedProtocolMessageType('ParagraphPosition', (_message.Message,), {
  'DESCRIPTOR' : _PARAGRAPHPOSITION,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ParagraphPosition)
  })
_sym_db.RegisterMessage(ParagraphPosition)

ParagraphMetadata = _reflection.GeneratedProtocolMessageType('ParagraphMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PARAGRAPHMETADATA,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.ParagraphMetadata)
  })
_sym_db.RegisterMessage(ParagraphMetadata)

IndexParagraph = _reflection.GeneratedProtocolMessageType('IndexParagraph', (_message.Message,), {

  'SentencesEntry' : _reflection.GeneratedProtocolMessageType('SentencesEntry', (_message.Message,), {
    'DESCRIPTOR' : _INDEXPARAGRAPH_SENTENCESENTRY,
    '__module__' : 'nucliadb_protos.noderesources_pb2'
    # @@protoc_insertion_point(class_scope:noderesources.IndexParagraph.SentencesEntry)
    })
  ,
  'DESCRIPTOR' : _INDEXPARAGRAPH,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.IndexParagraph)
  })
_sym_db.RegisterMessage(IndexParagraph)
_sym_db.RegisterMessage(IndexParagraph.SentencesEntry)

VectorSetID = _reflection.GeneratedProtocolMessageType('VectorSetID', (_message.Message,), {
  'DESCRIPTOR' : _VECTORSETID,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.VectorSetID)
  })
_sym_db.RegisterMessage(VectorSetID)

VectorSetList = _reflection.GeneratedProtocolMessageType('VectorSetList', (_message.Message,), {
  'DESCRIPTOR' : _VECTORSETLIST,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.VectorSetList)
  })
_sym_db.RegisterMessage(VectorSetList)

IndexParagraphs = _reflection.GeneratedProtocolMessageType('IndexParagraphs', (_message.Message,), {

  'ParagraphsEntry' : _reflection.GeneratedProtocolMessageType('ParagraphsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INDEXPARAGRAPHS_PARAGRAPHSENTRY,
    '__module__' : 'nucliadb_protos.noderesources_pb2'
    # @@protoc_insertion_point(class_scope:noderesources.IndexParagraphs.ParagraphsEntry)
    })
  ,
  'DESCRIPTOR' : _INDEXPARAGRAPHS,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.IndexParagraphs)
  })
_sym_db.RegisterMessage(IndexParagraphs)
_sym_db.RegisterMessage(IndexParagraphs.ParagraphsEntry)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {

  'TextsEntry' : _reflection.GeneratedProtocolMessageType('TextsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESOURCE_TEXTSENTRY,
    '__module__' : 'nucliadb_protos.noderesources_pb2'
    # @@protoc_insertion_point(class_scope:noderesources.Resource.TextsEntry)
    })
  ,

  'ParagraphsEntry' : _reflection.GeneratedProtocolMessageType('ParagraphsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESOURCE_PARAGRAPHSENTRY,
    '__module__' : 'nucliadb_protos.noderesources_pb2'
    # @@protoc_insertion_point(class_scope:noderesources.Resource.ParagraphsEntry)
    })
  ,

  'VectorsEntry' : _reflection.GeneratedProtocolMessageType('VectorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESOURCE_VECTORSENTRY,
    '__module__' : 'nucliadb_protos.noderesources_pb2'
    # @@protoc_insertion_point(class_scope:noderesources.Resource.VectorsEntry)
    })
  ,

  'VectorsToDeleteEntry' : _reflection.GeneratedProtocolMessageType('VectorsToDeleteEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESOURCE_VECTORSTODELETEENTRY,
    '__module__' : 'nucliadb_protos.noderesources_pb2'
    # @@protoc_insertion_point(class_scope:noderesources.Resource.VectorsToDeleteEntry)
    })
  ,
  'DESCRIPTOR' : _RESOURCE,
  '__module__' : 'nucliadb_protos.noderesources_pb2'
  # @@protoc_insertion_point(class_scope:noderesources.Resource)
  })
_sym_db.RegisterMessage(Resource)
_sym_db.RegisterMessage(Resource.TextsEntry)
_sym_db.RegisterMessage(Resource.ParagraphsEntry)
_sym_db.RegisterMessage(Resource.VectorsEntry)
_sym_db.RegisterMessage(Resource.VectorsToDeleteEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INDEXPARAGRAPH_SENTENCESENTRY._options = None
  _INDEXPARAGRAPH_SENTENCESENTRY._serialized_options = b'8\001'
  _INDEXPARAGRAPHS_PARAGRAPHSENTRY._options = None
  _INDEXPARAGRAPHS_PARAGRAPHSENTRY._serialized_options = b'8\001'
  _RESOURCE_TEXTSENTRY._options = None
  _RESOURCE_TEXTSENTRY._serialized_options = b'8\001'
  _RESOURCE_PARAGRAPHSENTRY._options = None
  _RESOURCE_PARAGRAPHSENTRY._serialized_options = b'8\001'
  _RESOURCE_VECTORSENTRY._options = None
  _RESOURCE_VECTORSENTRY._serialized_options = b'8\001'
  _RESOURCE_VECTORSTODELETEENTRY._options = None
  _RESOURCE_VECTORSTODELETEENTRY._serialized_options = b'8\001'
  _TEXTINFORMATION._serialized_start=116
  _TEXTINFORMATION._serialized_end=163
  _INDEXMETADATA._serialized_start=165
  _INDEXMETADATA._serialized_end=271
  _SHARDID._serialized_start=273
  _SHARDID._serialized_end=294
  _SHARDIDS._serialized_start=296
  _SHARDIDS._serialized_end=343
  _SHARDCREATED._serialized_start=346
  _SHARDCREATED._serialized_end=863
  _SHARDCREATED_DOCUMENTSERVICE._serialized_start=656
  _SHARDCREATED_DOCUMENTSERVICE._serialized_end=707
  _SHARDCREATED_PARAGRAPHSERVICE._serialized_start=709
  _SHARDCREATED_PARAGRAPHSERVICE._serialized_end=763
  _SHARDCREATED_VECTORSERVICE._serialized_start=765
  _SHARDCREATED_VECTORSERVICE._serialized_end=810
  _SHARDCREATED_RELATIONSERVICE._serialized_start=812
  _SHARDCREATED_RELATIONSERVICE._serialized_end=863
  _SHARDCLEANED._serialized_start=866
  _SHARDCLEANED._serialized_end=1162
  _RESOURCEID._serialized_start=1164
  _RESOURCEID._serialized_end=1208
  _SHARD._serialized_start=1210
  _SHARD._serialized_end=1293
  _SHARDLIST._serialized_start=1295
  _SHARDLIST._serialized_end=1344
  _EMPTYRESPONSE._serialized_start=1346
  _EMPTYRESPONSE._serialized_end=1361
  _EMPTYQUERY._serialized_start=1363
  _EMPTYQUERY._serialized_end=1375
  _VECTORSENTENCE._serialized_start=1377
  _VECTORSENTENCE._serialized_end=1409
  _PARAGRAPHPOSITION._serialized_start=1411
  _PARAGRAPHPOSITION._serialized_end=1538
  _PARAGRAPHMETADATA._serialized_start=1540
  _PARAGRAPHMETADATA._serialized_end=1611
  _INDEXPARAGRAPH._serialized_start=1614
  _INDEXPARAGRAPH._serialized_end=1944
  _INDEXPARAGRAPH_SENTENCESENTRY._serialized_start=1865
  _INDEXPARAGRAPH_SENTENCESENTRY._serialized_end=1944
  _VECTORSETID._serialized_start=1946
  _VECTORSETID._serialized_end=2017
  _VECTORSETLIST._serialized_start=2019
  _VECTORSETLIST._serialized_end=2092
  _INDEXPARAGRAPHS._serialized_start=2095
  _INDEXPARAGRAPHS._serialized_end=2262
  _INDEXPARAGRAPHS_PARAGRAPHSENTRY._serialized_start=2182
  _INDEXPARAGRAPHS_PARAGRAPHSENTRY._serialized_end=2262
  _RESOURCE._serialized_start=2265
  _RESOURCE._serialized_end=3228
  _RESOURCE_TEXTSENTRY._serialized_start=2841
  _RESOURCE_TEXTSENTRY._serialized_end=2917
  _RESOURCE_PARAGRAPHSENTRY._serialized_start=2919
  _RESOURCE_PARAGRAPHSENTRY._serialized_end=3000
  _RESOURCE_VECTORSENTRY._serialized_start=3002
  _RESOURCE_VECTORSENTRY._serialized_end=3068
  _RESOURCE_VECTORSTODELETEENTRY._serialized_start=3070
  _RESOURCE_VECTORSTODELETEENTRY._serialized_end=3148
  _RESOURCE_RESOURCESTATUS._serialized_start=3150
  _RESOURCE_RESOURCESTATUS._serialized_end=3228
# @@protoc_insertion_point(module_scope)
