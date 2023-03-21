# I don't use imports because the test environment can react
# unpredictably to them
from turtle import left


class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def __repr__(self):
        return (f'Node {self.NodeKey}')


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

        # Если нашлась нода с таким же ключом- следуя условию задания не делаем ничего
        if search_result.NodeHasKey is True:
            return False

        child_node = BSTNode(key, val, search_result.Node)

        if search_result.ToLeft:
            search_result.Node.LeftChild = child_node
            return True

        search_result.Node.RightChild = child_node
        return True

    def FinMinMax(self, FromNode, FindMax: bool):
        if not isinstance(FromNode, BSTNode):
            return None

        curr_node = FromNode

        def get_next(node, FindMax):
            if FindMax:
                return node.RightChild
            return node.LeftChild

        while curr_node is not None:
            next = get_next(curr_node, FindMax)
            if next is None:
                return curr_node
            curr_node = next

        return curr_node

    def DeleteNodeByKey(self, key):
        search_result = self.FindNodeByKey(key)
        if not search_result.NodeHasKey:
            return False

        if search_result.Node is self.Root:
            self.Root = None
            return True

        removable_node: BSTNode = search_result.Node

        if not removable_node.LeftChild:
            if not removable_node.RightChild:
                self._remove_child_from_parent(removable_node)
                return True
            self._move_node(removable_node.RightChild, removable_node.Parent)
            return True

        if removable_node.RightChild:
            r_child_subtree_min_key = self.FinMinMax(
                removable_node.RightChild, False)

            # Найденная нода может иметь либо 0 потомков, либо потомка
            # справа (иначе нашлась бы другая нода с меньшим значением)
            if r_child_subtree_min_key.RightChild is None:
                self._move_node(r_child_subtree_min_key, removable_node.Parent)
                self._move_node(removable_node.LeftChild,
                                r_child_subtree_min_key)
                self._move_node(removable_node.RightChild,
                                r_child_subtree_min_key)
                return True

            self._move_node(r_child_subtree_min_key.RightChild,
                            r_child_subtree_min_key.Parent)
            self._move_node(r_child_subtree_min_key, removable_node.Parent)
            self._move_node(removable_node.RightChild, r_child_subtree_min_key)
            self._move_node(removable_node.LeftChild, r_child_subtree_min_key)
            return True

        self._move_node(removable_node.LeftChild, removable_node.Parent)

    def _move_node(self, node_to_move, parent):
        '''Вырежет node_to_move из дерева из её родителя и присоединит к
        parent на основании ключа.'''
        if node_to_move is None:
            return
        is_left = node_to_move.NodeKey < parent.NodeKey
        self._remove_child_from_parent(node_to_move)
        node_to_move.Parent = parent
        if is_left:
            parent.LeftChild = node_to_move
            return
        parent.RightChild = node_to_move

    def _remove_child_from_parent(self, child):
        '''Обрезает все связи child с его родительской нодой'''
        if child is None:
            return
        parent = child.Parent
        child.Parent = None
        if parent.LeftChild is child:
            parent.LeftChild = None
            return
        if parent.RightChild is child:
            parent.RightChild = None
            return

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


class TraversalBST(BST):
    def WideAllNodes(self) -> tuple[BSTNode]:
        """Производит обход всего дерева в ширину."""
        if not self.Root:
            return ()
        h = self._height(self.Root)

        nodes = [self.Root]

        for lvl in range(1, h):
            nodes.extend(self._add_nodes_of_lvl(self.Root, 1, lvl))

        return tuple(nodes)

    def _add_nodes_of_lvl(self, node, curr_lvl, need_lvl):
        if not node:
            return []
        if curr_lvl == need_lvl:
            nodes_same_lvl = []
            if node.LeftChild:
                nodes_same_lvl.append(node.LeftChild)
            if node.RightChild:
                nodes_same_lvl.append(node.RightChild)
            return nodes_same_lvl
        if curr_lvl < need_lvl:
            return (self._add_nodes_of_lvl(node.LeftChild, curr_lvl + 1, need_lvl) +
                    self._add_nodes_of_lvl(node.RightChild, curr_lvl + 1, need_lvl))
        return []

    def _height(self, node: BSTNode) -> int:
        if not node:
            return 0

        l_height = r_height = 0

        if node.LeftChild:
            l_height = self._height(node.LeftChild)
        if node.RightChild:
            r_height = self._height(node.RightChild)

        return max(l_height, r_height) + 1

    def DeepAllNodes(self, order: int) -> tuple[BSTNode]:
        """Производит обход всего дерева в глубину.

        order == 0 - in-order

        order == 1 - post-order

        order == 2 - pre-order
        """
        if order == 0:
            return tuple(self._deep_in_order(self.Root))
        if order == 1:
            return tuple(self._deep_post_order(self.Root))
        if order == 2:
            return tuple(self._deep_pre_order(self.Root))

    def _deep_in_order(self, node):
        if not node:
            return []
        nodes = []

        if node.LeftChild:
            nodes.extend(self._deep_in_order(node.LeftChild))

        nodes.append(node)

        if node.RightChild:
            nodes.extend(self._deep_in_order(node.RightChild))

        return nodes

    def _deep_post_order(self, node):
        if not node:
            return []
        nodes = []

        if node.LeftChild:
            nodes.extend(self._deep_post_order(node.LeftChild))

        if node.RightChild:
            nodes.extend(self._deep_post_order(node.RightChild))

        nodes.append(node)

        return nodes

    def _deep_pre_order(self, node):
        if not node:
            return []

        nodes = [node]

        if node.LeftChild:
            nodes.extend(self._deep_pre_order(node.LeftChild))

        if node.RightChild:
            nodes.extend(self._deep_pre_order(node.RightChild))

        return nodes
