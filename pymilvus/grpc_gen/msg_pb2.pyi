import common_pb2 as _common_pb2
import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ColumnBased: InsertDataVersion
DESCRIPTOR: _descriptor.FileDescriptor
RowBased: InsertDataVersion

class CreateCollectionRequest(_message.Message):
    __slots__ = ["base", "collectionID", "collectionName", "dbID", "db_name", "partitionID", "partitionIDs", "partitionName", "physicalChannelNames", "schema", "virtualChannelNames"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONNAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONNAME_FIELD_NUMBER: _ClassVar[int]
    PHYSICALCHANNELNAMES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    VIRTUALCHANNELNAMES_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    collectionName: str
    dbID: int
    db_name: str
    partitionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    partitionName: str
    physicalChannelNames: _containers.RepeatedScalarFieldContainer[str]
    schema: bytes
    virtualChannelNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collectionName: _Optional[str] = ..., partitionName: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., schema: _Optional[bytes] = ..., virtualChannelNames: _Optional[_Iterable[str]] = ..., physicalChannelNames: _Optional[_Iterable[str]] = ..., partitionIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class CreatePartitionRequest(_message.Message):
    __slots__ = ["base", "collectionID", "collection_name", "dbID", "db_name", "partitionID", "partition_name"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    collection_name: str
    dbID: int
    db_name: str
    partitionID: int
    partition_name: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ...) -> None: ...

class DataNodeTtMsg(_message.Message):
    __slots__ = ["base", "channel_name", "segments_stats", "timestamp"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_STATS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    channel_name: str
    segments_stats: _containers.RepeatedCompositeFieldContainer[_common_pb2.SegmentStats]
    timestamp: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., channel_name: _Optional[str] = ..., timestamp: _Optional[int] = ..., segments_stats: _Optional[_Iterable[_Union[_common_pb2.SegmentStats, _Mapping]]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ["base", "collectionID", "collection_name", "dbID", "db_name", "int64_primary_keys", "num_rows", "partitionID", "partition_name", "primary_keys", "shardName", "timestamps"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    INT64_PRIMARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    SHARDNAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    collection_name: str
    dbID: int
    db_name: str
    int64_primary_keys: _containers.RepeatedScalarFieldContainer[int]
    num_rows: int
    partitionID: int
    partition_name: str
    primary_keys: _schema_pb2.IDs
    shardName: str
    timestamps: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., shardName: _Optional[str] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., int64_primary_keys: _Optional[_Iterable[int]] = ..., timestamps: _Optional[_Iterable[int]] = ..., num_rows: _Optional[int] = ..., primary_keys: _Optional[_Union[_schema_pb2.IDs, _Mapping]] = ...) -> None: ...

class DropCollectionRequest(_message.Message):
    __slots__ = ["base", "collectionID", "collectionName", "dbID", "db_name"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONNAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    collectionName: str
    dbID: int
    db_name: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collectionName: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ...) -> None: ...

class DropPartitionRequest(_message.Message):
    __slots__ = ["base", "collectionID", "collection_name", "dbID", "db_name", "partitionID", "partition_name"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    collection_name: str
    dbID: int
    db_name: str
    partitionID: int
    partition_name: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ...) -> None: ...

class InsertRequest(_message.Message):
    __slots__ = ["base", "collectionID", "collection_name", "dbID", "db_name", "fields_data", "num_rows", "partitionID", "partition_name", "rowIDs", "row_data", "segmentID", "shardName", "timestamps", "version"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_DATA_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    ROWIDS_FIELD_NUMBER: _ClassVar[int]
    ROW_DATA_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    SHARDNAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    collection_name: str
    dbID: int
    db_name: str
    fields_data: _containers.RepeatedCompositeFieldContainer[_schema_pb2.FieldData]
    num_rows: int
    partitionID: int
    partition_name: str
    rowIDs: _containers.RepeatedScalarFieldContainer[int]
    row_data: _containers.RepeatedCompositeFieldContainer[_common_pb2.Blob]
    segmentID: int
    shardName: str
    timestamps: _containers.RepeatedScalarFieldContainer[int]
    version: InsertDataVersion
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., shardName: _Optional[str] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., segmentID: _Optional[int] = ..., timestamps: _Optional[_Iterable[int]] = ..., rowIDs: _Optional[_Iterable[int]] = ..., row_data: _Optional[_Iterable[_Union[_common_pb2.Blob, _Mapping]]] = ..., fields_data: _Optional[_Iterable[_Union[_schema_pb2.FieldData, _Mapping]]] = ..., num_rows: _Optional[int] = ..., version: _Optional[_Union[InsertDataVersion, str]] = ...) -> None: ...

class MsgPosition(_message.Message):
    __slots__ = ["channel_name", "msgGroup", "msgID", "timestamp"]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MSGGROUP_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    channel_name: str
    msgGroup: str
    msgID: bytes
    timestamp: int
    def __init__(self, channel_name: _Optional[str] = ..., msgID: _Optional[bytes] = ..., msgGroup: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class TimeTickMsg(_message.Message):
    __slots__ = ["base"]
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ...) -> None: ...

class InsertDataVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
