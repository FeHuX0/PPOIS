import pytest

from graph.AdjacentVertexIterator import AdjacentVertexIterator
from graph.Edge import Edge
from graph.EdgeIterator import EdgeIterator
from graph.Graph import Graph
from graph.GraphDemo import GraphDemo
from graph.IncidentEdgeIterator import IncidentEdgeIterator
from graph.Vertex import Vertex
from graph.VertexIterator import VertexIterator
from sort.BinaryTreeSort import BinaryTreeSort
from sort.MSDRadixSort import MSDRadixSort
from sort.Person import Person
from sort.SortDemo import SortDemo


# ==================== BinaryTreeSort Tests ====================

def test_binary_tree_sort_sorted_and_reverse():
    data = [1, 2, 3, 4]
    BinaryTreeSort.sort(data)
    assert data == [1, 2, 3, 4]

    BinaryTreeSort.sort(data, reverse=True)
    assert data == [4, 3, 2, 1]


def test_binary_tree_sort_with_key_on_custom_type():
    people = [
        Person(name="Alice", age=32, score=4.0),
        Person(name="Bob", age=28, score=4.5),
        Person(name="Charlie", age=30, score=3.5),
    ]
    BinaryTreeSort.sort(people, key=lambda p: p.score)
    assert [p.name for p in people] == ["Charlie", "Alice", "Bob"]

    BinaryTreeSort.sort(people, key=lambda p: p.age, reverse=True)
    assert [p.age for p in people] == [32, 30, 28]


def test_binary_tree_sort_empty_and_single():
    empty = []
    BinaryTreeSort.sort(empty)
    assert empty == []

    single = [42]
    BinaryTreeSort.sort(single)
    assert single == [42]


def test_binary_tree_sort_duplicates():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    BinaryTreeSort.sort(data)
    assert data == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


def test_binary_tree_sort_negative_numbers():
    data = [-5, 3, -1, 0, 2, -3]
    BinaryTreeSort.sort(data)
    assert data == [-5, -3, -1, 0, 2, 3]

    BinaryTreeSort.sort(data, reverse=True)
    assert data == [3, 2, 0, -1, -3, -5]


def test_binary_tree_sort_without_key():
    data = [5, 2, 8, 1, 9]
    BinaryTreeSort.sort(data)
    assert data == [1, 2, 5, 8, 9]


# ==================== MSDRadixSort Tests ====================

def test_msd_radix_sort_with_key_and_reverse():
    words = ["alpha", "beta", "gamma", "d"]
    original = list(words)
    MSDRadixSort.sort(words, key=len)
    # After sorting by length: "d" (1), "beta" (4), "alpha" (5), "gamma" (5)
    # Note: MSD Radix Sort on integers, so words with same length may be in any order
    lengths = [len(w) for w in words]
    assert lengths == sorted(lengths)

    MSDRadixSort.sort(words, reverse=True)
    assert words == sorted(original, reverse=True)


def test_msd_radix_sort_strings():
    words = ["banana", "apple", "cherry", "date"]
    MSDRadixSort.sort(words)
    assert words == ["apple", "banana", "cherry", "date"]


def test_msd_radix_sort_strings_reverse():
    words = ["apple", "banana", "cherry"]
    MSDRadixSort.sort(words, reverse=True)
    assert words == ["cherry", "banana", "apple"]


def test_msd_radix_sort_strings_different_lengths():
    words = ["a", "abc", "ab", "abcd", "aa"]
    MSDRadixSort.sort(words)
    assert words == ["a", "aa", "ab", "abc", "abcd"]


def test_msd_radix_sort_integers():
    numbers = [42, 5, 17, 3, 99, 1]
    MSDRadixSort.sort(numbers)
    assert numbers == [1, 3, 5, 17, 42, 99]


def test_msd_radix_sort_integers_reverse():
    numbers = [42, 5, 17, 3, 99, 1]
    MSDRadixSort.sort(numbers, reverse=True)
    assert numbers == [99, 42, 17, 5, 3, 1]


def test_msd_radix_sort_integers_negative():
    numbers = [-5, 3, -1, 0, 2, -3]
    MSDRadixSort.sort(numbers)
    assert numbers == [-5, -3, -1, 0, 2, 3]


