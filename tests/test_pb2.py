# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='protobuf_json_test',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\x12\x12protobuf_json_test\"\xfc\x02\n\x0bTestMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x13\n\x05query\x18\x02 \x01(\t:\x04test\x12\x0c\n\x04\x66lag\x18\x03 \x01(\x08\x12?\n\ttest_enum\x18\x04 \x01(\x0e\x32(.protobuf_json_test.TestMessage.TestEnum:\x02V1\x12=\n\nnested_msg\x18\x05 \x02(\x0b\x32).protobuf_json_test.TestMessage.NestedMsg\x12>\n\x0bnested_msgs\x18\x06 \x03(\x0b\x32).protobuf_json_test.TestMessage.NestedMsg\x12\x0f\n\x07rep_int\x18\x07 \x03(\x05\x12\t\n\x01\x62\x18\x08 \x01(\x0c\x12\n\n\x02\x62s\x18\t \x03(\x0c\x1a\x33\n\tNestedMsg\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"\x1a\n\x08TestEnum\x12\x06\n\x02V1\x10\x01\x12\x06\n\x02V2\x10\x02*\x05\x08\x64\x10\xc8\x01:8\n\x05query\x12\x1f.protobuf_json_test.TestMessage\x18\x64 \x01(\t:\x08test ext:-\n\x04long\x12\x1f.protobuf_json_test.TestMessage\x18\x65 \x01(\x04'
)


QUERY_FIELD_NUMBER = 100
query = _descriptor.FieldDescriptor(
  name='query', full_name='protobuf_json_test.query', index=0,
  number=100, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=b"test ext".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
LONG_FIELD_NUMBER = 101
long = _descriptor.FieldDescriptor(
  name='long', full_name='protobuf_json_test.long', index=1,
  number=101, type=4, cpp_type=4, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

_TESTMESSAGE_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='protobuf_json_test.TestMessage.TestEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V1', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V2', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=382,
  serialized_end=408,
)
_sym_db.RegisterEnumDescriptor(_TESTMESSAGE_TESTENUM)


_TESTMESSAGE_NESTEDMSG = _descriptor.Descriptor(
  name='NestedMsg',
  full_name='protobuf_json_test.TestMessage.NestedMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf_json_test.TestMessage.NestedMsg.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='protobuf_json_test.TestMessage.NestedMsg.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='protobuf_json_test.TestMessage.NestedMsg.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=380,
)

_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='protobuf_json_test.TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf_json_test.TestMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='protobuf_json_test.TestMessage.query', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"test".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flag', full_name='protobuf_json_test.TestMessage.flag', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_enum', full_name='protobuf_json_test.TestMessage.test_enum', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_msg', full_name='protobuf_json_test.TestMessage.nested_msg', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_msgs', full_name='protobuf_json_test.TestMessage.nested_msgs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rep_int', full_name='protobuf_json_test.TestMessage.rep_int', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='protobuf_json_test.TestMessage.b', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bs', full_name='protobuf_json_test.TestMessage.bs', index=8,
      number=9, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TESTMESSAGE_NESTEDMSG, ],
  enum_types=[
    _TESTMESSAGE_TESTENUM,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 200), ],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=415,
)

_TESTMESSAGE_NESTEDMSG.containing_type = _TESTMESSAGE
_TESTMESSAGE.fields_by_name['test_enum'].enum_type = _TESTMESSAGE_TESTENUM
_TESTMESSAGE.fields_by_name['nested_msg'].message_type = _TESTMESSAGE_NESTEDMSG
_TESTMESSAGE.fields_by_name['nested_msgs'].message_type = _TESTMESSAGE_NESTEDMSG
_TESTMESSAGE_TESTENUM.containing_type = _TESTMESSAGE
DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE
DESCRIPTOR.extensions_by_name['query'] = query
DESCRIPTOR.extensions_by_name['long'] = long
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), {

  'NestedMsg' : _reflection.GeneratedProtocolMessageType('NestedMsg', (_message.Message,), {
    'DESCRIPTOR' : _TESTMESSAGE_NESTEDMSG,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:protobuf_json_test.TestMessage.NestedMsg)
    })
  ,
  'DESCRIPTOR' : _TESTMESSAGE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_json_test.TestMessage)
  })
_sym_db.RegisterMessage(TestMessage)
_sym_db.RegisterMessage(TestMessage.NestedMsg)

TestMessage.RegisterExtension(query)
TestMessage.RegisterExtension(long)

# @@protoc_insertion_point(module_scope)
