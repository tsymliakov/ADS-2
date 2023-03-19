from sbinarytree import *


# It would be better to replace this function with a class with tree and
# nodes attribute
def give_tree_and_nodes():
    root = BSTNode(8, 1, None)
    tree = BST(root)

    r_lc = BSTNode(4, 1, root)
    r_rc = BSTNode(12, 1, root)

    root.LeftChild = r_lc
    root.RightChild = r_rc

    r_lc_lc = BSTNode(2, 1, r_lc)
    r_lc_rc = BSTNode(6, 1, r_lc)

    r_lc.LeftChild = r_lc_lc
    r_lc.RightChild = r_lc_rc

    r_rc_lc = BSTNode(10, 1, r_rc)
    r_rc_rc = BSTNode(14, 1, r_rc)

    r_rc.LeftChild = r_rc_lc
    r_rc.RightChild = r_rc_rc

    nodes = dict()
    nodes['r_lc'] = r_lc
    nodes['r_rc'] = r_rc
    nodes['r_lc_lc'] = r_lc_lc
    nodes['r_lc_rc'] = r_lc_rc
    nodes['r_rc_lc'] = r_rc_lc
    nodes['r_rc_rc'] = r_rc_rc

    return {'tree': tree, 'nodes': nodes}


# Test FindKey
def test_FindNodeByKey_empty():
    tree = BST(None)

    search_res = tree.FindNodeByKey(1)

    assert isinstance(search_res, BSTFind)
    assert search_res.Node is None


def test_FindNodeByKey_all_nodes():
    tree_nodes = give_tree_and_nodes()
    tree: BST = tree_nodes['tree']
    nodes = tree_nodes['nodes']
    r_lc = nodes['r_lc']  # 4
    r_rc = nodes['r_rc']  # 12
    r_lc_lc = nodes['r_lc_lc']  # 2
    r_lc_rc = nodes['r_lc_rc']  # 6
    r_rc_lc = nodes['r_rc_lc']  # 10
    r_rc_rc = nodes['r_rc_rc']  # 14

    assert tree.FindNodeByKey(8).Node is tree.Root
    assert tree.FindNodeByKey(4).Node is r_lc
    assert tree.FindNodeByKey(12).Node is r_rc
    assert tree.FindNodeByKey(2).Node is r_lc_lc
    assert tree.FindNodeByKey(6).Node is r_lc_rc
    assert tree.FindNodeByKey(10).Node is r_rc_lc
    assert tree.FindNodeByKey(14).Node is r_rc_rc


def test_FindNodeByKey_all_possible_leafs_withot_swaping_childs():
    tree_nodes = give_tree_and_nodes()
    tree: BST = tree_nodes['tree']
    nodes = tree_nodes['nodes']
    r_lc = nodes['r_lc']  # 4
    r_rc = nodes['r_rc']  # 12
    r_lc_lc = nodes['r_lc_lc']  # 2
    r_lc_rc = nodes['r_lc_rc']  # 6
    r_rc_lc = nodes['r_rc_lc']  # 10
    r_rc_rc = nodes['r_rc_rc']  # 14

    result_bstfind = tree.FindNodeByKey(1)
    assert result_bstfind.Node is r_lc_lc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is True

    result_bstfind = tree.FindNodeByKey(3)
    assert result_bstfind.Node is r_lc_lc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is False

    result_bstfind = tree.FindNodeByKey(5)
    assert result_bstfind.Node is r_lc_rc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is True

    result_bstfind = tree.FindNodeByKey(7)
    assert result_bstfind.Node is r_lc_rc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is False

    result_bstfind = tree.FindNodeByKey(9)
    assert result_bstfind.Node is r_rc_lc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is True

    result_bstfind = tree.FindNodeByKey(11)
    assert result_bstfind.Node is r_rc_lc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is False

    result_bstfind = tree.FindNodeByKey(13)
    assert result_bstfind.Node is r_rc_rc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is True

    result_bstfind = tree.FindNodeByKey(15)
    assert result_bstfind.Node is r_rc_rc
    assert result_bstfind.NodeHasKey is False
    assert result_bstfind.ToLeft is False


# Test AddKeyValue
def test_addkey_empty():
    tree = BST(None)
    tree.AddKeyValue(key=5, val=10)

    assert tree.Root.NodeKey == 5
    assert tree.Root.NodeValue == 10
    assert tree.Root.Parent is None
    assert tree.Root.LeftChild is None
    assert tree.Root.RightChild is None


def test_addkey_left_right():
    root = BSTNode(5, 10, None)
    tree = BST(root)

    tree.AddKeyValue(3, 10)
    tree.AddKeyValue(7, 10)

    assert root.LeftChild.NodeKey == 3
    assert root.RightChild.NodeKey == 7


def test_addkey_left_exists():
    root = BSTNode(5, 10, None)
    tree = BST(root)

    tree.AddKeyValue(3, 10)
    left_root_child = root.LeftChild

    tree.AddKeyValue(3, 5)

    assert root.LeftChild.NodeValue == 10
    assert left_root_child is root.LeftChild


def test_addkey_right_exists():
    root = BSTNode(5, 10, None)
    tree = BST(root)

    tree.AddKeyValue(7, 10)
    right_root_child = root.RightChild

    tree.AddKeyValue(7, 5)

    assert root.RightChild.NodeValue == 10
    assert right_root_child is root.RightChild


def test_addkey_complex_1():
    tree = BST(None)

    for i in range(0, 4):
        tree.AddKeyValue(i, 5)

    assert tree.Root.NodeKey == 0
    assert tree.Root.RightChild.NodeKey == 1
    assert tree.Root.RightChild.RightChild.NodeKey == 2
    assert tree.Root.RightChild.RightChild.RightChild.NodeKey == 3


