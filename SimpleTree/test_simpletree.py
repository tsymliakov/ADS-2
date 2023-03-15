from simpletree import SimpleTree, SimpleTreeNode


def create_tree_for_tests():
    pass


def test_create_simpletree():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    assert tree.Root is root
    assert root.Parent is None
    assert root.NodeValue == 1


def test_add_level_1_child():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_2_lvl_1 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)

    assert child_1_lvl_1 in tree.Root.Children
    assert child_2_lvl_1 in tree.Root.Children

    assert child_1_lvl_1.Parent is root
    assert child_2_lvl_1.Parent is root


def test_add_level_2_child():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_lvl_1 = SimpleTreeNode(1)
    child_lvl_2 = SimpleTreeNode(1)

    tree.AddChild(root, child_lvl_1)
    tree.AddChild(child_lvl_1, child_lvl_2)

    assert child_lvl_1.Parent is root
    assert child_lvl_2.Parent is child_lvl_1


def test_get_children_empty():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    assert len(tree._get_all_child(root)) == 0


def test_get_children_normal():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)

    assert len(tree._get_all_child(root)) == 2


def test_get_children_bigger():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_2_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)
    child_2_lvl_2 = SimpleTreeNode(1)
    child_3_lvl_2 = SimpleTreeNode(1)
    child_1_lvl_3 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)
    tree.AddChild(child_1_lvl_1, child_2_lvl_2)
    tree.AddChild(child_1_lvl_1, child_3_lvl_2)
    tree.AddChild(child_1_lvl_2, child_1_lvl_3)

    founded_nodes = tree._get_all_child(root)
    assert set(founded_nodes).discard({child_1_lvl_1, child_2_lvl_1, child_1_lvl_2, child_2_lvl_2,
                                       child_3_lvl_2, child_1_lvl_3}) is None


def test_get_children_of_children():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_2_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)
    child_2_lvl_2 = SimpleTreeNode(1)
    child_3_lvl_2 = SimpleTreeNode(1)
    child_1_lvl_3 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)
    tree.AddChild(child_1_lvl_1, child_2_lvl_2)
    tree.AddChild(child_1_lvl_1, child_3_lvl_2)
    tree.AddChild(child_1_lvl_2, child_1_lvl_3)

    founded_nodes = tree._get_all_child(child_1_lvl_1)
    assert set(founded_nodes).discard({child_1_lvl_2, child_2_lvl_2, child_3_lvl_2,
                                       child_1_lvl_3}) is None


def test_check_children_immutability():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_2_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)
    child_2_lvl_2 = SimpleTreeNode(1)
    child_3_lvl_2 = SimpleTreeNode(1)
    child_1_lvl_3 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)
    tree.AddChild(child_1_lvl_1, child_2_lvl_2)
    tree.AddChild(child_1_lvl_1, child_3_lvl_2)
    tree.AddChild(child_1_lvl_2, child_1_lvl_3)

    tree._get_all_child(root)

    assert set(root.Children) == set([child_1_lvl_1, child_2_lvl_1])
    assert set(child_1_lvl_1.Children) == set([child_1_lvl_2, child_2_lvl_2, child_3_lvl_2])
    assert set(child_1_lvl_2.Children) == {child_1_lvl_3}
    assert len(child_2_lvl_2.Children) == 0
    assert len(child_3_lvl_2.Children) == 0
    assert len(child_1_lvl_3.Children) == 0


# def test_delete():
#     root = SimpleTreeNode(5, None)
#     tree = SimpleTree(root)

#     child_lvl_1 = SimpleTreeNode(1)
#     child_lvl_2 = SimpleTreeNode(1)

#     tree.AddChild(root, child_lvl_1)
#     tree.AddChild(child_lvl_1, child_lvl_2)

