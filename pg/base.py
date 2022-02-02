from abc import ABC, abstractmethod

__all__ = [
    'PythonCode',
    'Statement',
    'Expression'
]


class PythonCode(ABC):
    @abstractmethod
    def tokens(self) -> list[str]:
        """Return the list of tokens to build the python code object."""

    def __str__(self):
        return "".join(map(str, self.tokens()))


class Statement(PythonCode, ABC):
    ...


class Expression(PythonCode, ABC):
    ...
