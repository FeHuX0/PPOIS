from __future__ import annotations

from typing import Iterable, Iterator, List, TypeVar

from .Vertex import Vertex

T = TypeVar("T")


class VertexIterator(Iterator[Vertex[T]]):
    """Bidirectional-capable iterator over vertices."""

    def __init__(self, vertices: Iterable[Vertex[T]]) -> None:
        self._data: List[Vertex[T]] = list(vertices)
        self._index = 0

    def __iter__(self) -> "VertexIterator[T]":
        self._index = 0
        return self

    def __next__(self) -> Vertex[T]:
        if self._index >= len(self._data):
            raise StopIteration
        value = self._data[self._index]
        self._index += 1
        return value

    def __reversed__(self) -> "VertexIterator[T]":
        return VertexIterator(reversed(self._data))
