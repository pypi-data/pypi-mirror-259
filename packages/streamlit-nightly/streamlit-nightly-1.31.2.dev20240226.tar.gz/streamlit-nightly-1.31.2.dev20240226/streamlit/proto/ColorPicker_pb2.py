# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/ColorPicker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import LabelVisibilityMessage_pb2 as streamlit_dot_proto_dot_LabelVisibilityMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!streamlit/proto/ColorPicker.proto\x1a,streamlit/proto/LabelVisibilityMessage.proto\"\xbf\x01\n\x0b\x43olorPicker\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x0c\n\x04help\x18\x04 \x01(\t\x12\x0f\n\x07\x66orm_id\x18\x05 \x01(\t\x12\r\n\x05value\x18\x06 \x01(\t\x12\x11\n\tset_value\x18\x07 \x01(\x08\x12\x10\n\x08\x64isabled\x18\x08 \x01(\x08\x12\x31\n\x10label_visibility\x18\t \x01(\x0b\x32\x17.LabelVisibilityMessageB0\n\x1c\x63om.snowflake.apps.streamlitB\x10\x43olorPickerProtob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.ColorPicker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.snowflake.apps.streamlitB\020ColorPickerProto'
  _COLORPICKER._serialized_start=84
  _COLORPICKER._serialized_end=275
# @@protoc_insertion_point(module_scope)
