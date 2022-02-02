from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Union

from .base import PythonCode, Statement, Expression
from .constants import Keywords, Symbols
from .core import Block

__all__ = ['If', 'Elif', 'Else', 'While', 'For']


@dataclass
class If(Statement):
    condition: Expression
    block: Block
    alt: Optional[Union[Elif, Else]] = None

    def tokens(self) -> list[str]:
        tokens = [
            Keywords.IF, Symbols.SPACE, *self.condition.tokens(), Symbols.COLON,
            *self.block.tokens()
        ]

        if self.alt:
            tokens.extend(self.alt.tokens())

        return tokens


@dataclass
class Elif(PythonCode):
    condition: Expression
    block: Block
    alt: Optional[Union[Elif, Else]] = None

    def tokens(self) -> list[str]:
        tokens = [
            Keywords.ELIF, Symbols.SPACE, *self.condition.tokens(), Symbols.COLON,
            *self.block.tokens()
        ]

        if self.alt:
            tokens.extend(self.alt.tokens())

        return tokens


@dataclass
class Else(PythonCode):
    block: Block

    def tokens(self) -> list[str]:
        return [
            Keywords.ELSE,
            Symbols.COLON,
            *self.block.tokens()
        ]


@dataclass
class While(Statement):
    condition: Expression
    block: Block
    alt: Optional[Else] = None

    def tokens(self) -> list[str]:
        tokens = [
            Keywords.WHILE,
            Symbols.SPACE,
            *self.condition.tokens(),
            Symbols.COLON,
            *self.block.tokens()
        ]

        if self.alt:
            tokens.extend(self.alt.tokens())

        return tokens


@dataclass
class For(Statement):
    vars: Expression
    iterator: Expression
    block: Block
    alt: Optional[Else] = None

    def tokens(self) -> list[str]:
        tokens = [
            Keywords.FOR,
            Symbols.SPACE,
            *self.vars.tokens(),
            Symbols.SPACE,
            Keywords.IN,
            Symbols.SPACE,
            *self.iterator.tokens(),
            Symbols.COLON,
            *self.block.tokens()
        ]

        if self.alt:
            tokens.extend(self.alt.tokens())

        return tokens
