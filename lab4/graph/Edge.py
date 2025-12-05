from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Tuple, TypeVar

from .Vertex import Vertex

T = TypeVar("T")


@dataclass(frozen=True)
class Edge(Generic[T]):
    """Directed edge from source to target vertex."""

    source: Vertex[T]
    target: Vertex[T]

    def __post_init__(self) -> None:
        if self.source == self.target:
            raise ValueError("Self-loops are not allowed in this graph implementation.")

    @property
    def endpoints(self) -> Tuple[Vertex[T], Vertex[T]]:
        return self.source, self.target

    def connects(self, vertex: Vertex[T]) -> bool:
        """Check if edge connects to vertex (as source or target)."""
        return vertex == self.source or vertex == self.target

    def is_outgoing_from(self, vertex: Vertex[T]) -> bool:
        """Check if edge is outgoing from vertex."""
        return vertex == self.source

    def is_incoming_to(self, vertex: Vertex[T]) -> bool:
        """Check if edge is incoming to vertex."""
        return vertex == self.target

    def other(self, vertex: Vertex[T]) -> Vertex[T]:
        """Get the other vertex in the edge."""
        if vertex == self.source:
            return self.target
        if vertex == self.target:
            return self.source
        raise ValueError("Vertex is not part of the edge.")

    def __repr__(self) -> str:
        return f"Edge({self.source!r} -> {self.target!r})"
