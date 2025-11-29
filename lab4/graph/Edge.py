from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Tuple, TypeVar

from .Vertex import Vertex

T = TypeVar("T")


@dataclass(frozen=True)
class Edge(Generic[T]):
    """Undirected edge between two vertices."""

    first: Vertex[T]
    second: Vertex[T]

    def __post_init__(self) -> None:
        if self.first == self.second:
            raise ValueError("Self-loops are not allowed in this graph implementation.")

    @property
    def endpoints(self) -> Tuple[Vertex[T], Vertex[T]]:
        return self.first, self.second

    def connects(self, vertex: Vertex[T]) -> bool:
        return vertex == self.first or vertex == self.second

    def other(self, vertex: Vertex[T]) -> Vertex[T]:
        if vertex == self.first:
            return self.second
        if vertex == self.second:
            return self.first
        raise ValueError("Vertex is not part of the edge.")

    def __repr__(self) -> str:
        return f"Edge({self.first!r}, {self.second!r})"
