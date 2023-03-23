from balanced_tree import *


def test_generate_tree_1():
    tree = BalancedBST()
    simple_keys = [3, 1, 2]

    tree.GenerateTree(simple_keys)

    root = tree.Root
    left = root.LeftChild
    right = root.RightChild

    assert root.NodeKey == 2
    assert left.NodeKey == 1
    assert right.NodeKey == 3

    assert root.Parent is None
    assert left.Parent is root
    assert right.Parent is root

    assert root.Level == 0
    assert left.Level == 1
    assert right.Level == 1


def test_generate_tree_2():
    tree = BalancedBST()

    tree.GenerateTree([1])

    assert tree.Root.NodeKey == 1


def test_generate_tree_3():
    tree = BalancedBST()

    tree.GenerateTree([])

    assert tree.Root is None


# def test_generate_tree_4():
#     tree = BalancedBST()

#     keys = [1, 1, 1, 1, 1, 1]

#     tree.GenerateTree([1, 1, 1, 1, 1, 1])

#     curr_node = tree.Root.RightChild
#     nodes = 1

#     while curr_node is not None:
#         assert curr_node.Level == curr_node.Parent.Level + 1
#         assert curr_node.LeftChild is None
#         nodes += 1
#         curr_node = curr_node.RightChild

#     assert nodes == len(keys) - 1


# Test IsBalanced

def test_balanced_1():
    keys = [3, 2, 1]
    tree = BalancedBST()
    tree.GenerateTree(keys)

    assert tree.IsBalanced(tree.Root) == True