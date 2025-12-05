from __future__ import annotations

from typing import Generic, Iterable, Iterator, List, Optional, Set, TypeVar

from .AdjacentVertexIterator import AdjacentVertexIterator
from .Edge import Edge
from .EdgeIterator import EdgeIterator
from .IncidentEdgeIterator import IncidentEdgeIterator
from .Vertex import Vertex
from .VertexIterator import VertexIterator

T = TypeVar("T")


class Graph(Generic[T]):
    """Directed graph container using ordered edge lists."""

    value_type = Vertex[T]
    reference = Vertex[T]
    const_reference = Vertex[T]
    pointer = Vertex[T]

    def __init__(self, vertices: Optional[Iterable[Vertex[T]]] = None) -> None:
        self._vertices: Set[Vertex[T]] = set()
        self._edges: List[Edge[T]] = []  # Ordered list of edges
        if vertices:
            for vertex in vertices:
                self.add_vertex(vertex)

    def __len__(self) -> int:
        return self.vertex_count()

    def __iter__(self) -> Iterator[Vertex[T]]:
        return iter(VertexIterator(self._vertices))

    def __reversed__(self) -> Iterator[Vertex[T]]:
        return iter(reversed(VertexIterator(self._vertices)))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return False
        return self._vertices == other._vertices and self._edges == other._edges

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
            f"{edge.source.value}->{edge.target.value}" for edge in self._edges
        )
        vertices_repr = ", ".join(str(v.value) for v in self._vertices)
        return f"Graph(vertices=[{vertices_repr}], edges=[{edges_repr}])"

    def empty(self) -> bool:
        return not self._vertices

    def clear(self) -> None:
        self._vertices.clear()
        self._edges.clear()

    def _ensure_vertex(self, vertex_or_value: Vertex[T] | T) -> Vertex[T]:
        vertex = (
            vertex_or_value
            if isinstance(vertex_or_value, Vertex)
            else Vertex(vertex_or_value)
        )
        if vertex not in self._vertices:
            raise ValueError("Vertex not found in graph.")
        return vertex

    def has_vertex(self, vertex_or_value: Vertex[T] | T) -> bool:
        return (
            vertex_or_value in self._vertices
            if isinstance(vertex_or_value, Vertex)
            else Vertex(vertex_or_value) in self._vertices
        )

    def has_edge(self, source: Vertex[T] | T, target: Vertex[T] | T) -> bool:
        """Check if there is a directed edge from source to target."""
        if not self.has_vertex(source) or not self.has_vertex(target):
            return False
        v1 = self._ensure_vertex(source)
        v2 = self._ensure_vertex(target)
        return any(e.source == v1 and e.target == v2 for e in self._edges)

    def vertex_count(self) -> int:
        return len(self._vertices)

    def edge_count(self) -> int:
        return len(self._edges)

    def out_degree(self, vertex: Vertex[T] | T) -> int:
        """Get the out-degree of a vertex (number of outgoing edges)."""
        v = self._ensure_vertex(vertex)
        return sum(1 for e in self._edges if e.source == v)

    def in_degree(self, vertex: Vertex[T] | T) -> int:
        """Get the in-degree of a vertex (number of incoming edges)."""
        v = self._ensure_vertex(vertex)
        return sum(1 for e in self._edges if e.target == v)

    def degree_vertex(self, vertex: Vertex[T] | T) -> int:
        """Get the total degree (in-degree + out-degree) of a vertex."""
        return self.in_degree(vertex) + self.out_degree(vertex)

    def degree_edge(self, edge: Edge[T]) -> int:
        """Get the sum of degrees of edge endpoints minus 2."""
        # Check if edge exists in graph by comparing source and target
        if not any(e.source == edge.source and e.target == edge.target for e in self._edges):
            raise ValueError("Edge does not belong to this graph.")
        return (self.degree_vertex(edge.source) - 1) + (self.degree_vertex(edge.target) - 1)

    def add_vertex(self, vertex_or_value: Vertex[T] | T) -> Vertex[T]:
        vertex = (
            vertex_or_value
            if isinstance(vertex_or_value, Vertex)
            else Vertex(vertex_or_value)
        )
        if vertex in self._vertices:
            return vertex
        self._vertices.add(vertex)
        return vertex

    def add_edge(self, source: Vertex[T] | T, target: Vertex[T] | T) -> Edge[T]:
        """Add a directed edge from source to target."""
        v1 = (
            source if isinstance(source, Vertex) else self.add_vertex(source)
        )  # ensure vertex exists
        v2 = (
            target if isinstance(target, Vertex) else self.add_vertex(target)
        )
        if v1 == v2:
            raise ValueError("Self-loops are not allowed.")
        edge = Edge(v1, v2)
        # Check if edge already exists
        if any(e.source == v1 and e.target == v2 for e in self._edges):
            return edge
        self._edges.append(edge)  # Add to ordered list
        return edge

    def remove_vertex(self, vertex: Vertex[T] | T) -> None:
        v = self._ensure_vertex(vertex)
        # Remove all edges connected to this vertex
        self._edges = [e for e in self._edges if e.source != v and e.target != v]
        self._vertices.remove(v)

    def remove_edge(
        self, source: Vertex[T] | T | Edge[T], target: Vertex[T] | T | Edge[T] | None = None
    ) -> None:
        if isinstance(source, Edge):
            edge = source
        elif isinstance(target, Edge):
            edge = target
        elif target is not None:
            v1 = self._ensure_vertex(source)  # type: ignore[arg-type]
            v2 = self._ensure_vertex(target)  # type: ignore[arg-type]
            edge = Edge(v1, v2)
        else:
            raise ValueError("Edge not found.")
        # Remove first occurrence of the edge
        for i, e in enumerate(self._edges):
            if e.source == edge.source and e.target == edge.target:
                self._edges.pop(i)
                return
        raise ValueError("Edge not found.")

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
        return VertexIterator(self._vertices)

    def edges(self) -> EdgeIterator[T]:
        return EdgeIterator(self._edges)

    def incident_edges(self, vertex: Vertex[T] | T) -> IncidentEdgeIterator[T]:
        """Get all edges incident to vertex (both incoming and outgoing)."""
        v = self._ensure_vertex(vertex)
        return IncidentEdgeIterator(v, self._edges)

    def outgoing_edges(self, vertex: Vertex[T] | T) -> IncidentEdgeIterator[T]:
        """Get all outgoing edges from vertex."""
        v = self._ensure_vertex(vertex)
        outgoing = [e for e in self._edges if e.is_outgoing_from(v)]
        return IncidentEdgeIterator(v, outgoing)

    def incoming_edges(self, vertex: Vertex[T] | T) -> IncidentEdgeIterator[T]:
        """Get all incoming edges to vertex."""
        v = self._ensure_vertex(vertex)
        incoming = [e for e in self._edges if e.is_incoming_to(v)]
        return IncidentEdgeIterator(v, incoming)

    def adjacent_vertices(self, vertex: Vertex[T] | T) -> AdjacentVertexIterator[T]:
        """Get all adjacent vertices (both targets of outgoing and sources of incoming edges)."""
        v = self._ensure_vertex(vertex)
        return AdjacentVertexIterator(v, self._edges)
