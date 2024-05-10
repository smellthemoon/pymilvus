# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from . import schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tmsg.proto\x12\x10milvus.proto.msg\x1a\x0c\x63ommon.proto\x1a\x0cschema.proto\"\xaa\x03\n\rInsertRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x11\n\tshardName\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x62_name\x18\x03 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x04 \x01(\t\x12\x16\n\x0epartition_name\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x62ID\x18\x06 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x07 \x01(\x03\x12\x13\n\x0bpartitionID\x18\x08 \x01(\x03\x12\x11\n\tsegmentID\x18\t \x01(\x03\x12\x12\n\ntimestamps\x18\n \x03(\x04\x12\x0e\n\x06rowIDs\x18\x0b \x03(\x03\x12+\n\x08row_data\x18\x0c \x03(\x0b\x32\x19.milvus.proto.common.Blob\x12\x33\n\x0b\x66ields_data\x18\r \x03(\x0b\x32\x1e.milvus.proto.schema.FieldData\x12\x10\n\x08num_rows\x18\x0e \x01(\x04\x12\x34\n\x07version\x18\x0f \x01(\x0e\x32#.milvus.proto.msg.InsertDataVersion\"\xbb\x02\n\rDeleteRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x11\n\tshardName\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x62_name\x18\x03 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x04 \x01(\t\x12\x16\n\x0epartition_name\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x62ID\x18\x06 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x07 \x01(\x03\x12\x13\n\x0bpartitionID\x18\x08 \x01(\x03\x12\x1a\n\x12int64_primary_keys\x18\t \x03(\x03\x12\x12\n\ntimestamps\x18\n \x03(\x04\x12\x10\n\x08num_rows\x18\x0b \x01(\x03\x12.\n\x0cprimary_keys\x18\x0c \x01(\x0b\x32\x18.milvus.proto.schema.IDs\"W\n\x0bMsgPosition\x12\x14\n\x0c\x63hannel_name\x18\x01 \x01(\t\x12\r\n\x05msgID\x18\x02 \x01(\x0c\x12\x10\n\x08msgGroup\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\"\x9f\x02\n\x17\x43reateCollectionRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x0f\n\x07\x64\x62_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63ollectionName\x18\x03 \x01(\t\x12\x15\n\rpartitionName\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x62ID\x18\x05 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x06 \x01(\x03\x12\x13\n\x0bpartitionID\x18\x07 \x01(\x03\x12\x0e\n\x06schema\x18\x08 \x01(\x0c\x12\x1b\n\x13virtualChannelNames\x18\t \x03(\t\x12\x1c\n\x14physicalChannelNames\x18\n \x03(\t\x12\x14\n\x0cpartitionIDs\x18\x0b \x03(\x03\"\x90\x01\n\x15\x44ropCollectionRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x0f\n\x07\x64\x62_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63ollectionName\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x62ID\x18\x04 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x05 \x01(\x03\"\xbf\x01\n\x16\x43reatePartitionRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x0f\n\x07\x64\x62_name\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12\x16\n\x0epartition_name\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x62ID\x18\x05 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x06 \x01(\x03\x12\x13\n\x0bpartitionID\x18\x07 \x01(\x03\"\xbd\x01\n\x14\x44ropPartitionRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x0f\n\x07\x64\x62_name\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12\x16\n\x0epartition_name\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x62ID\x18\x05 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x06 \x01(\x03\x12\x13\n\x0bpartitionID\x18\x07 \x01(\x03\"9\n\x0bTimeTickMsg\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\"\x9f\x01\n\rDataNodeTtMsg\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x39\n\x0esegments_stats\x18\x04 \x03(\x0b\x32!.milvus.proto.common.SegmentStats*2\n\x11InsertDataVersion\x12\x0c\n\x08RowBased\x10\x00\x12\x0f\n\x0b\x43olumnBased\x10\x01\x42\x33Z1github.com/milvus-io/milvus-proto/go-api/v2/msgpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/milvus-io/milvus-proto/go-api/v2/msgpb'
  _INSERTDATAVERSION._serialized_start=1939
  _INSERTDATAVERSION._serialized_end=1989
  _INSERTREQUEST._serialized_start=60
  _INSERTREQUEST._serialized_end=486
  _DELETEREQUEST._serialized_start=489
  _DELETEREQUEST._serialized_end=804
  _MSGPOSITION._serialized_start=806
  _MSGPOSITION._serialized_end=893
  _CREATECOLLECTIONREQUEST._serialized_start=896
  _CREATECOLLECTIONREQUEST._serialized_end=1183
  _DROPCOLLECTIONREQUEST._serialized_start=1186
  _DROPCOLLECTIONREQUEST._serialized_end=1330
  _CREATEPARTITIONREQUEST._serialized_start=1333
  _CREATEPARTITIONREQUEST._serialized_end=1524
  _DROPPARTITIONREQUEST._serialized_start=1527
  _DROPPARTITIONREQUEST._serialized_end=1716
  _TIMETICKMSG._serialized_start=1718
  _TIMETICKMSG._serialized_end=1775
  _DATANODETTMSG._serialized_start=1778
  _DATANODETTMSG._serialized_end=1937
# @@protoc_insertion_point(module_scope)
