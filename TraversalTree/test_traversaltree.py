from traversaltree import *


# Test wide

def test_wide_empty():
    tree = TraversalBST(None)
    assert tree.WideAllNodes() == ()


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


def test_wide_2():
    tree = TraversalBST(BSTNode(10, 1, None))
    tree.AddKeyValue(5, 1)
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(0, 1)
    tree.AddKeyValue(20, 1)
    tree.AddKeyValue(-5, 1)

    assert tree._height(tree.Root) == 4
    nodes_keys = (10, 5, 15, 0, 20, -5)
    traversaled_nodes = tree.WideAllNodes()

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_wide_3():
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


# Test deep

def test_deep_in_order_empty():
    tree = TraversalBST(None)
    assert tree.DeepAllNodes(0) == ()


def test_deep_in_order_root():
    root = BSTNode(10, 1, None)
    tree = TraversalBST(root)
    assert tree.DeepAllNodes(0) == (root,)


def test_deep_in_order_1():
    tree = TraversalBST(BSTNode(8, 1, None))
    tree.AddKeyValue(4, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(2, 1)
    tree.AddKeyValue(6, 1)
    tree.AddKeyValue(10, 1)
    tree.AddKeyValue(14, 1)

    nodes_keys = (2, 4, 6, 8, 10, 12, 14)
    traversaled_nodes = tree.DeepAllNodes(0)

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_deep_in_order_2():
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

    nodes_keys = (3, 6, 12, 20, 22, 25, 30, 40,
                  50, 60, 75, 90, 95, 98, 100, 101)
    traversaled_nodes = tree.DeepAllNodes(0)

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_deep_post_order_1():
    tree = TraversalBST(BSTNode(10, 1, None))
    tree.AddKeyValue(5, 1)
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(2, 1)
    tree.AddKeyValue(7, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(17, 1)

    nodes_keys = (2, 7, 5, 12, 17, 15, 10)

    traversaled_nodes = tree.DeepAllNodes(1)

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_deep_post_order_2():
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

    nodes_keys = (3, 6, 22, 20, 12, 30, 40, 25,
                  60, 98, 95, 90, 75, 50, 101, 100)
    traversaled_nodes = tree.DeepAllNodes(1)

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_deep_pre_order_1():
    tree = TraversalBST(BSTNode(10, 1, None))
    tree.AddKeyValue(5, 1)
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(2, 1)
    tree.AddKeyValue(7, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(17, 1)

    nodes_keys = (10, 5, 2, 7, 15, 12, 17)

    traversaled_nodes = tree.DeepAllNodes(2)

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey


def test_deep_pre_order_2():
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

    nodes_keys = (100, 50, 25, 12, 6, 3, 20, 22,
                  40, 30, 75, 60, 90, 95, 98, 101)
    traversaled_nodes = tree.DeepAllNodes(2)

    for i, key in enumerate(nodes_keys):
        assert key == traversaled_nodes[i].NodeKey
