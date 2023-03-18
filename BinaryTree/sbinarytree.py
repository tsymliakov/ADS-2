from http import server
from multiprocessing import Value
from platform import node
from re import search
from tkinter import N
from tkinter.messagebox import NO
from xmlrpc.client import Boolean


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()

        return self._recursive_node_search(self.Root, key)

    def _recursive_node_search(self, node: BSTNode, key):
        if key == node.NodeKey:
            search_result = BSTFind()
            search_result.Node = node
            search_result.NodeHasKey = True
            return search_result
        if key < node.NodeKey:
            if node.LeftChild is not None:
                return self._recursive_node_search(node.LeftChild, key)
            search_result = BSTFind()
            search_result.Node = node
            search_result.ToLeft = True
            return search_result
        if node.RightChild is not None:
            return self._recursive_node_search(node.RightChild, key)
        search_result = BSTFind()
        search_result.Node = node
        return search_result

    def AddKeyValue(self, key, val):
        search_result = self.FindNodeByKey(key)

        if search_result.Node is None:
            self.Root = BSTNode(key, val, None)
            return True

        # Если нашлась нода с таким же ключом- не делаем ничего
        if search_result.NodeHasKey is True:
            return False

        child_node = BSTNode(key, val, search_result.Node)

        if search_result.ToLeft:
            search_result.Node.LeftChild = child_node
            return True

        search_result.Node.RightChild = child_node
        return True

    def FinMinMax(self, FromNode, FindMax: Boolean):
        if not isinstance(FromNode, BSTNode):
            return None
        curr_node = FromNode

        if FindMax is False:
            while curr_node is not None:
                if curr_node.LeftChild is None:
                    return curr_node
                curr_node = curr_node.LeftChild
        while curr_node is not None:
            if curr_node.RightChild is None:
                return curr_node
            curr_node = curr_node.RightChild

    def DeleteNodeByKey(self, key):
        return False

    def Count(self):
        if self.Root is None:
            return 0
        root_node = 1
        return self._count(self.Root) + root_node

    def _count(self, node):
        nodes = 0

        if node.LeftChild is not None:
            nodes += 1
            nodes += self._count(node.LeftChild)
        if node.RightChild is not None:
            nodes += 1
            nodes += self._count(node.RightChild)
        return nodes
