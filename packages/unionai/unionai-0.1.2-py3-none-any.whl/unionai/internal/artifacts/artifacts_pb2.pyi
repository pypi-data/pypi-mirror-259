from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from flyteidl.admin import launch_plan_pb2 as _launch_plan_pb2
from flyteidl.core import literals_pb2 as _literals_pb2
from flyteidl.core import types_pb2 as _types_pb2
from flyteidl.core import identifier_pb2 as _identifier_pb2
from flyteidl.core import artifact_id_pb2 as _artifact_id_pb2
from flyteidl.core import interface_pb2 as _interface_pb2
from flyteidl.event import cloudevents_pb2 as _cloudevents_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Artifact(_message.Message):
    __slots__ = ["artifact_id", "spec", "tags", "source"]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    artifact_id: _artifact_id_pb2.ArtifactID
    spec: ArtifactSpec
    tags: _containers.RepeatedScalarFieldContainer[str]
    source: ArtifactSource
    def __init__(self, artifact_id: _Optional[_Union[_artifact_id_pb2.ArtifactID, _Mapping]] = ..., spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., source: _Optional[_Union[ArtifactSource, _Mapping]] = ...) -> None: ...

class CreateArtifactRequest(_message.Message):
    __slots__ = ["artifact_key", "version", "spec", "partitions", "time_partition_value", "source"]
    class PartitionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_PARTITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    artifact_key: _artifact_id_pb2.ArtifactKey
    version: str
    spec: ArtifactSpec
    partitions: _containers.ScalarMap[str, str]
    time_partition_value: _timestamp_pb2.Timestamp
    source: ArtifactSource
    def __init__(self, artifact_key: _Optional[_Union[_artifact_id_pb2.ArtifactKey, _Mapping]] = ..., version: _Optional[str] = ..., spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., partitions: _Optional[_Mapping[str, str]] = ..., time_partition_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[_Union[ArtifactSource, _Mapping]] = ...) -> None: ...

class ArtifactSource(_message.Message):
    __slots__ = ["workflow_execution", "node_id", "task_id", "retry_attempt", "principal"]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    workflow_execution: _identifier_pb2.WorkflowExecutionIdentifier
    node_id: str
    task_id: _identifier_pb2.Identifier
    retry_attempt: int
    principal: str
    def __init__(self, workflow_execution: _Optional[_Union[_identifier_pb2.WorkflowExecutionIdentifier, _Mapping]] = ..., node_id: _Optional[str] = ..., task_id: _Optional[_Union[_identifier_pb2.Identifier, _Mapping]] = ..., retry_attempt: _Optional[int] = ..., principal: _Optional[str] = ...) -> None: ...

