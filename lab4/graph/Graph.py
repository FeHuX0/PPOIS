from __future__ import annotations

from typing import Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar

from .AdjacentVertexIterator import AdjacentVertexIterator
from .Edge import Edge
from .EdgeIterator import EdgeIterator
from .IncidentEdgeIterator import IncidentEdgeIterator
from .Vertex import Vertex
from .VertexIterator import VertexIterator

T = TypeVar("T")


class Graph(Generic[T]):
    """Undirected graph container using a modified Wirth-style adjacency store."""

    value_type = Vertex[T]
    reference = Vertex[T]
    const_reference = Vertex[T]
    pointer = Vertex[T]

    def __init__(self, vertices: Optional[Iterable[Vertex[T]]] = None) -> None:
        self._adjacency: Dict[Vertex[T], Dict[Vertex[T], Edge[T]]] = {}
        self._edges: Set[Edge[T]] = set()
        if vertices:
            for vertex in vertices:
                self.add_vertex(vertex)

    def __len__(self) -> int:
        return self.vertex_count()

    def __iter__(self) -> Iterator[Vertex[T]]:
        return iter(VertexIterator(self._adjacency.keys()))

    def __reversed__(self) -> Iterator[Vertex[T]]:
        return iter(reversed(VertexIterator(self._adjacency.keys())))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return False
        return self._adjacency == other._adjacency

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return (self.vertex_count(), self.edge_count()) < (
            other.vertex_count(),
            other.edge_count(),
        )

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return (self.vertex_count(), self.edge_count()) <= (
            other.vertex_count(),
            other.edge_count(),
        )

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return (self.vertex_count(), self.edge_count()) > (
            other.vertex_count(),
            other.edge_count(),
        )

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented
        return (self.vertex_count(), self.edge_count()) >= (
            other.vertex_count(),
            other.edge_count(),
        )

    def __str__(self) -> str:
        edges_repr = ", ".join(
            f"{edge.first.value}--{edge.second.value}" for edge in self._edges
        )
        vertices_repr = ", ".join(str(v.value) for v in self._adjacency.keys())
        return f"Graph(vertices=[{vertices_repr}], edges=[{edges_repr}])"

    def empty(self) -> bool:
        return not self._adjacency

    def clear(self) -> None:
        self._adjacency.clear()
        self._edges.clear()

    def _ensure_vertex(self, vertex_or_value: Vertex[T] | T) -> Vertex[T]:
        vertex = (
            vertex_or_value
            if isinstance(vertex_or_value, Vertex)
            else Vertex(vertex_or_value)
        )
        if vertex not in self._adjacency:
            raise ValueError("Vertex not found in graph.")
        return vertex

    def _canonical_edge(self, first: Vertex[T], second: Vertex[T]) -> Edge[T]:
        if repr(first) <= repr(second):
            return Edge(first, second)
        return Edge(second, first)

    def has_vertex(self, vertex_or_value: Vertex[T] | T) -> bool:
        return (
            vertex_or_value in self._adjacency
            if isinstance(vertex_or_value, Vertex)
            else Vertex(vertex_or_value) in self._adjacency
        )

    def has_edge(self, first: Vertex[T] | T, second: Vertex[T] | T) -> bool:
        if not self.has_vertex(first) or not self.has_vertex(second):
            return False
        v1 = self._ensure_vertex(first)
        v2 = self._ensure_vertex(second)
        return v2 in self._adjacency[v1]

    def vertex_count(self) -> int:
        return len(self._adjacency)

    def edge_count(self) -> int:
        return len(self._edges)

    def degree_vertex(self, vertex: Vertex[T] | T) -> int:
        v = self._ensure_vertex(vertex)
        return len(self._adjacency[v])

    def degree_edge(self, edge: Edge[T]) -> int:
        if edge not in self._edges:
            raise ValueError("Edge does not belong to this graph.")
        return (self.degree_vertex(edge.first) - 1) + (self.degree_vertex(edge.second) - 1)

    def add_vertex(self, vertex_or_value: Vertex[T] | T) -> Vertex[T]:
        vertex = (
            vertex_or_value
            if isinstance(vertex_or_value, Vertex)
            else Vertex(vertex_or_value)
        )
        if vertex in self._adjacency:
            return vertex
        self._adjacency[vertex] = {}
        return vertex

    def add_edge(self, first: Vertex[T] | T, second: Vertex[T] | T) -> Edge[T]:
        v1 = (
            first if isinstance(first, Vertex) else self.add_vertex(first)
        )  # ensure vertex exists
        v2 = (
            second if isinstance(second, Vertex) else self.add_vertex(second)
        )
        if v1 == v2:
            raise ValueError("Self-loops are not allowed.")
        edge = self._canonical_edge(v1, v2)
        if edge in self._edges:
            return edge
        self._edges.add(edge)
        self._adjacency[v1][v2] = edge
        self._adjacency[v2][v1] = edge
        return edge

    def remove_vertex(self, vertex: Vertex[T] | T) -> None:
        v = self._ensure_vertex(vertex)
        for neighbor in list(self._adjacency[v].keys()):
            self.remove_edge(v, neighbor)
        del self._adjacency[v]

    def remove_edge(
        self, first: Vertex[T] | T | Edge[T], second: Vertex[T] | T | Edge[T] | None = None
    ) -> None:
        if isinstance(first, Edge):
            edge = first
        elif isinstance(second, Edge):
            edge = second
        elif second is not None:
            v1 = self._ensure_vertex(first)  # type: ignore[arg-type]
            v2 = self._ensure_vertex(second)  # type: ignore[arg-type]
            edge = self._canonical_edge(v1, v2)
        else:
            raise ValueError("Edge not found.")
        if edge not in self._edges:
            raise ValueError("Edge not found.")
        self._edges.remove(edge)
        self._adjacency[edge.first].pop(edge.second, None)
        self._adjacency[edge.second].pop(edge.first, None)

    def remove_vertex_by_iterator(self, iterator: VertexIterator[T]) -> None:
        try:
            vertex = next(iterator)
        except StopIteration:
            raise ValueError("Iterator is exhausted.")
        self.remove_vertex(vertex)

    def remove_edge_by_iterator(self, iterator: EdgeIterator[T]) -> None:
        try:
            edge = next(iterator)
        except StopIteration:
            raise ValueError("Iterator is exhausted.")
        self.remove_edge(edge)

    def vertices(self) -> VertexIterator[T]:
        return VertexIterator(self._adjacency.keys())

    def edges(self) -> EdgeIterator[T]:
        return EdgeIterator(self._edges)

    def incident_edges(self, vertex: Vertex[T] | T) -> IncidentEdgeIterator[T]:
        v = self._ensure_vertex(vertex)
        return IncidentEdgeIterator(v, self._edges)

    def adjacent_vertices(self, vertex: Vertex[T] | T) -> AdjacentVertexIterator[T]:
        v = self._ensure_vertex(vertex)
        return AdjacentVertexIterator(v, self._edges)
