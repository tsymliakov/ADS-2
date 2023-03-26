from heap import *


# Test MakeHeap

def test_makeheap_1():
    h = Heap()

    h.MakeHeap([], 0)
    assert h.HeapArray == [None]

    h.MakeHeap([], 1)
    assert h.HeapArray == [None, None, None]


def test_makeheap_2():
    h = Heap()
    h.MakeHeap([1, 2, 3], 1)

    assert h.HeapArray == [3, 1, 2]


def test_makeheap_3():
    h = Heap()
    h.MakeHeap([1, 2, 3, 4, 5, 6], 2)

    # Не самый хороший тест ввиду того, что порядок дочерних элементов
    # любого из узлов кучи не определен. Так что при изменени внутренней
    # реализации класса или всего- то порядка следования значений в
    # входном массиве, подобные тесты могут начать выдавать
    # ложноотрицательный результат
    assert h.HeapArray == [6, 4, 5, 1, 3, 2, None]


def test_makeheap_4():
    h = Heap()
    h.MakeHeap([3, 2, 1, 4, 6, 5], 2)

    assert h.HeapArray == [6, 4, 5, 2, 3, 1, None]


def test_makeheap_5():
    h = Heap()
    h.MakeHeap([1, 1, 1, 1], 2)

    assert h.HeapArray == [1, 1, 1, 1, None, None, None]


def test_makeheap_6():
    h = Heap()
    h.MakeHeap([2, 1, 2, 1], 2)

    assert h.HeapArray == [2, 1, 2, 1, None, None, None]


# Test GetMax

def test_getmax_1():
    h = Heap()

    h.MakeHeap([], 0)
    assert h.GetMax() == -1

    h.MakeHeap([], 1)
    assert h.GetMax() == -1


def test_getmax_2():
    h = Heap()
    h.MakeHeap([1, 2, 3], 1)

    assert h.GetMax() == 3
    assert h.HeapArray == [2, 1, None]

    assert h.GetMax() == 2
    assert h.HeapArray == [1, None, None]

    assert h.GetMax() == 1
    assert h.HeapArray == [None, None, None]

    assert h.GetMax() == -1
    assert h.HeapArray == [None, None, None]
    print()


def test_getmax_3():
    h = Heap()
    h.MakeHeap([2, 1, 2, 1], 2)

    assert h.GetMax() == 2
    assert h.GetMax() == 2
    assert h.GetMax() == 1
    assert h.GetMax() == 1
    assert h.HeapArray == [None, None, None, None, None, None, None]


# Test Add

def test_add_1():
    h = Heap()
    h.MakeHeap([], 0)

    h.Add(5)

    assert h.HeapArray == [5]
    assert h.LastKey == 0


def test_add_2():
    h = Heap()
    h.MakeHeap([], 0)

    h.Add(5)
    h.Add(9)

    assert h.LastKey == 0


def test_add_3():
    h = Heap()
    h.MakeHeap([], 1)

    h.Add(5)
    h.Add(9)
    h.Add(4)

    assert h.LastKey == 2
    assert h.HeapArray == [9, 5, 4]


def test_add_4():
    h = Heap()
    h.MakeHeap([], 2)

    h.Add(0)
    h.Add(4)
    h.Add(6)
    h.Add(3)
    h.Add(2)
    h.Add(1)
    h.Add(5)

    assert h.Add(101) == False
    assert h.LastKey == 6
    assert h.HeapArray == [6, 3, 5, 0, 2, 1, 4]
