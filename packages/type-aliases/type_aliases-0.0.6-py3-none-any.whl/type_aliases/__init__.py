import collections
import collections.abc as abstract_base_classes
import typing

import typing_extensions

__all__ = [
    "Bool",
    "Bytes",
    "Dict",
    "Float",
    "Int",
    "List",
    "Set",
    "Str",
    "Tuple",
    "Type",
    "Object",
    "Any",
    "AnyStr",
    "Literal",
    "LiteralString",
    "NamedTuple",
    "Never",
    "NewType",
    "NoReturn",
    "NotRequired",
    "Optional",
    "ParamSpecArgs",
    "ParamSpecKwargs",
    "Required",
    "Self",
    "TypeAlias",
    "TypeGuard",
    "TypeVar",
    "Union",
    "Unpack",
    "AsyncGenerator",
    "AsyncIterable",
    "AsyncIterator",
    "Awaitable",
    "ByteString",
    "Callable",
    "Collection",
    "Container",
    "Coroutine",
    "Hashable",
    "ItemsView",
    "Iterable",
    "Iterator",
    "KeysView",
    "Mapping",
    "MappingView",
    "MutableMapping",
    "MutableSequence",
    "MutableSet",
    "Sequence",
    "Sized",
    "ValuesView",
    "ChainMap",
    "Counter",
    "OrderedDict",
    "UserDict",
    "UserList",
]

# Capitalised stdlib types

Bool = bool
Bytes = bytes
Dict = dict
Float = float
Int = int
List = list
Set = set
Str = str
Tuple = tuple
Type = type
Object = object

# Re-exported from typing

Any = typing.Any
AnyStr: typing_extensions.TypeAlias = typing_extensions.AnyStr
Literal = typing.Literal
LiteralString = typing_extensions.LiteralString
NamedTuple = typing.NamedTuple
Never = typing_extensions.Never
NewType = typing.NewType
NoReturn = typing.NoReturn
NotRequired = typing_extensions.NotRequired
Optional = typing.Optional
ParamSpecArgs = typing_extensions.ParamSpecArgs
ParamSpecKwargs = typing_extensions.ParamSpecKwargs
Required = typing_extensions.Required
Self = typing_extensions.Self
TypeAlias = typing_extensions.TypeAlias
TypeGuard = typing_extensions.TypeGuard
TypeVar: typing_extensions.TypeAlias = typing.TypeVar
Union = typing.Union
Unpack = typing_extensions.Unpack

# Re-exported from ABC

AsyncGenerator = abstract_base_classes.AsyncGenerator
AsyncIterable = abstract_base_classes.AsyncIterable
AsyncIterator = abstract_base_classes.AsyncIterator
Awaitable = abstract_base_classes.Awaitable
ByteString = abstract_base_classes.ByteString
Callable = abstract_base_classes.Callable
Collection = abstract_base_classes.Collection
Container = abstract_base_classes.Container
Coroutine = abstract_base_classes.Coroutine
Hashable = abstract_base_classes.Hashable
ItemsView = abstract_base_classes.ItemsView
Iterable = abstract_base_classes.Iterable
Iterator = abstract_base_classes.Iterator
KeysView = abstract_base_classes.KeysView
Mapping = abstract_base_classes.Mapping
MappingView = abstract_base_classes.MappingView
MutableMapping = abstract_base_classes.MutableMapping
MutableSequence = abstract_base_classes.MutableSequence
MutableSet = abstract_base_classes.MutableSet
Sequence = abstract_base_classes.Sequence
Sized = abstract_base_classes.Sized
ValuesView = abstract_base_classes.ValuesView

# Re-exported from collections

ChainMap = collections.ChainMap
Counter = collections.Counter
OrderedDict = collections.OrderedDict
UserDict = collections.UserDict
UserList = collections.UserList
