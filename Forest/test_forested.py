from forested_tree import *


def test_adj_list_1():
    node1 = SimpleTreeNode(1)
    tree = SimpleTree(node1)

    assert tree.EvenTrees() == []


def test_adj_list_2():
    node1 = SimpleTreeNode(1)
    tree = SimpleTree(node1)

    node2 = SimpleTreeNode(2)
    node3 = SimpleTreeNode(3)
    node4 = SimpleTreeNode(4)
    node5 = SimpleTreeNode(5)
    node6 = SimpleTreeNode(6)
    node7 = SimpleTreeNode(7)
    node8 = SimpleTreeNode(8)
    node9 = SimpleTreeNode(9)
    node10 = SimpleTreeNode(10)


    tree.AddChild(node1, node2)
    tree.AddChild(node1, node3)
    tree.AddChild(node1, node6)
    tree.AddChild(node2, node5)
    tree.AddChild(node2, node7)
    tree.AddChild(node3, node4)
    tree.AddChild(node6, node8)
    tree.AddChild(node8, node9)
    tree.AddChild(node8, node10)

    links = tree.AdjacencyList(node1)
    right_result = [node1, node2, node2, node5, node2, node7, node1, node3,
                    node3, node4, node1, node6, node6, node8, node8, node9,
                    node8, node10]

    assert links == right_result


def test_adj_list_2():
    node1 = SimpleTreeNode(1)
    tree = SimpleTree(node1)

    node2 = SimpleTreeNode(2)
    node3 = SimpleTreeNode(3)
    node4 = SimpleTreeNode(4)

    tree.AddChild(node1, node2)
    tree.AddChild(node1, node3)
    tree.AddChild(node3, node4)

    links = tree.AdjacencyList(node3)
    right_result = [node3, node4]

    assert links == right_result


def test_del_edge_1():
    nodeA = SimpleTreeNode('A')
    tree = SimpleTree(nodeA)

    nodeB = SimpleTreeNode('B')
    nodeC = SimpleTreeNode('C')
    # nodeD = SimpleTreeNode('D')
    # nodeE = SimpleTreeNode('E')
    # nodeF = SimpleTreeNode('F')

    tree.AddChild(nodeA, nodeB)
    tree.AddChild(nodeB, nodeC)

    l_adj = tree.AdjacencyList(nodeA)
    b = tree._get_subtrees(l_adj, nodeA, nodeB)
    print()
