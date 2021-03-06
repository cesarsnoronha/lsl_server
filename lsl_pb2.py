# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lsl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lsl.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tlsl.proto\"#\n\nLSLRequest\x12\x15\n\x05state\x18\x01 \x01(\x0e\x32\x06.State\".\n\x0bLSLResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t*D\n\x05State\x12\t\n\x05START\x10\x00\x12\x11\n\rSENTENCE_SHOW\x10\x01\x12\x11\n\rQUESTION_SHOW\x10\x02\x12\n\n\x06\x41NSWER\x10\x03\x32\x36\n\nLSLMessage\x12(\n\x0bSendMessage\x12\x0b.LSLRequest\x1a\x0c.LSLResponseb\x06proto3'
)

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENTENCE_SHOW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUESTION_SHOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANSWER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=98,
  serialized_end=166,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
START = 0
SENTENCE_SHOW = 1
QUESTION_SHOW = 2
ANSWER = 3



_LSLREQUEST = _descriptor.Descriptor(
  name='LSLRequest',
  full_name='LSLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='LSLRequest.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=13,
  serialized_end=48,
)


_LSLRESPONSE = _descriptor.Descriptor(
  name='LSLResponse',
  full_name='LSLResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LSLResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='LSLResponse.description', index=1,
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
  serialized_start=50,
  serialized_end=96,
)

_LSLREQUEST.fields_by_name['state'].enum_type = _STATE
DESCRIPTOR.message_types_by_name['LSLRequest'] = _LSLREQUEST
DESCRIPTOR.message_types_by_name['LSLResponse'] = _LSLRESPONSE
DESCRIPTOR.enum_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LSLRequest = _reflection.GeneratedProtocolMessageType('LSLRequest', (_message.Message,), {
  'DESCRIPTOR' : _LSLREQUEST,
  '__module__' : 'lsl_pb2'
  # @@protoc_insertion_point(class_scope:LSLRequest)
  })
_sym_db.RegisterMessage(LSLRequest)

LSLResponse = _reflection.GeneratedProtocolMessageType('LSLResponse', (_message.Message,), {
  'DESCRIPTOR' : _LSLRESPONSE,
  '__module__' : 'lsl_pb2'
  # @@protoc_insertion_point(class_scope:LSLResponse)
  })
_sym_db.RegisterMessage(LSLResponse)



_LSLMESSAGE = _descriptor.ServiceDescriptor(
  name='LSLMessage',
  full_name='LSLMessage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=168,
  serialized_end=222,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='LSLMessage.SendMessage',
    index=0,
    containing_service=None,
    input_type=_LSLREQUEST,
    output_type=_LSLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LSLMESSAGE)

DESCRIPTOR.services_by_name['LSLMessage'] = _LSLMESSAGE

# @@protoc_insertion_point(module_scope)
