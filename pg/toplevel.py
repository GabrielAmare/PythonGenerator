from dataclasses import dataclass

from .base import PythonCode
from .core import Scope

__all__ = ['Module']


@dataclass
class Module(PythonCode):
    name: str
    scope: Scope

    def tokens(self) -> list[str]:
        return self.scope.tokens()
