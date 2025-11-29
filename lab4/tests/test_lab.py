import pytest

from graph.Graph import Graph
from graph.GraphDemo import GraphDemo
from graph.Vertex import Vertex
from sort.Person import Person
from sort.SimplePancakeSort import SimplePancakeSort
from sort.Smoothsort import Smoothsort
from sort.SortDemo import SortDemo


def test_smoothsort_sorted_and_reverse():
    data = [1, 2, 3, 4]
    Smoothsort.sort(data)  # already sorted triggers adaptive fast path
    assert data == [1, 2, 3, 4]

    Smoothsort.sort(data, reverse=True)
    assert data == [4, 3, 2, 1]


def test_smoothsort_with_key_on_custom_type():
    people = [
        Person(name="Alice", age=32, score=4.0),
        Person(name="Bob", age=28, score=4.5),
        Person(name="Charlie", age=30, score=3.5),
    ]
    Smoothsort.sort(people, key=lambda p: p.score)
    assert [p.name for p in people] == ["Charlie", "Alice", "Bob"]

    Smoothsort.sort(people, key=lambda p: p.age, reverse=True)
    assert [p.age for p in people] == [32, 30, 28]


def test_pancake_sort_with_key_and_reverse():
    words = ["alpha", "beta", "gamma", "d"]
    original = list(words)
    SimplePancakeSort.sort(words, key=len)
    assert [len(w) for w in words] == sorted([len(w) for w in words])

    SimplePancakeSort.sort(words, reverse=True)
    assert words == sorted(original, reverse=True)


def test_sort_demo_runs():
    result = SortDemo.run()
    assert result["numbers"] == sorted(result["numbers"])
    assert result["words"] == sorted(result["words"])
    assert [p.name for p in result["people"]] == ["Bob", "Charlie", "Alice"]


def test_graph_core_operations_and_iterators():
    graph: Graph[str] = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    vc = graph.add_vertex("C")

    edge_ab = graph.add_edge(va, vb)
    edge_bc = graph.add_edge(vb, vc)

    assert graph.has_vertex("A")
    assert graph.has_edge(va, vb)
    assert graph.vertex_count() == 3
    assert graph.edge_count() == 2
    assert graph.degree_vertex(vb) == 2
    assert graph.degree_edge(edge_ab) == 1  # each endpoint has degree 1 other than this edge

    # iterators forward and reverse
    assert set(v.value for v in graph.vertices()) == {"A", "B", "C"}
    assert list(reversed(graph.vertices()))
    assert list(graph.incident_edges(vb))
    assert list(graph.adjacent_vertices(vb))

    # removal via iterators
    graph.remove_edge_by_iterator(graph.edges())
    assert graph.edge_count() == 1
    graph.remove_vertex_by_iterator(graph.vertices())
    assert graph.vertex_count() == 2


def test_graph_comparisons_and_str():
    g1 = Graph([Vertex(1)])
    g2 = Graph([Vertex(1), Vertex(2)])
    g2.add_edge(1, 2)

    assert g1 != g2
    assert g1 < g2
    assert g2 > g1
    assert g1 <= g2
    assert g2 >= g1
    assert "Graph(vertices" in str(g1)


def test_graph_exceptions_and_clear():
    graph: Graph[int] = Graph()
    graph.add_vertex(1)
    with pytest.raises(ValueError):
        graph.remove_vertex(2)
    with pytest.raises(ValueError):
        graph.add_edge(1, 1)

    graph.clear()
    assert graph.empty()

    with pytest.raises(ValueError):
        graph.remove_edge_by_iterator(graph.edges())
    with pytest.raises(ValueError):
        graph.remove_vertex_by_iterator(graph.vertices())


def test_graph_demo_run():
    result = GraphDemo.run()
    assert "graph" in result
    assert result["vertex_count_after_removal"] <= 3
    assert result["edge_count_after_removal"] <= 4
