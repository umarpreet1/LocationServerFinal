# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serve_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10serve_data.proto\x12\ndataserver\"N\n\rwrite_request\x12\r\n\x05ls_id\x18\x03 \x02(\t\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x12\n\nrequest_id\x18\x04 \x02(\t\">\n\x0clock_request\x12\r\n\x05ls_id\x18\x01 \x02(\t\x12\x0b\n\x03key\x18\x02 \x02(\t\x12\x12\n\nrequest_id\x18\x03 \x02(\t\"\x1b\n\x0cread_request\x12\x0b\n\x03key\x18\x01 \x02(\t\"\x1e\n\rresponse_read\x12\r\n\x05value\x18\x01 \x02(\t\"=\n\x08response\x12\x0e\n\x06status\x18\x01 \x02(\t\x12\x12\n\nrequest_id\x18\x02 \x02(\t\x12\r\n\x05\x64s_id\x18\x03 \x02(\t2\xf7\x01\n\x0b\x64\x61ta_server\x12;\n\x04read\x12\x18.dataserver.read_request\x1a\x19.dataserver.response_read\x12\x38\n\x05write\x12\x19.dataserver.write_request\x1a\x14.dataserver.response\x12\x39\n\x06update\x12\x19.dataserver.write_request\x1a\x14.dataserver.response\x12\x36\n\x04lock\x12\x18.dataserver.lock_request\x1a\x14.dataserver.response')



_WRITE_REQUEST = DESCRIPTOR.message_types_by_name['write_request']
_LOCK_REQUEST = DESCRIPTOR.message_types_by_name['lock_request']
_READ_REQUEST = DESCRIPTOR.message_types_by_name['read_request']
_RESPONSE_READ = DESCRIPTOR.message_types_by_name['response_read']
_RESPONSE = DESCRIPTOR.message_types_by_name['response']
write_request = _reflection.GeneratedProtocolMessageType('write_request', (_message.Message,), {
  'DESCRIPTOR' : _WRITE_REQUEST,
  '__module__' : 'serve_data_pb2'
  # @@protoc_insertion_point(class_scope:dataserver.write_request)
  })
_sym_db.RegisterMessage(write_request)

lock_request = _reflection.GeneratedProtocolMessageType('lock_request', (_message.Message,), {
  'DESCRIPTOR' : _LOCK_REQUEST,
  '__module__' : 'serve_data_pb2'
  # @@protoc_insertion_point(class_scope:dataserver.lock_request)
  })
_sym_db.RegisterMessage(lock_request)

read_request = _reflection.GeneratedProtocolMessageType('read_request', (_message.Message,), {
  'DESCRIPTOR' : _READ_REQUEST,
  '__module__' : 'serve_data_pb2'
  # @@protoc_insertion_point(class_scope:dataserver.read_request)
  })
_sym_db.RegisterMessage(read_request)

response_read = _reflection.GeneratedProtocolMessageType('response_read', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE_READ,
  '__module__' : 'serve_data_pb2'
  # @@protoc_insertion_point(class_scope:dataserver.response_read)
  })
_sym_db.RegisterMessage(response_read)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'serve_data_pb2'
  # @@protoc_insertion_point(class_scope:dataserver.response)
  })
_sym_db.RegisterMessage(response)

_DATA_SERVER = DESCRIPTOR.services_by_name['data_server']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WRITE_REQUEST._serialized_start=32
  _WRITE_REQUEST._serialized_end=110
  _LOCK_REQUEST._serialized_start=112
  _LOCK_REQUEST._serialized_end=174
  _READ_REQUEST._serialized_start=176
  _READ_REQUEST._serialized_end=203
  _RESPONSE_READ._serialized_start=205
  _RESPONSE_READ._serialized_end=235
  _RESPONSE._serialized_start=237
  _RESPONSE._serialized_end=298
  _DATA_SERVER._serialized_start=301
  _DATA_SERVER._serialized_end=548
# @@protoc_insertion_point(module_scope)
