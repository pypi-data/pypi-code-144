# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arg_services/mining_explanation/v1/entailment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from arg_services.mining.v1 import entailment_pb2 as arg__services_dot_mining_dot_v1_dot_entailment__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3arg_services/mining_explanation/v1/entailment.proto\x12\"arg_services.mining_explanation.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\'arg_services/mining/v1/entailment.proto\x1a\x1cgoogle/api/annotations.proto\"\xb3\x01\n\x12\x45ntailmentsRequest\x12\x1a\n\x08language\x18\x01 \x01(\tR\x08language\x12P\n\x0b\x65ntailments\x18\x02 \x03(\x0b\x32..arg_services.mining_explanation.v1.EntailmentR\x0b\x65ntailments\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"\x96\x01\n\x13\x45ntailmentsResponse\x12N\n\x07results\x18\x01 \x03(\x0b\x32\x34.arg_services.mining_explanation.v1.EntailmentResultR\x07results\x12/\n\x06\x65xtras\x18\x0f \x01(\x0b\x32\x17.google.protobuf.StructR\x06\x65xtras\"x\n\nEntailment\x12\x18\n\x07premise\x18\x01 \x01(\tR\x07premise\x12\x14\n\x05\x63laim\x18\x02 \x01(\tR\x05\x63laim\x12:\n\x04type\x18\x03 \x01(\x0e\x32&.arg_services.mining.v1.EntailmentTypeR\x04type\"\x91\x02\n\x10\x45ntailmentResult\x12j\n\x0csimilarities\x18\x01 \x03(\x0b\x32\x46.arg_services.mining_explanation.v1.EntailmentResult.SimilaritiesEntryR\x0csimilarities\x12)\n\x10keywords_premise\x18\x02 \x03(\x08R\x0fkeywordsPremise\x12%\n\x0ekeywords_claim\x18\x03 \x03(\x08R\rkeywordsClaim\x1a?\n\x11SimilaritiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01\x32\xce\x01\n\x1c\x45ntailmentExplanationService\x12\xad\x01\n\x0b\x45ntailments\x12\x36.arg_services.mining_explanation.v1.EntailmentsRequest\x1a\x37.arg_services.mining_explanation.v1.EntailmentsResponse\"-\x82\xd3\xe4\x93\x02\':\x01*\"\"/mining_explanation/v1/entailmentsB\xea\x01\n5de.uni_trier.recap.arg_services.mining_explanation.v1B\x0f\x45ntailmentProtoP\x01\xa2\x02\x03\x41MX\xaa\x02 ArgServices.MiningExplanation.V1\xca\x02 ArgServices\\MiningExplanation\\V1\xe2\x02,ArgServices\\MiningExplanation\\V1\\GPBMetadata\xea\x02\"ArgServices::MiningExplanation::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arg_services.mining_explanation.v1.entailment_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n5de.uni_trier.recap.arg_services.mining_explanation.v1B\017EntailmentProtoP\001\242\002\003AMX\252\002 ArgServices.MiningExplanation.V1\312\002 ArgServices\\MiningExplanation\\V1\342\002,ArgServices\\MiningExplanation\\V1\\GPBMetadata\352\002\"ArgServices::MiningExplanation::V1'
  _ENTAILMENTRESULT_SIMILARITIESENTRY._options = None
  _ENTAILMENTRESULT_SIMILARITIESENTRY._serialized_options = b'8\001'
  _ENTAILMENTEXPLANATIONSERVICE.methods_by_name['Entailments']._options = None
  _ENTAILMENTEXPLANATIONSERVICE.methods_by_name['Entailments']._serialized_options = b'\202\323\344\223\002\':\001*\"\"/mining_explanation/v1/entailments'
  _ENTAILMENTSREQUEST._serialized_start=193
  _ENTAILMENTSREQUEST._serialized_end=372
  _ENTAILMENTSRESPONSE._serialized_start=375
  _ENTAILMENTSRESPONSE._serialized_end=525
  _ENTAILMENT._serialized_start=527
  _ENTAILMENT._serialized_end=647
  _ENTAILMENTRESULT._serialized_start=650
  _ENTAILMENTRESULT._serialized_end=923
  _ENTAILMENTRESULT_SIMILARITIESENTRY._serialized_start=860
  _ENTAILMENTRESULT_SIMILARITIESENTRY._serialized_end=923
  _ENTAILMENTEXPLANATIONSERVICE._serialized_start=926
  _ENTAILMENTEXPLANATIONSERVICE._serialized_end=1132
# @@protoc_insertion_point(module_scope)
