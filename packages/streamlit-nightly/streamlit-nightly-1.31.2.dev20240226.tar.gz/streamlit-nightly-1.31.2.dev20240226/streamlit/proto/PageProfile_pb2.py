# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/PageProfile.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!streamlit/proto/PageProfile.proto\"\xc1\x01\n\x0bPageProfile\x12\x1a\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x08.Command\x12\x11\n\texec_time\x18\x02 \x01(\x03\x12\x11\n\tprep_time\x18\x03 \x01(\x03\x12\x0e\n\x06\x63onfig\x18\x05 \x03(\t\x12\x1a\n\x12uncaught_exception\x18\x06 \x01(\t\x12\x14\n\x0c\x61ttributions\x18\x07 \x03(\t\x12\n\n\x02os\x18\x08 \x01(\t\x12\x10\n\x08timezone\x18\t \x01(\t\x12\x10\n\x08headless\x18\n \x01(\x08\"6\n\x08\x41rgument\x12\t\n\x01k\x18\x01 \x01(\t\x12\t\n\x01t\x18\x02 \x01(\t\x12\t\n\x01m\x18\x03 \x01(\t\x12\t\n\x01p\x18\x05 \x01(\x05\">\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\t.Argument\x12\x0c\n\x04time\x18\x04 \x01(\x03\x42\x30\n\x1c\x63om.snowflake.apps.streamlitB\x10PageProfileProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.PageProfile_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.snowflake.apps.streamlitB\020PageProfileProto'
  _PAGEPROFILE._serialized_start=38
  _PAGEPROFILE._serialized_end=231
  _ARGUMENT._serialized_start=233
  _ARGUMENT._serialized_end=287
  _COMMAND._serialized_start=289
  _COMMAND._serialized_end=351
# @@protoc_insertion_point(module_scope)