def test_addkey_complex_2():
    tree = BST(None)

    for i in range(3, -1, -1):
        tree.AddKeyValue(i, 5)

    assert tree.Root.NodeKey == 3
    assert tree.Root.LeftChild.NodeKey == 2
    assert tree.Root.LeftChild.LeftChild.NodeKey == 1
    assert tree.Root.LeftChild.LeftChild.LeftChild.NodeKey == 0


# Test FinMinMax
def test_find_min_from_root():
    tree_nodes = give_tree_and_nodes()
    tree = tree_nodes['tree']

    min_key_node = tree.FinMinMax(tree.Root, False)
    assert min_key_node.NodeKey == 2


def test_find_max_from_root():
    tree_nodes = give_tree_and_nodes()
    tree = tree_nodes['tree']

    min_key_node = tree.FinMinMax(tree.Root, True)
    assert min_key_node.NodeKey == 14


def test_find_min_in_subtree():
    tree_nodes = give_tree_and_nodes()
    tree = tree_nodes['tree']
    nodes = tree_nodes['nodes']

    min_key_node = tree.FinMinMax(nodes['r_lc'], False)
    assert min_key_node.NodeKey == 2


def test_find_max_in_subtree():
    tree_nodes = give_tree_and_nodes()
    tree = tree_nodes['tree']
    nodes = tree_nodes['nodes']

    min_key_node = tree.FinMinMax(nodes['r_lc'], True)
    assert min_key_node.NodeKey == 6


# Test Count
def test_count_empty():
    tree = BST(None)

    assert tree.Count() == 0


def test_count_only_root():
    root = BSTNode(1, 1, None)
    tree = BST(root)

    assert tree.Count() == 1


def test_count_1():
    tree = give_tree_and_nodes()['tree']

    assert tree.Count() == 7


def test_count_2():
    tree = BST(None)
    for i in range(100):
        tree.AddKeyValue(i, 1)

    assert tree.Count() == 100


# Test DeleteNodeByKey
def test_delete_root():
    tree_nodes = give_tree_and_nodes()
    tree : BST = tree_nodes['tree']

    tree.DeleteNodeByKey(8)
    assert tree.Root is None


def test_delete_no_child():
    tree_nodes = give_tree_and_nodes()
    tree : BST = tree_nodes['tree']
    nodes = tree_nodes['nodes']

    count_before = tree.Count()

    tree.DeleteNodeByKey(2)
    assert tree.Count() == count_before - 1
    assert nodes['r_lc'].LeftChild is None
    assert nodes['r_lc'].RightChild is nodes['r_lc_rc']
    assert nodes['r_lc'].Parent is tree.Root
    assert nodes['r_lc_rc'].Parent is nodes['r_lc']


def test_delete_only_right_child():
    tree = BST(BSTNode(10, 1, None))
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(18, 1)
    tree.AddKeyValue(16, 1)
    tree.AddKeyValue(20, 1)

    del_node = tree.FindNodeByKey(15).Node
    child = tree.FindNodeByKey(18).Node

    count_before = tree.Count()

    assert del_node.Parent is tree.Root
    assert del_node.LeftChild is None
    assert del_node.RightChild is child
    assert child.Parent is del_node

    tree.DeleteNodeByKey(15)

    assert tree.Count() == count_before - 1
    assert tree.Root.RightChild is child
    assert child.Parent is tree.Root
    assert tree.FindNodeByKey(20).NodeHasKey is True
    assert tree.FindNodeByKey(16).NodeHasKey is True


def test_delete_only_left_child():
    tree = BST(BSTNode(10, 1, None))
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(13, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(14, 1)

    del_node = tree.FindNodeByKey(15).Node
    child = tree.FindNodeByKey(13).Node

    count_before = tree.Count()

    assert del_node.Parent is tree.Root
    assert del_node.RightChild is None
    assert del_node.LeftChild is child
    assert child.Parent is del_node

    tree.DeleteNodeByKey(15)

    assert tree.Count() == count_before - 1
    assert tree.Root.RightChild is child
    assert child.Parent is tree.Root
    assert tree.FindNodeByKey(12).NodeHasKey is True
    assert tree.FindNodeByKey(14).NodeHasKey is True


def test_delete_all_two_child_1():
    tree = BST(BSTNode(10, 1, None))
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(17, 1)

    node_12 = tree.FindNodeByKey(12).Node
    print(repr(node_12))
    node_17 = tree.FindNodeByKey(17).Node

    tree.DeleteNodeByKey(15)

    assert tree.Root.RightChild is node_17
    assert node_17.Parent is tree.Root

    assert node_17.LeftChild is node_12
    assert node_12.Parent is node_17


def test_delete_all_two_child_2():
    tree = BST(BSTNode(10, 1, None))
    tree.AddKeyValue(15, 1)
    tree.AddKeyValue(12, 1)
    tree.AddKeyValue(17, 1)
    tree.AddKeyValue(16, 1)
    tree.AddKeyValue(18, 1)

    node_12 = tree.FindNodeByKey(12).Node
    node_16 = tree.FindNodeByKey(16).Node
    node_17 = tree.FindNodeByKey(17).Node
    node_18 = tree.FindNodeByKey(18).Node

    tree.DeleteNodeByKey(15)

    assert tree.Root.RightChild is node_16
    assert node_16.Parent is tree.Root
    assert node_16.LeftChild is node_12
    assert node_12.Parent is node_16
    assert node_16.RightChild is node_17
    assert node_17.Parent is node_16
    assert node_17.LeftChild is None
    assert node_17.RightChild is node_18
    assert node_18.Parent is node_17
