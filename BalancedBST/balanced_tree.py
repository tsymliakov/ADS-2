class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        if len(a) == 0:
            return

        if len(a) == 1:
            self.Root = BSTNode(a[0], None)
            return

        keys = a[:]
        keys.sort()

        root_index = len(keys) // 2
        self.Root = BSTNode(keys[root_index], None)

        left = right = None

        if root_index - 1 >= 0:
            left = self._generate_tree(
                keys, self.Root, 0, root_index - 1)
        if root_index + 1 <= len(keys) - 1:
            right = self._generate_tree(
                keys, self.Root, root_index + 1, len(keys) - 1)

        if left is not None and left.NodeKey == self.Root.NodeKey:
            self.Root.RightChild = left

            curr_node = self.Root.RightChild
            while curr_node.RightChild is not None:
                curr_node = curr_node.RightChild

            curr_node.RightChild = right
            right.Parent = curr_node

            self._put_level_in_nodes(self.Root, 0)
            return

        self.Root.LeftChild = left
        self.Root.RightChild = right
        self._put_level_in_nodes(self.Root, 0)

    def _put_level_in_nodes(self, node, lvl):
        node.Level = lvl

        if node.LeftChild is not None:
            self._put_level_in_nodes(node.LeftChild, lvl + 1)
        if node.RightChild is not None:
            self._put_level_in_nodes(node.RightChild, lvl + 1)

    def _generate_tree(self, keys: list, parent: BSTNode, start, end):
        key_for_node_index = (start + end) // 2
        new_node = BSTNode(keys[key_for_node_index], parent)

        if start == end:
            return new_node

        left = right = None

        if key_for_node_index - 1 >= start:
            left = self._generate_tree(
                keys, new_node, start, key_for_node_index - 1)
        if key_for_node_index + 1 <= end:
            right = self._generate_tree(
                keys, new_node, key_for_node_index + 1, end)

        if left is not None and left.NodeKey == new_node.NodeKey:
            new_node.RightChild = left

            curr_node = new_node.RightChild
            while curr_node.RightChild is not None:
                curr_node = curr_node.RightChild

            curr_node.RightChild = right
            right.Parent = curr_node
            return new_node

        new_node.LeftChild = left
        new_node.RightChild = right

        return new_node

    def IsBalanced(self, root_node):
        # Дерево является сбалансированным если его правое и левое
        # поддеревья сбалансированны. А также если глубина левого и
        # правого поддеревьев различаются менее, чем на 2.
        if root_node is None:
            return True

        left_deep = self._get_deep(root_node.LeftChild, 1)
        right_deep = self._get_deep(root_node.RightChild, 1)

        if abs(left_deep - right_deep) > 1:
            return False

        if self.IsBalanced(root_node.LeftChild) is False:
            return False
        if self.IsBalanced(root_node.RightChild) is False:
            return False

        return self.IsBalanced(root_node.LeftChild) and self.IsBalanced(root_node.RightChild)

    def _get_deep(self, node: BSTNode, curr_lvl):
        if node is None:
            return curr_lvl - 1

        return max(self._get_deep(node.LeftChild, curr_lvl + 1), self._get_deep(node.RightChild, curr_lvl + 1))
