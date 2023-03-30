from wv_graph import *


"""
Граф с петлями
Граф с циклами
Граф с множественными ребрами
"""


def test_loops_no_weak():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 0)

    g.AddEdge(0, 0)
    g.AddEdge(1, 1)
    g.AddEdge(2, 2)

    assert g.WeakVertices() == []


def test_loops_all_weak():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)

    g.AddEdge(0, 0)
    g.AddEdge(1, 1)
    g.AddEdge(2, 2)

    assert g.WeakVertices() == [g.vertex[0], g.vertex[1], g.vertex[2]]


def test_simple_2():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)

    assert g.WeakVertices() == [g.vertex[0], g.vertex[1], g.vertex[2]]

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)

    assert g.WeakVertices() == [g.vertex[0], g.vertex[1], g.vertex[2]]

    g.AddEdge(0, 2)

    assert g.WeakVertices() == []


def test_cycle():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    g.AddEdge(1, 0)
    g.AddEdge(2, 0)
    g.AddEdge(3, 0)
    g.AddEdge(4, 0)

    assert g.WeakVertices() == [g.vertex[5]]

def test_only_one():
    g = SimpleGraph(1)

    g.AddVertex(0)

    assert g.WeakVertices() == [g.vertex[0]]


def test_2_graphs_only_one():
    g = SimpleGraph(2)

    g.AddVertex(0)
    g.AddVertex(1)

    assert g.WeakVertices() == [g.vertex[0], g.vertex[1]]


def test_graph_from_picture():
    g = SimpleGraph(9)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)
    g.AddVertex(6)
    g.AddVertex(7)
    g.AddVertex(8)

    g.AddEdge(0, 1)
    g.AddEdge(0, 3)
    g.AddEdge(1, 2)
    g.AddEdge(1, 3)
    g.AddEdge(2, 3)
    g.AddEdge(2, 4)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(5, 6)
    g.AddEdge(5, 7)
    g.AddEdge(6, 7)
    g.AddEdge(7, 8)

    assert g.WeakVertices() == [g.vertex[4], g.vertex[8]]


def test_multiple_edges():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(4, 5)

    g.AddEdge(5, 5)
    g.AddEdge(0, 0)
    g.AddEdge(4, 4)
    g.AddEdge(2, 2)

    assert g.WeakVertices() == [g.vertex[0], g.vertex[1], g.vertex[2]]


def test_multiple_edges_not_full():
    g = SimpleGraph(10)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(4, 5)

    g.AddEdge(5, 5)
    g.AddEdge(0, 0)
    g.AddEdge(4, 4)
    g.AddEdge(2, 2)

    assert g.WeakVertices() == [g.vertex[0], g.vertex[1], g.vertex[2]]
