from dfs_graph import *


def test_get_related_1():
    g = SimpleGraph(2)
    g.AddVertex(1)
    g.AddVertex(2)

    g.AddEdge(0, 1)

    assert g._get_related_vertexes(0) == [1]


def test_get_related_2():
    g = SimpleGraph(5)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(0, 3)
    g.AddEdge(2, 3)
    g.AddEdge(1, 3)
    g.AddEdge(1, 4)
    g.AddEdge(3, 4)
    g.AddEdge(3, 3)

    assert g._get_related_vertexes(0) == [1, 2, 3]
    assert g._get_related_vertexes(1) == [0, 3, 4]
    assert g._get_related_vertexes(2) == [0, 3]
    assert g._get_related_vertexes(3) == [0, 1, 2, 3, 4]
    assert g._get_related_vertexes(4) == [1, 3]


def test_dfs_1():
    g = SimpleGraph(2)
    g.AddVertex(1)
    g.AddVertex(2)

    g.AddEdge(0, 1)

    assert g.DepthFirstSearch(2, 3) == []


def test_dfs_2():
    g = SimpleGraph(5)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(0, 3)
    g.AddEdge(2, 3)
    g.AddEdge(1, 3)
    g.AddEdge(1, 4)
    g.AddEdge(3, 4)
    g.AddEdge(3, 3)

    assert g.DepthFirstSearch(0, 3) == [g.vertex[0], g.vertex[3]]
    assert g.DepthFirstSearch(0, 4) == [g.vertex[0], g.vertex[1], g.vertex[4]]
    assert g.DepthFirstSearch(3, 3) == [g.vertex[3], g.vertex[3]]
    assert g.DepthFirstSearch(3, 1) == [g.vertex[3], g.vertex[1]]


def test_dfs_3():
    g = SimpleGraph(5)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)

    g.AddEdge(3, 4)

    assert g.DepthFirstSearch(0, 3) == []
    assert g.DepthFirstSearch(4, 1) == []


def test_dfs_4():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 3)
    g.AddEdge(4, 1)
    g.AddEdge(4, 5)

    assert g.DepthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5],
    ]


def test_dfs_5():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 3)

    assert g.DepthFirstSearch(0, 3) == [g.vertex[0], g.vertex[1], g.vertex[3]]


def test_dfs_additional():
    g = SimpleGraph(5)

    g.AddVertex(0)  # A
    g.AddVertex(1)  # B
    g.AddVertex(2)  # C
    g.AddVertex(3)  # D
    g.AddVertex(4)  # E

    g.AddEdge(0, 1)
    g.AddEdge(0, 3)
    g.AddEdge(0, 2)
    g.AddEdge(1, 3)
    g.AddEdge(2, 3)
    g.AddEdge(1, 4)
    g.AddEdge(3, 4)
    g.AddEdge(3, 3)

    g.AddEdge(1, 0)

    assert g.DepthFirstSearch(0, 4) == [g.vertex[0], g.vertex[1], g.vertex[4]]
    assert g.DepthFirstSearch(0, 1) == [g.vertex[0], g.vertex[1]]
    assert g.DepthFirstSearch(0, 3) == [g.vertex[0], g.vertex[3]]
    assert g.DepthFirstSearch(0, 2) == [g.vertex[0], g.vertex[2]]
    assert g.DepthFirstSearch(2, 1) == [g.vertex[2], g.vertex[0], g.vertex[1]]
