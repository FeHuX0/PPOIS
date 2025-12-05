from __future__ import annotations

from typing import Dict, List

from .EdgeIterator import EdgeIterator
from .Graph import Graph
from .Vertex import Vertex
from .VertexIterator import VertexIterator


class GraphDemo:
    """Simple demo harness for the graph container."""

    @staticmethod
    def build_sample_graph() -> Graph[str]:
        graph: Graph[str] = Graph()
        a = graph.add_vertex("A")
        b = graph.add_vertex("B")
        c = graph.add_vertex("C")
        d = graph.add_vertex("D")
        graph.add_edge(a, b)
        graph.add_edge(b, c)
        graph.add_edge(c, d)
        graph.add_edge(a, d)
        return graph

    @staticmethod
    def run() -> Dict[str, object]:
        graph = GraphDemo.build_sample_graph()
        vertex_iter = graph.vertices()
        edge_iter = graph.edges()

        vertex_names = [v.value for v in vertex_iter]
        edge_pairs = [(e.source.value, e.target.value) for e in edge_iter]

        # Demonstrate removal via iterators.
        removable_vertices = graph.vertices()
        graph.remove_vertex_by_iterator(removable_vertices)

        return {
            "graph": graph,
            "vertices": vertex_names,
            "edges": edge_pairs,
            "vertex_count_after_removal": graph.vertex_count(),
            "edge_count_after_removal": graph.edge_count(),
        }
