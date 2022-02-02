from __future__ import annotations

from dataclasses import dataclass

from .base import PythonCode, Statement
from .constants import Symbols

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

    def __post_init__(self):
        assert len(self.statements) > 0, "cannot define a block without statements !"

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
