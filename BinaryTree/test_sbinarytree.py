from sbinarytree import *


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

    return {'tree' : tree, 'nodes' : nodes}


def test_FindNodeByKey_all_nodes():
    tree_nodes = give_tree_and_nodes()
    tree : BST = tree_nodes['tree']
    nodes = tree_nodes['nodes']
    r_lc = nodes['r_lc'] # 4
    r_rc = nodes['r_rc'] # 12
    r_lc_lc = nodes['r_lc_lc'] # 2
    r_lc_rc = nodes['r_lc_rc'] # 6
    r_rc_lc = nodes['r_rc_lc'] # 10
    r_rc_rc = nodes['r_rc_rc'] # 14

    assert tree.FindNodeByKey(8).Node is tree.Root
    assert tree.FindNodeByKey(4).Node is r_lc
    assert tree.FindNodeByKey(12).Node is r_rc
    assert tree.FindNodeByKey(2).Node is r_lc_lc
    assert tree.FindNodeByKey(6).Node is r_lc_rc
    assert tree.FindNodeByKey(10).Node is r_rc_lc
    assert tree.FindNodeByKey(14).Node is r_rc_rc


def test_FindNodeByKey_all_possible_leafs_withot_swaping_childs():
    tree_nodes = give_tree_and_nodes()
    tree : BST = tree_nodes['tree']
    nodes = tree_nodes['nodes']
    r_lc = nodes['r_lc'] # 4
    r_rc = nodes['r_rc'] # 12
    r_lc_lc = nodes['r_lc_lc'] # 2
    r_lc_rc = nodes['r_lc_rc'] # 6
    r_rc_lc = nodes['r_rc_lc'] # 10
    r_rc_rc = nodes['r_rc_rc'] # 14

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