def test_msd_radix_sort_integers_negative_reverse():
    numbers = [-5, 3, -1, 0, 2, -3]
    MSDRadixSort.sort(numbers, reverse=True)
    # For reverse=True: positives sorted high to low, then negatives sorted high to low by value (-1 > -3 > -5)
    assert numbers == [3, 2, 0, -1, -3, -5]


def test_msd_radix_sort_integers_zeros():
    numbers = [0, 0, 0]
    MSDRadixSort.sort(numbers)
    assert numbers == [0, 0, 0]


def test_msd_radix_sort_empty_and_single():
    empty = []
    MSDRadixSort.sort(empty)
    assert empty == []

    single = [42]
    MSDRadixSort.sort(single)
    assert single == [42]


def test_msd_radix_sort_mixed_types():
    # Should convert to string (first element determines type, so use string first)
    data = ["123", 45, "abc"]
    original_len = len(data)
    MSDRadixSort.sort(data, key=str)
    # After string conversion, should still have same length
    assert len(data) == original_len


def test_msd_radix_sort_with_key_function():
    words = ["hello", "hi", "world", "a"]
    MSDRadixSort.sort(words, key=len)
    lengths = [len(w) for w in words]
    assert lengths == sorted(lengths)


# ==================== SortDemo Tests ====================

def test_sort_demo_runs():
    result = SortDemo.run()
    assert result["numbers"] == sorted(result["numbers"])
    assert result["words"] == sorted(result["words"])
    assert [p.name for p in result["people"]] == ["Bob", "Charlie", "Alice"]


# ==================== Graph Core Tests ====================

def test_graph_core_operations_and_iterators():
    graph: Graph[str] = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    vc = graph.add_vertex("C")

    edge_ab = graph.add_edge(va, vb)
    edge_bc = graph.add_edge(vb, vc)

    assert graph.has_vertex("A")
    assert graph.has_edge(va, vb)  # Directed edge from va to vb
    assert graph.vertex_count() == 3
    assert graph.edge_count() == 2
    # For directed graph: vb has 1 incoming (from va) and 1 outgoing (to vc)
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


def test_graph_init_with_vertices():
    vertices = [Vertex(1), Vertex(2), Vertex(3)]
    graph = Graph(vertices)
    assert graph.vertex_count() == 3


def test_graph_len():
    graph = Graph()
    assert len(graph) == 0
    graph.add_vertex(1)
    assert len(graph) == 1


def test_graph_iter():
    graph = Graph([Vertex(1), Vertex(2), Vertex(3)])
    vertices = list(graph)
    assert len(vertices) == 3
    assert all(isinstance(v, Vertex) for v in vertices)


def test_graph_reversed():
    graph = Graph([Vertex(1), Vertex(2), Vertex(3)])
    vertices = list(reversed(graph))
    assert len(vertices) == 3


def test_graph_eq():
    g1 = Graph([Vertex(1), Vertex(2)])
    g1.add_edge(1, 2)
    g2 = Graph([Vertex(1), Vertex(2)])
    g2.add_edge(1, 2)
    assert g1 == g2

    g3 = Graph([Vertex(1)])
    assert g1 != g3

    # Test with non-Graph object
    assert g1 != "not a graph"


def test_graph_comparisons():
    g1 = Graph([Vertex(1)])
    g2 = Graph([Vertex(1), Vertex(2)])
    g2.add_edge(1, 2)

    assert g1 != g2
    assert g1 < g2
    assert g2 > g1
    assert g1 <= g2
    assert g2 >= g1

    # Test with non-Graph object - should raise TypeError
    with pytest.raises(TypeError):
        _ = g1 < "not a graph"
    with pytest.raises(TypeError):
        _ = g1 <= "not a graph"
    with pytest.raises(TypeError):
        _ = g1 > "not a graph"
    with pytest.raises(TypeError):
        _ = g1 >= "not a graph"


def test_graph_str():
    graph = Graph()
    assert "Graph(vertices=[" in str(graph)
    assert "edges=[" in str(graph)

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")
    graph_str = str(graph)
    assert "A" in graph_str
    assert "B" in graph_str
    assert "->" in graph_str


def test_graph_empty():
    graph = Graph()
    assert graph.empty()
    graph.add_vertex(1)
    assert not graph.empty()


