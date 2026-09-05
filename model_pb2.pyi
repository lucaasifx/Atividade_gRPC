from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Task(_message.Message):
    __slots__ = ("id", "title", "description", "status", "data", "responsible")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSIBLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    description: str
    status: bool
    data: str
    responsible: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[bool] = ..., data: _Optional[str] = ..., responsible: _Optional[str] = ...) -> None: ...

class TaskID(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class TaskList(_message.Message):
    __slots__ = ("list",)
    LIST_FIELD_NUMBER: _ClassVar[int]
    list: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, list: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...
