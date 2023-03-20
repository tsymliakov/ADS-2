from traversaltree import *


def test_wide_only_root():
    root = BSTNode(10, 1, None)
    tree = TraversalBST(root)
    assert tree.WideAllNodes() == (root,)


def test_wide_1():
    tree = TraversalBST(BSTNode(8, 1, None))
    tree.AddKeyValue(4, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(2, 1)
    tree.AddKeyValue(6, 1)
    tree.AddKeyValue(10, 1)
    tree.AddKeyValue(14, 1)

    nodes_keys = (8, 4, 12, 2, 6, 10, 14)
    traversaled_nodes = tree.WideAllNodes()

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_wide_3():
    tree = TraversalBST(BSTNode(10, 1, None))
    tree.AddKeyValue(5, 1)
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(0, 1)
    tree.AddKeyValue(20, 1)
    tree.AddKeyValue(-5, 1)

    nodes_keys = (10, 5, 15, 0, 20, -5)
    traversaled_nodes = tree.WideAllNodes()

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey

def test_wide_4():
    tree = TraversalBST(BSTNode(100, 1, None))
    tree.AddKeyValue(50, 1)
    tree.AddKeyValue(101, 1)
    tree.AddKeyValue(25, 1)
    tree.AddKeyValue(75, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(40, 1)
    tree.AddKeyValue(60, 1)
    tree.AddKeyValue(90, 1)
    tree.AddKeyValue(95, 1)
    tree.AddKeyValue(98, 1)
    tree.AddKeyValue(30, 1)
    tree.AddKeyValue(20, 1)
    tree.AddKeyValue(22, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(6, 1)
    tree.AddKeyValue(3, 1)

    nodes_keys = (100, 50, 101, 25, 75, 12, 40,
                  60, 90, 6, 20, 30, 95, 3, 22, 98)
    traversaled_nodes = tree.WideAllNodes()

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey
