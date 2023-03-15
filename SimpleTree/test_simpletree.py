from simpletree import SimpleTree, SimpleTreeNode


# Test creation and child addition
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


# Test GetAllNodes

def test_get_root():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    founded_nodes = tree.GetAllNodes()

    assert len(founded_nodes) == 1
    assert root in founded_nodes


def test_get_cont_nodes():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_lvl_1 = SimpleTreeNode(1)
    child_lvl_2 = SimpleTreeNode(1)
    child_lvl_3 = SimpleTreeNode(1)
    child_lvl_4 = SimpleTreeNode(1)
    child_lvl_5 = SimpleTreeNode(1)

    tree.AddChild(root, child_lvl_1)
    tree.AddChild(child_lvl_1, child_lvl_2)
    tree.AddChild(child_lvl_2, child_lvl_3)
    tree.AddChild(child_lvl_3, child_lvl_4)
    tree.AddChild(child_lvl_4, child_lvl_5)

    nodes = [
        root,
        child_lvl_1,
        child_lvl_2,
        child_lvl_3,
        child_lvl_4,
        child_lvl_5,
    ]

    founded_nodes = tree.GetAllNodes()

    assert len(founded_nodes) == len(nodes)
    
    for node in nodes:
        assert node in founded_nodes


# Test get children. Also tests GetAllNodes
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
    assert set(child_1_lvl_1.Children) == set(
        [child_1_lvl_2, child_2_lvl_2, child_3_lvl_2])
    assert set(child_1_lvl_2.Children) == {child_1_lvl_3}
    assert len(child_2_lvl_2.Children) == 0
    assert len(child_3_lvl_2.Children) == 0
    assert len(child_1_lvl_3.Children) == 0


# Test count leaf
def test_count_leaf_empty():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    assert tree.LeafCount() == 1


def test_count_leaf_2_cont_nodes():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)

    assert tree.LeafCount() == 1


def test_count_leaf_2_nodes_same_lvl():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_1_lvl_2)

    assert tree.LeafCount() == 2


def test_count_leaf_harder():
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

    assert tree.LeafCount() == 4


# Test count nodes
def test_count_root_only():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    assert tree.Count() == 1


def test_count_cont_nodes():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)

    assert tree.Count() == 3


def test_count_nodes_same_lvl():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_1_lvl_2 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_1_lvl_2)

    assert tree.Count() == 3


def test_count_harder():
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

    assert tree.Count() == 7


# Test FindNodesByValue

def test_root_has_value():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    assert tree.FindNodesByValue(1) == [root]


def test_root_hasnt_value():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    assert len(tree.FindNodesByValue(2)) == 0


def test_all_nodes_has_value():
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

    assert set(tree.FindNodesByValue(1)).discard({root, child_1_lvl_1, child_2_lvl_1,
                                                  child_1_lvl_2, child_2_lvl_2, child_3_lvl_2,
                                                  child_1_lvl_3}) == None


def test_half_nodes_has_value():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)
    child_2_lvl_1 = SimpleTreeNode(2)
    child_1_lvl_2 = SimpleTreeNode(1)
    child_2_lvl_2 = SimpleTreeNode(2)
    child_3_lvl_2 = SimpleTreeNode(1)
    child_1_lvl_3 = SimpleTreeNode(2)

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)
    tree.AddChild(child_1_lvl_1, child_2_lvl_2)
    tree.AddChild(child_1_lvl_1, child_3_lvl_2)
    tree.AddChild(child_1_lvl_2, child_1_lvl_3)

    assert set(tree.FindNodesByValue(1)).discard({root, child_1_lvl_1, child_1_lvl_2,
                                                  child_3_lvl_2}) == None


# Test delete

def test_delete_root():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    tree.DeleteNode(root)

    assert tree.Root is root
    assert tree.Root.NodeValue == 1


def test_delete_node_simple():
    root = SimpleTreeNode(1)
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode(1)

    tree.AddChild(root, child_1_lvl_1)
    tree.DeleteNode(child_1_lvl_1)

    assert tree.GetAllNodes() == [root]


def test_delete_all_nodes():
    root = SimpleTreeNode('root')
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode('1_1')
    child_2_lvl_1 = SimpleTreeNode('2_1')
    child_1_lvl_2 = SimpleTreeNode('1_2')
    child_2_lvl_2 = SimpleTreeNode('2_2')
    child_3_lvl_2 = SimpleTreeNode('3_2')
    child_1_lvl_3 = SimpleTreeNode('1_3')

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)
    tree.AddChild(child_1_lvl_1, child_2_lvl_2)
    tree.AddChild(child_1_lvl_1, child_3_lvl_2)
    tree.AddChild(child_1_lvl_2, child_1_lvl_3)

    for child in tree.Root.Children:
        tree.DeleteNode(child)

    assert tree.Count() == 1
    assert tree.GetAllNodes()[0] is root


def test_delete_half_nodes():
    root = SimpleTreeNode('root')
    tree = SimpleTree(root)

    child_1_lvl_1 = SimpleTreeNode('1_1')
    child_2_lvl_1 = SimpleTreeNode('2_1')
    child_1_lvl_2 = SimpleTreeNode('1_2')
    child_2_lvl_2 = SimpleTreeNode('2_2')
    child_3_lvl_2 = SimpleTreeNode('3_2')
    child_1_lvl_3 = SimpleTreeNode('1_3')
    child_2_lvl_3 = SimpleTreeNode('2_3')
    child_3_lvl_3 = SimpleTreeNode('3_3')

    tree.AddChild(root, child_1_lvl_1)
    tree.AddChild(root, child_2_lvl_1)
    tree.AddChild(child_1_lvl_1, child_1_lvl_2)
    tree.AddChild(child_1_lvl_1, child_2_lvl_2)
    tree.AddChild(child_1_lvl_1, child_3_lvl_2)
    tree.AddChild(child_1_lvl_2, child_1_lvl_3)
    tree.AddChild(child_2_lvl_2, child_2_lvl_3)
    tree.AddChild(child_2_lvl_2, child_3_lvl_3)

    tree.DeleteNode(child_2_lvl_2)

    nodes_must_stay = [
        root,
        child_1_lvl_1,
        child_2_lvl_1,
        child_1_lvl_2,
        child_3_lvl_2,
        child_1_lvl_3
    ]

    nodes_after_deletion = tree.GetAllNodes()

    assert len(nodes_must_stay) == len(nodes_after_deletion)

    for node in nodes_must_stay:
        assert node in nodes_after_deletion
