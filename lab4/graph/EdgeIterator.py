from __future__ import annotations

from typing import Iterable, Iterator, List, TypeVar

from .Edge import Edge

T = TypeVar("T")


class EdgeIterator(Iterator[Edge[T]]):
    """Bidirectional-capable iterator over edges."""

    def __init__(self, edges: Iterable[Edge[T]]) -> None:
        self._data: List[Edge[T]] = list(edges)
        self._index = 0

    def __iter__(self) -> "EdgeIterator[T]":
        self._index = 0
        return self

    def __next__(self) -> Edge[T]:
        if self._index >= len(self._data):
            raise StopIteration
        edge = self._data[self._index]
        self._index += 1
        return edge

    def __reversed__(self) -> "EdgeIterator[T]":
        return EdgeIterator(reversed(self._data))
