from dataclasses import dataclass

from .base import Expression
from .constants import Symbols

__all__ = [
    'Eq',
    'Ne',
    'Le',
    'Lt',
    'Ge',
    'Gt',
    'Add',
    'Sub',
    'Mul',
    'Truediv',
    'Floordiv',
    'Mod'
]


@dataclass
class Eq(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.EQUAL_EQUAL,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Ne(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.EXC_EQUAL,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Le(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.LV_EQUAL,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Lt(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.LV,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Ge(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.RV_EQUAL,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Gt(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.RV,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Add(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.PLUS,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Sub(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.MINUS,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Mul(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.STAR,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Truediv(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.SLASH,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Floordiv(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.SLASH_SLASH,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Mod(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.PERCENT,
            Symbols.SPACE,
            *self.right.tokens()
        ]


@dataclass
class Pow(Expression):
    left: Expression
    right: Expression

    def tokens(self) -> list[str]:
        return [
            *self.left.tokens(),
            Symbols.SPACE,
            Symbols.STAR_STAR,
            Symbols.SPACE,
            *self.right.tokens()
        ]