class ArtifactSpec(_message.Message):
    __slots__ = ["value", "type", "short_description", "user_metadata", "metadata_type", "created_at", "file_format"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    value: _literals_pb2.Literal
    type: _types_pb2.LiteralType
    short_description: str
    user_metadata: _any_pb2.Any
    metadata_type: str
    created_at: _timestamp_pb2.Timestamp
    file_format: str
    def __init__(self, value: _Optional[_Union[_literals_pb2.Literal, _Mapping]] = ..., type: _Optional[_Union[_types_pb2.LiteralType, _Mapping]] = ..., short_description: _Optional[str] = ..., user_metadata: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., metadata_type: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., file_format: _Optional[str] = ...) -> None: ...

class Trigger(_message.Message):
    __slots__ = ["trigger_id", "triggers"]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    trigger_id: _identifier_pb2.Identifier
    triggers: _containers.RepeatedCompositeFieldContainer[_artifact_id_pb2.ArtifactID]
    def __init__(self, trigger_id: _Optional[_Union[_identifier_pb2.Identifier, _Mapping]] = ..., triggers: _Optional[_Iterable[_Union[_artifact_id_pb2.ArtifactID, _Mapping]]] = ...) -> None: ...

class CreateArtifactResponse(_message.Message):
    __slots__ = ["artifact"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    artifact: Artifact
    def __init__(self, artifact: _Optional[_Union[Artifact, _Mapping]] = ...) -> None: ...

class GetArtifactRequest(_message.Message):
    __slots__ = ["query", "details"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    query: _artifact_id_pb2.ArtifactQuery
    details: bool
    def __init__(self, query: _Optional[_Union[_artifact_id_pb2.ArtifactQuery, _Mapping]] = ..., details: bool = ...) -> None: ...

class GetArtifactResponse(_message.Message):
    __slots__ = ["artifact"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    artifact: Artifact
    def __init__(self, artifact: _Optional[_Union[Artifact, _Mapping]] = ...) -> None: ...

class SearchOptions(_message.Message):
    __slots__ = ["strict_partitions", "latest_by_key"]
    STRICT_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    LATEST_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    strict_partitions: bool
    latest_by_key: bool
    def __init__(self, strict_partitions: bool = ..., latest_by_key: bool = ...) -> None: ...

class SearchArtifactsRequest(_message.Message):
    __slots__ = ["artifact_key", "partitions", "time_partition_value", "principal", "version", "options", "token", "limit"]
    ARTIFACT_KEY_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_PARTITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    artifact_key: _artifact_id_pb2.ArtifactKey
    partitions: _artifact_id_pb2.Partitions
    time_partition_value: _timestamp_pb2.Timestamp
    principal: str
    version: str
    options: SearchOptions
    token: str
    limit: int
    def __init__(self, artifact_key: _Optional[_Union[_artifact_id_pb2.ArtifactKey, _Mapping]] = ..., partitions: _Optional[_Union[_artifact_id_pb2.Partitions, _Mapping]] = ..., time_partition_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., principal: _Optional[str] = ..., version: _Optional[str] = ..., options: _Optional[_Union[SearchOptions, _Mapping]] = ..., token: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class SearchArtifactsResponse(_message.Message):
    __slots__ = ["artifacts", "token"]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[Artifact]
    token: str
    def __init__(self, artifacts: _Optional[_Iterable[_Union[Artifact, _Mapping]]] = ..., token: _Optional[str] = ...) -> None: ...

class FindByWorkflowExecRequest(_message.Message):
    __slots__ = ["exec_id", "direction"]
    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        INPUTS: _ClassVar[FindByWorkflowExecRequest.Direction]
        OUTPUTS: _ClassVar[FindByWorkflowExecRequest.Direction]
    INPUTS: FindByWorkflowExecRequest.Direction
    OUTPUTS: FindByWorkflowExecRequest.Direction
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    exec_id: _identifier_pb2.WorkflowExecutionIdentifier
    direction: FindByWorkflowExecRequest.Direction
    def __init__(self, exec_id: _Optional[_Union[_identifier_pb2.WorkflowExecutionIdentifier, _Mapping]] = ..., direction: _Optional[_Union[FindByWorkflowExecRequest.Direction, str]] = ...) -> None: ...

class AddTagRequest(_message.Message):
    __slots__ = ["artifact_id", "value", "overwrite"]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    artifact_id: _artifact_id_pb2.ArtifactID
    value: str
    overwrite: bool
    def __init__(self, artifact_id: _Optional[_Union[_artifact_id_pb2.ArtifactID, _Mapping]] = ..., value: _Optional[str] = ..., overwrite: bool = ...) -> None: ...

class AddTagResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateTriggerRequest(_message.Message):
    __slots__ = ["trigger_launch_plan"]
    TRIGGER_LAUNCH_PLAN_FIELD_NUMBER: _ClassVar[int]
    trigger_launch_plan: _launch_plan_pb2.LaunchPlan
    def __init__(self, trigger_launch_plan: _Optional[_Union[_launch_plan_pb2.LaunchPlan, _Mapping]] = ...) -> None: ...

class CreateTriggerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeactivateTriggerRequest(_message.Message):
    __slots__ = ["trigger_id"]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    trigger_id: _identifier_pb2.Identifier
    def __init__(self, trigger_id: _Optional[_Union[_identifier_pb2.Identifier, _Mapping]] = ...) -> None: ...

class DeactivateTriggerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ArtifactProducer(_message.Message):
    __slots__ = ["entity_id", "outputs"]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    entity_id: _identifier_pb2.Identifier
    outputs: _interface_pb2.VariableMap
    def __init__(self, entity_id: _Optional[_Union[_identifier_pb2.Identifier, _Mapping]] = ..., outputs: _Optional[_Union[_interface_pb2.VariableMap, _Mapping]] = ...) -> None: ...

class RegisterProducerRequest(_message.Message):
    __slots__ = ["producers"]
    PRODUCERS_FIELD_NUMBER: _ClassVar[int]
    producers: _containers.RepeatedCompositeFieldContainer[ArtifactProducer]
    def __init__(self, producers: _Optional[_Iterable[_Union[ArtifactProducer, _Mapping]]] = ...) -> None: ...

class ArtifactConsumer(_message.Message):
    __slots__ = ["entity_id", "inputs"]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    entity_id: _identifier_pb2.Identifier
    inputs: _interface_pb2.ParameterMap
    def __init__(self, entity_id: _Optional[_Union[_identifier_pb2.Identifier, _Mapping]] = ..., inputs: _Optional[_Union[_interface_pb2.ParameterMap, _Mapping]] = ...) -> None: ...

class RegisterConsumerRequest(_message.Message):
    __slots__ = ["consumers"]
    CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    consumers: _containers.RepeatedCompositeFieldContainer[ArtifactConsumer]
    def __init__(self, consumers: _Optional[_Iterable[_Union[ArtifactConsumer, _Mapping]]] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutionInputsRequest(_message.Message):
    __slots__ = ["execution_id", "inputs"]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    execution_id: _identifier_pb2.WorkflowExecutionIdentifier
    inputs: _containers.RepeatedCompositeFieldContainer[_artifact_id_pb2.ArtifactID]
    def __init__(self, execution_id: _Optional[_Union[_identifier_pb2.WorkflowExecutionIdentifier, _Mapping]] = ..., inputs: _Optional[_Iterable[_Union[_artifact_id_pb2.ArtifactID, _Mapping]]] = ...) -> None: ...

class ExecutionInputsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListUsageRequest(_message.Message):
    __slots__ = ["artifact_id"]
    ARTIFACT_ID_FIELD_NUMBER: _ClassVar[int]
    artifact_id: _artifact_id_pb2.ArtifactID
    def __init__(self, artifact_id: _Optional[_Union[_artifact_id_pb2.ArtifactID, _Mapping]] = ...) -> None: ...

class ListUsageResponse(_message.Message):
    __slots__ = ["executions"]
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_identifier_pb2.WorkflowExecutionIdentifier]
    def __init__(self, executions: _Optional[_Iterable[_Union[_identifier_pb2.WorkflowExecutionIdentifier, _Mapping]]] = ...) -> None: ...
