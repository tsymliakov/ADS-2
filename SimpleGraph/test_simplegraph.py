from webbrowser import Grail
from simplegraph import *


# Test AddVertex

def test_addvertex_1():
    g = SimpleGraph(0)
    g.AddVertex(1)

    assert g.vertex == []
    assert g.m_adjacency == []


def test_addvertex_2():
    g = SimpleGraph(1)
    g.AddVertex(1)

    assert [v.Value for v in g.vertex] == [1]
    assert g.m_adjacency == [[0]]


def test_addvertex_3():
    g = SimpleGraph(1)
    g.AddVertex(1)
    g.AddVertex(2)

    assert [v.Value for v in g.vertex] == [1]
    assert g.m_adjacency == [[0]]


# Test AddEdge

def test_addedge_1():
    g = SimpleGraph(2)
    g.AddVertex(1)
    g.AddVertex(2)

    assert g.m_adjacency == [[0, 0], [0, 0]]

    g.AddEdge(0, 1)
    assert g.m_adjacency == [[0, 1], [1, 0]]

    g.AddEdge(0, 0)
    assert g.m_adjacency == [[1, 1], [1, 0]]


# Test RemoveEdge

def test_removeedge_1():
    g = SimpleGraph(2)
    g.AddVertex(1)
    g.AddVertex(2)

    g.RemoveEdge(0, 0)
    g.RemoveEdge(1, 1)
    g.RemoveEdge(1, 0)
    g.RemoveEdge(0, 1)

    assert g.m_adjacency == [[0, 0], [0, 0]]


def test_removeedge_2():
    g = SimpleGraph(2)
    g.AddVertex(1)
    g.AddVertex(2)

    assert g.m_adjacency == [[0, 0], [0, 0]]

    g.AddEdge(0, 1)
    g.AddEdge(1, 1)

    assert g.m_adjacency == [[0, 1], [1, 1]]

    g.RemoveEdge(1, 1)
    assert g.m_adjacency == [[0, 1], [1, 0]]

    g.RemoveEdge(1, 0)
    assert g.m_adjacency == [[0, 0], [0, 0]]

    g.AddEdge(1, 0)
    assert g.m_adjacency == [[0, 1], [1, 0]]

    g.RemoveEdge(0, 1)
    assert g.m_adjacency == [[0, 0], [0, 0]]


def test_removeedge_3():
    g = SimpleGraph(0)

    g.AddEdge(0, 0)


# Test isEdge

def test_isedge_1():
    g = SimpleGraph(0)

    assert g.IsEdge(0, 0) is None


def test_isedge_2():
    g = SimpleGraph(2)

    assert g.IsEdge(0, 0) is None


def test_isedge_3():
    g = SimpleGraph(2)

    g.AddVertex(1)
    g.AddVertex(2)

    assert g.IsEdge(0, 1) is False
    assert g.IsEdge(1, 0) is False

    g.AddEdge(0, 1)

    assert g.IsEdge(0, 1) is True
    assert g.IsEdge(1, 0) is True


# Test RemoveVertex

def test_removevertex_1():
    g = SimpleGraph(0)
    g.AddVertex(1)
    g.RemoveVertex(0)

    assert g.vertex == []
    assert g.m_adjacency == []


def test_removevertex_2():
    g = SimpleGraph(5)

    g.AddVertex('A')  # 0
    g.AddVertex('B')  # 1
    g.AddVertex('C')  # 2
    g.AddVertex('D')  # 3
    g.AddVertex('E')  # 4

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(0, 3)
    g.AddEdge(2, 3)
    g.AddEdge(1, 3)
    g.AddEdge(1, 4)
    g.AddEdge(3, 4)
    g.AddEdge(3, 3)

    assert g.m_adjacency == [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0]
    ]

    g.RemoveVertex(0)

    assert g.IsEdge(0, 1) is None
    assert g.IsEdge(0, 2) is None
    assert g.IsEdge(0, 3) is None

    assert g.m_adjacency == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0]
    ]
