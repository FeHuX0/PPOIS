from __future__ import annotations

from typing import Iterable, Iterator, List, TypeVar

from .Edge import Edge
from .Vertex import Vertex

T = TypeVar("T")


class AdjacentVertexIterator(Iterator[Vertex[T]]):
    """Iterates over vertices adjacent to the given vertex."""

    def __init__(self, vertex: Vertex[T], edges: Iterable[Edge[T]]) -> None:
        self._vertex = vertex
        adjacent = []
        for edge in edges:
            if edge.connects(vertex):
                adjacent.append(edge.other(vertex))
        self._data: List[Vertex[T]] = adjacent
        self._index = 0

    def __iter__(self) -> "AdjacentVertexIterator[T]":
        self._index = 0
        return self

    def __next__(self) -> Vertex[T]:
        if self._index >= len(self._data):
            raise StopIteration
        vertex = self._data[self._index]
        self._index += 1
        return vertex

    def __reversed__(self) -> "AdjacentVertexIterator[T]":
        return AdjacentVertexIterator(self._vertex, reversed(self._data))
