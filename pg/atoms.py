from dataclasses import dataclass

from .base import PythonCode

__all__ = [
    'Variable',
    'Int',
    'Float',
    'Bool',
    'Str'
]


@dataclass
class Variable(PythonCode):
    name: str

    def __post_init__(self):
        assert self.name.isidentifier()

    def tokens(self) -> list[str]:
        return [self.name]


@dataclass
class Int(PythonCode):
    value: int

    def tokens(self) -> list[str]:
        return [repr(self.value)]


@dataclass
class Float(PythonCode):
    value: float

    def tokens(self) -> list[str]:
        return [repr(self.value)]


@dataclass
class Bool(PythonCode):
    value: bool

    def tokens(self) -> list[str]:
        return [repr(self.value)]


@dataclass
class Str(PythonCode):
    value: str

    def tokens(self) -> list[str]:
        return [repr(self.value)]
