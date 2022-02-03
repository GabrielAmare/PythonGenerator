from dataclasses import dataclass
from typing import Optional

from .atoms import Variable
from .base import Statement, Expression
from .constants import Keywords, Symbols

__all__ = [
    'PASS',
    'CONTINUE',
    'BREAK',
    'Return',
    'Yield',
    'Raise',
    'Assign',
    'IAdd',
    'ISub',
    'IMul',
    'ITruediv',
    'IFloordiv',
    'IMod',
    'IPow'
]


class _Pass(Statement):
    def tokens(self) -> list[str]:
        return [Keywords.PASS]


class _Continue(Statement):
    def tokens(self) -> list[str]:
        return [Keywords.CONTINUE]


class _Break(Statement):
    def tokens(self) -> list[str]:
        return [Keywords.BREAK]


PASS = _Pass()
CONTINUE = _Continue()
BREAK = _Break()


@dataclass
class Return(Statement):
    expression: Optional[Expression] = None

    def tokens(self) -> list[str]:
        tokens = [Keywords.RETURN]

        if self.expression:
            tokens.extend([
                Symbols.SPACE,
                *self.expression.tokens()
            ])

        return tokens


@dataclass
class Yield(Statement):
    expression: Optional[Expression] = None

    def tokens(self) -> list[str]:
        tokens = [Keywords.YIELD]

        if self.expression:
            tokens.extend([
                Symbols.SPACE,
                *self.expression.tokens()
            ])

        return tokens


@dataclass
class Raise(Statement):
    expression: Optional[Expression] = None

    def tokens(self) -> list[str]:
        tokens = [Keywords.RAISE]

        if self.expression:
            tokens.extend([
                Symbols.SPACE,
                *self.expression.tokens()
            ])

        return tokens


@dataclass
class Assign(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class IAdd(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.PLUS_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class ISub(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.MINUS_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class IMul(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.STAR_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class ITruediv(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.SLASH_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class IFloordiv(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.SLASH_SLASH_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class IMod(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.PERCENT_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]


@dataclass
class IPow(Statement):
    var: Variable
    value: Expression

    def tokens(self) -> list[str]:
        return [
            *self.var.tokens(),
            Symbols.SPACE,
            Symbols.STAR_STAR_EQUAL,
            Symbols.SPACE,
            *self.value.tokens()
        ]
