from forested_tree import *


def test_eventrees_1():
    node1 = SimpleTreeNode(1)
    tree = SimpleTree(node1)

    assert tree.EvenTrees() == []


def test_eventrees_2():
    node1 = SimpleTreeNode(1)
    node2 = SimpleTreeNode(2)
    node3 = SimpleTreeNode(3)
    node4 = SimpleTreeNode(4)

    tree = SimpleTree(node1)

    tree.AddChild(node1, node2)
    tree.AddChild(node2, node3)
    tree.AddChild(node3, node4)

    assert tree.EvenTrees() == [node2, node3]


def test_eventrees_3():
    node1 = SimpleTreeNode(1)
    node2 = SimpleTreeNode(2)
    node3 = SimpleTreeNode(3)
    node4 = SimpleTreeNode(4)
    node5 = SimpleTreeNode(5)
    node6 = SimpleTreeNode(6)

    tree = SimpleTree(node1)

    tree.AddChild(node1, node2)
    tree.AddChild(node2, node3)
    tree.AddChild(node3, node4)
    tree.AddChild(node4, node5)
    tree.AddChild(node5, node6)

    assert set(tree.EvenTrees()) == set([node2, node3, node4, node5])
