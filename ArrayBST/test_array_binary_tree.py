from array_binary_tree import *


# Test Add

def test_add_1():
    tree = aBST(0)
    tree.AddKey(5)

    assert tree.Tree == [5]


def test_add_2():
    tree = aBST(2)
    tree.AddKey(10)
    tree.AddKey(5)
    tree.AddKey(15)
    tree.AddKey(2)
    tree.AddKey(7)
    tree.AddKey(12)
    tree.AddKey(17)

    assert tree.Tree == [10, 5, 15, 2, 7, 12, 17]


def test_add_3():
    tree = aBST(3)
    assert tree.AddKey(50) == 0
    tree.AddKey(25)
    assert tree.AddKey(75) == 2
    tree.AddKey(37)
    assert tree.AddKey(62) == 5
    tree.AddKey(84)
    assert tree.AddKey(31) == 9
    tree.AddKey(43)
    assert tree.AddKey(55) == 11
    tree.AddKey(92)

    assert tree.Tree == [50, 25, 75, None, 37, 62,
                         84, None, None, 31, 43, 55, None, None, 92]


def test_add_4():
    tree = aBST(1)
    assert tree.AddKey(0) == 0
    assert tree.AddKey(5) == 2
    assert tree.AddKey(5) == 2


# Test Find

def test_find_1():
    tree = aBST(0)
    tree.AddKey(5)

    assert tree.FindKeyIndex(5) == 0
    assert tree.FindKeyIndex(1) is None


def test_find_2():
    tree = aBST(3)
    tree.AddKey(50)
    tree.AddKey(25)
    tree.AddKey(75)
    tree.AddKey(37)
    tree.AddKey(62)
    tree.AddKey(84)
    tree.AddKey(31)
    tree.AddKey(43)
    tree.AddKey(55)
    tree.AddKey(92)

    assert tree.FindKeyIndex(50) == 0
    assert tree.FindKeyIndex(25) == 1
    assert tree.FindKeyIndex(75) == 2
    assert tree.FindKeyIndex(37) == 4
    assert tree.FindKeyIndex(62) == 5
    assert tree.FindKeyIndex(84) == 6
    assert tree.FindKeyIndex(31) == 9
    assert tree.FindKeyIndex(43) == 10
    assert tree.FindKeyIndex(55) == 11
    assert tree.FindKeyIndex(92) == 14

    assert tree.FindKeyIndex(999) is None
    assert tree.FindKeyIndex(-999) == -3
