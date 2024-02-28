from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODE_UNSPECIFIED: _ClassVar[Mode]
    MODE_CONVERSATION: _ClassVar[Mode]
    MODE_CHATBOT: _ClassVar[Mode]
    MODE_EMAIL: _ClassVar[Mode]
    MODE_PHONE: _ClassVar[Mode]
    MODE_API: _ClassVar[Mode]
MODE_UNSPECIFIED: Mode
MODE_CONVERSATION: Mode
MODE_CHATBOT: Mode
MODE_EMAIL: Mode
MODE_PHONE: Mode
MODE_API: Mode

class User(_message.Message):
    __slots__ = ("guid", "email", "name", "conversations")
    class ConversationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GUID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    guid: str
    email: str
    name: str
    conversations: _containers.ScalarMap[str, str]
    def __init__(self, guid: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., conversations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Appliance(_message.Message):
    __slots__ = ("guid", "name", "purpose", "agents", "tools", "data_sources", "vector_stores")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    VECTOR_STORES_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    purpose: str
    agents: _containers.RepeatedCompositeFieldContainer[Agent]
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    vector_stores: _containers.RepeatedCompositeFieldContainer[VectorStore]
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ..., purpose: _Optional[str] = ..., agents: _Optional[_Iterable[_Union[Agent, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]] = ..., vector_stores: _Optional[_Iterable[_Union[VectorStore, _Mapping]]] = ...) -> None: ...

class Agent(_message.Message):
    __slots__ = ("guid", "name", "purpose", "email", "reply_as", "phone", "behaviors", "tools")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    REPLY_AS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    BEHAVIORS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    purpose: str
    email: str
    reply_as: str
    phone: str
    behaviors: _containers.RepeatedCompositeFieldContainer[Behavior]
    tools: _containers.RepeatedCompositeFieldContainer[Tool]
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ..., purpose: _Optional[str] = ..., email: _Optional[str] = ..., reply_as: _Optional[str] = ..., phone: _Optional[str] = ..., behaviors: _Optional[_Iterable[_Union[Behavior, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[Tool, _Mapping]]] = ...) -> None: ...

class Behavior(_message.Message):
    __slots__ = ("mode", "text", "model", "provider", "assistant_id", "output_format", "footer")
    MODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    mode: Mode
    text: str
    model: str
    provider: str
    assistant_id: str
    output_format: str
    footer: str
    def __init__(self, mode: _Optional[_Union[Mode, str]] = ..., text: _Optional[str] = ..., model: _Optional[str] = ..., provider: _Optional[str] = ..., assistant_id: _Optional[str] = ..., output_format: _Optional[str] = ..., footer: _Optional[str] = ...) -> None: ...

class Tool(_message.Message):
    __slots__ = ("guid", "name", "purpose", "definition")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    purpose: str
    definition: str
    def __init__(self, guid: _Optional[str] = ..., name: _Optional[str] = ..., purpose: _Optional[str] = ..., definition: _Optional[str] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ("guid", "title", "created_at", "user_guid", "agent_guid", "mode", "messages")
    GUID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_GUID_FIELD_NUMBER: _ClassVar[int]
    AGENT_GUID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    guid: str
    title: str
    created_at: str
    user_guid: str
    agent_guid: str
    mode: Mode
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, guid: _Optional[str] = ..., title: _Optional[str] = ..., created_at: _Optional[str] = ..., user_guid: _Optional[str] = ..., agent_guid: _Optional[str] = ..., mode: _Optional[_Union[Mode, str]] = ..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("guid", "sender", "text", "created_at")
    class Sender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Message.Sender]
        USER: _ClassVar[Message.Sender]
        AGENT: _ClassVar[Message.Sender]
    UNSPECIFIED: Message.Sender
    USER: Message.Sender
    AGENT: Message.Sender
    GUID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    guid: str
    sender: Message.Sender
    text: str
    created_at: str
    def __init__(self, guid: _Optional[str] = ..., sender: _Optional[_Union[Message.Sender, str]] = ..., text: _Optional[str] = ..., created_at: _Optional[str] = ...) -> None: ...

class DataSource(_message.Message):
    __slots__ = ("name", "type", "filesystem", "webpage", "website", "s3", "database", "api")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DataSource.Type]
        FILESYSTEM: _ClassVar[DataSource.Type]
        WEBPAGE: _ClassVar[DataSource.Type]
        WEBSITE: _ClassVar[DataSource.Type]
        S3: _ClassVar[DataSource.Type]
        DATABASE: _ClassVar[DataSource.Type]
        API: _ClassVar[DataSource.Type]
    UNSPECIFIED: DataSource.Type
    FILESYSTEM: DataSource.Type
    WEBPAGE: DataSource.Type
    WEBSITE: DataSource.Type
    S3: DataSource.Type
    DATABASE: DataSource.Type
    API: DataSource.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    S3_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: DataSource.Type
    filesystem: Filesystem
    webpage: Webpage
    website: Website
    s3: S3
    database: Database
    api: Api
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[DataSource.Type, str]] = ..., filesystem: _Optional[_Union[Filesystem, _Mapping]] = ..., webpage: _Optional[_Union[Webpage, _Mapping]] = ..., website: _Optional[_Union[Website, _Mapping]] = ..., s3: _Optional[_Union[S3, _Mapping]] = ..., database: _Optional[_Union[Database, _Mapping]] = ..., api: _Optional[_Union[Api, _Mapping]] = ...) -> None: ...

class Filesystem(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class Webpage(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class Website(_message.Message):
    __slots__ = ("url", "depth")
    URL_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    url: str
    depth: int
    def __init__(self, url: _Optional[str] = ..., depth: _Optional[int] = ...) -> None: ...

class S3(_message.Message):
    __slots__ = ("bucket", "key")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    key: str
    def __init__(self, bucket: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class Database(_message.Message):
    __slots__ = ("host", "port", "database", "username", "password", "table")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: str
    database: str
    username: str
    password: str
    table: str
    def __init__(self, host: _Optional[str] = ..., port: _Optional[str] = ..., database: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...

class Api(_message.Message):
    __slots__ = ("url", "username", "password")
    URL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    url: str
    username: str
    password: str
    def __init__(self, url: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class VectorStore(_message.Message):
    __slots__ = ("name", "type", "index", "pinecone", "qdrant")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VectorStore.Type]
        PINECONE: _ClassVar[VectorStore.Type]
        QDRANT: _ClassVar[VectorStore.Type]
    UNSPECIFIED: VectorStore.Type
    PINECONE: VectorStore.Type
    QDRANT: VectorStore.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PINECONE_FIELD_NUMBER: _ClassVar[int]
    QDRANT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    index: str
    pinecone: PineconeIndex
    qdrant: QdrantCollection
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., index: _Optional[str] = ..., pinecone: _Optional[_Union[PineconeIndex, _Mapping]] = ..., qdrant: _Optional[_Union[QdrantCollection, _Mapping]] = ...) -> None: ...

class PineconeIndex(_message.Message):
    __slots__ = ("name", "dimension", "metric")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    name: str
    dimension: int
    metric: str
    def __init__(self, name: _Optional[str] = ..., dimension: _Optional[int] = ..., metric: _Optional[str] = ...) -> None: ...

class QdrantCollection(_message.Message):
    __slots__ = ("name", "location", "url", "port", "dimension", "metric")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: str
    url: str
    port: int
    dimension: int
    metric: str
    def __init__(self, name: _Optional[str] = ..., location: _Optional[str] = ..., url: _Optional[str] = ..., port: _Optional[int] = ..., dimension: _Optional[int] = ..., metric: _Optional[str] = ...) -> None: ...
