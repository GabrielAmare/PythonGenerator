from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Union

from .base import PythonCode, Statement, Expression
from .constants import Keywords, Symbols

__all__ = ['Scope', 'Block']


@dataclass
class Scope(PythonCode):
    statements: list[Statement]

    def tokens(self) -> list[str]:
        tokens = []

        for statement in self.statements:
            tokens.append(Symbols.NEWLINE)

            for token in statement.tokens():
                tokens.append(token)

        return tokens


@dataclass
class Block(PythonCode):
    statements: list[Statement]

    def tokens(self) -> list[str]:
        tokens = []

        for statement in self.statements:
            tokens.append(Symbols.NEWLINE)
            tokens.append(Symbols.INDENT)

            for token in statement.tokens():
                tokens.append(token)

                if token is Symbols.NEWLINE:
                    tokens.append(Symbols.INDENT)

        return tokens