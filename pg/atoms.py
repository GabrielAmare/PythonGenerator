from dataclasses import dataclass

from .base import Expression

__all__ = [
    'Variable',
    'Int',
    'Float',
    'Bool',
    'Str'
]


@dataclass
class Variable(Expression):
    name: str

    def __post_init__(self):
        assert self.name.isidentifier()

    def tokens(self) -> list[str]:
        return [self.name]


@dataclass
class Int(Expression):
    value: int

    def tokens(self) -> list[str]:
        return [repr(self.value)]


@dataclass
class Float(Expression):
    value: float

    def tokens(self) -> list[str]:
        return [repr(self.value)]


@dataclass
class Bool(Expression):
    value: bool

    def tokens(self) -> list[str]:
        return [repr(self.value)]


@dataclass
class Str(Expression):
    value: str

    def tokens(self) -> list[str]:
        return [repr(self.value)]