def test_graph_clear():
    graph = Graph([Vertex(1), Vertex(2)])
    graph.add_edge(1, 2)
    graph.clear()
    assert graph.empty()
    assert graph.vertex_count() == 0
    assert graph.edge_count() == 0


def test_graph_has_vertex():
    graph = Graph()
    graph.add_vertex("A")
    assert graph.has_vertex("A")
    assert graph.has_vertex(Vertex("A"))
    assert not graph.has_vertex("B")


def test_graph_has_edge():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    graph.add_edge(va, vb)

    assert graph.has_edge(va, vb)
    assert graph.has_edge("A", "B")
    assert not graph.has_edge(vb, va)  # Directed graph
    assert not graph.has_edge("A", "C")


def test_graph_degrees():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    vc = graph.add_vertex("C")
    graph.add_edge(va, vb)  # A -> B
    graph.add_edge(vb, vc)  # B -> C
    graph.add_edge(vc, va)  # C -> A

    assert graph.out_degree(va) == 1
    assert graph.in_degree(va) == 1
    assert graph.degree_vertex(va) == 2

    assert graph.out_degree(vb) == 1
    assert graph.in_degree(vb) == 1
    assert graph.degree_vertex(vb) == 2


def test_graph_add_vertex_existing():
    graph = Graph()
    v1 = graph.add_vertex("A")
    v2 = graph.add_vertex("A")  # Should return same vertex
    assert v1 == v2
    assert graph.vertex_count() == 1


def test_graph_add_edge_existing():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    edge1 = graph.add_edge(va, vb)
    edge2 = graph.add_edge(va, vb)  # Should return same edge
    assert edge1 == edge2
    assert graph.edge_count() == 1


def test_graph_remove_vertex():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    vc = graph.add_vertex("C")
    graph.add_edge(va, vb)
    graph.add_edge(vb, vc)
    graph.add_edge(vc, va)

    graph.remove_vertex(vb)
    assert graph.vertex_count() == 2
    assert graph.edge_count() == 1  # Only vc -> va remains


def test_graph_remove_edge_by_vertices():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    graph.add_edge(va, vb)
    graph.remove_edge(va, vb)
    assert graph.edge_count() == 0


def test_graph_remove_edge_by_edge_object():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    edge = graph.add_edge(va, vb)
    graph.remove_edge(edge)
    assert graph.edge_count() == 0


def test_graph_remove_edge_not_found():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    vc = graph.add_vertex("C")
    graph.add_edge(va, vb)

    with pytest.raises(ValueError):
        graph.remove_edge(vb, va)  # Reverse edge doesn't exist

    with pytest.raises(ValueError):
        graph.remove_edge(va, vc)  # Edge doesn't exist


def test_graph_outgoing_incoming_edges():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    vc = graph.add_vertex("C")
    graph.add_edge(va, vb)
    graph.add_edge(va, vc)
    graph.add_edge(vb, va)

    outgoing = list(graph.outgoing_edges(va))
    assert len(outgoing) == 2

    incoming = list(graph.incoming_edges(va))
    assert len(incoming) == 1


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


def test_graph_degree_edge_not_in_graph():
    graph = Graph()
    va = graph.add_vertex("A")
    vb = graph.add_vertex("B")
    edge = Edge(va, vb)

    with pytest.raises(ValueError):
        graph.degree_edge(edge)


def test_graph_remove_edge_invalid_args():
    graph = Graph()
    # When source is not an Edge and target is None, should raise ValueError
    with pytest.raises(ValueError, match="Edge not found"):
        graph.remove_edge("A")  # No second argument and not an Edge


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


def test_graph_demo_run():
    result = GraphDemo.run()
    assert "graph" in result
    assert result["vertex_count_after_removal"] <= 3
    assert result["edge_count_after_removal"] <= 4


# ==================== Edge Tests ====================

def test_edge_creation():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edge = Edge(v1, v2)
    assert edge.source == v1
    assert edge.target == v2


def test_edge_self_loop():
    v1 = Vertex(1)
    with pytest.raises(ValueError):
        Edge(v1, v1)


def test_edge_endpoints():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edge = Edge(v1, v2)
    endpoints = edge.endpoints
    assert endpoints == (v1, v2)


