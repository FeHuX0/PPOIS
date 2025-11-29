from __future__ import annotations

from typing import Iterable, Iterator, List, TypeVar

from .Edge import Edge
from .Vertex import Vertex

T = TypeVar("T")


class IncidentEdgeIterator(Iterator[Edge[T]]):
    """Iterates over edges incident to a specific vertex."""

    def __init__(self, vertex: Vertex[T], edges: Iterable[Edge[T]]) -> None:
        self._vertex = vertex
        self._data: List[Edge[T]] = [edge for edge in edges if edge.connects(vertex)]
        self._index = 0

    def __iter__(self) -> "IncidentEdgeIterator[T]":
        self._index = 0
        return self

    def __next__(self) -> Edge[T]:
        if self._index >= len(self._data):
            raise StopIteration
        edge = self._data[self._index]
        self._index += 1
        return edge

    def __reversed__(self) -> "IncidentEdgeIterator[T]":
        return IncidentEdgeIterator(self._vertex, reversed(self._data))
