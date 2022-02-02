from typing import Optional

from .base import Statement, Expression
from .constants import Keywords, Symbols

__all__ = ['PASS', 'CONTINUE', 'BREAK', 'Return', 'Yield', 'Raise']


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