def test_edge_connects():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    edge = Edge(v1, v2)
    assert edge.connects(v1)
    assert edge.connects(v2)
    assert not edge.connects(v3)


def test_edge_is_outgoing_from():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edge = Edge(v1, v2)
    assert edge.is_outgoing_from(v1)
    assert not edge.is_outgoing_from(v2)


def test_edge_is_incoming_to():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edge = Edge(v1, v2)
    assert edge.is_incoming_to(v2)
    assert not edge.is_incoming_to(v1)


def test_edge_other():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edge = Edge(v1, v2)
    assert edge.other(v1) == v2
    assert edge.other(v2) == v1

    v3 = Vertex(3)
    with pytest.raises(ValueError):
        edge.other(v3)


def test_edge_repr():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edge = Edge(v1, v2)
    repr_str = repr(edge)
    assert "Edge" in repr_str
    assert "->" in repr_str


# ==================== Vertex Tests ====================

def test_vertex_creation():
    v = Vertex(42)
    assert v.value == 42


def test_vertex_repr():
    v = Vertex("test")
    repr_str = repr(v)
    assert "Vertex" in repr_str
    assert "test" in repr_str


# ==================== Iterator Tests ====================

def test_vertex_iterator():
    vertices = [Vertex(1), Vertex(2), Vertex(3)]
    iterator = VertexIterator(vertices)

    assert list(iterator) == vertices
    # Create a new iterator for reversed iteration
    iterator2 = VertexIterator(vertices)
    assert list(reversed(iterator2)) == list(reversed(vertices))

    # Test iteration reset
    iterator2 = VertexIterator(vertices)
    assert next(iterator2) == vertices[0]
    iterator2.__iter__()
    assert next(iterator2) == vertices[0]


def test_vertex_iterator_stop_iteration():
    iterator = VertexIterator([Vertex(1)])
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


def test_edge_iterator():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    edges = [Edge(v1, v2), Edge(v2, v3)]
    iterator = EdgeIterator(edges)

    assert list(iterator) == edges
    # Create a new iterator for reversed iteration
    iterator2 = EdgeIterator(edges)
    assert list(reversed(iterator2)) == list(reversed(edges))


def test_edge_iterator_stop_iteration():
    v1 = Vertex(1)
    v2 = Vertex(2)
    iterator = EdgeIterator([Edge(v1, v2)])
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


def test_incident_edge_iterator():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    edges = [Edge(v1, v2), Edge(v2, v3), Edge(v3, v1)]
    iterator = IncidentEdgeIterator(v2, edges)

    incident = list(iterator)
    assert len(incident) == 2  # v1->v2 and v2->v3

    # Create a new iterator for reversed iteration
    iterator2 = IncidentEdgeIterator(v2, edges)
    assert list(reversed(iterator2)) == list(reversed(incident))


def test_incident_edge_iterator_stop_iteration():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    edges = [Edge(v1, v2)]
    iterator = IncidentEdgeIterator(v2, edges)
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


def test_adjacent_vertex_iterator():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    edges = [Edge(v1, v2), Edge(v2, v3), Edge(v3, v1)]
    iterator = AdjacentVertexIterator(v2, edges)

    adjacent = list(iterator)
    assert len(adjacent) == 2  # v1 and v3

    # Create a new iterator for reversed iteration
    iterator2 = AdjacentVertexIterator(v2, edges)
    assert list(reversed(iterator2)) == list(reversed(adjacent))


def test_adjacent_vertex_iterator_stop_iteration():
    v1 = Vertex(1)
    v2 = Vertex(2)
    edges = [Edge(v1, v2)]
    iterator = AdjacentVertexIterator(v2, edges)
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


# ==================== Person Tests ====================

def test_person_creation():
    person = Person(name="Alice", age=30, score=4.5)
    assert person.name == "Alice"
    assert person.age == 30
    assert person.score == 4.5


def test_person_repr():
    person = Person(name="Bob", age=25, score=3.8)
    repr_str = repr(person)
    assert "Person" in repr_str
    assert "Bob" in repr_str
    assert "25" in repr_str


def test_person_ordering():
    p1 = Person(name="Alice", age=30, score=4.0)
    p2 = Person(name="Bob", age=25, score=4.5)
    # Person is ordered by age (first field in dataclass)
    assert p2 < p1  # 25 < 30
