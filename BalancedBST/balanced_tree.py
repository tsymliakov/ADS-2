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

        if root_index - 1 >= 0:
            self.Root.LeftChild = self._generate_tree(keys, self.Root, 0, root_index - 1)
        if root_index + 1 <= len(keys) - 1:
            self.Root.RightChild = self._generate_tree(keys, self.Root, root_index + 1, len(keys) - 1)

    def _generate_tree(self, keys: list, parent: BSTNode, start, end):
        # todo: ключ правого равен или больше ключа предка. А ключ
        # левого всегда меньше
        key_for_node_index = (start + end) // 2
        new_node = BSTNode(keys[key_for_node_index], parent)
        new_node.Level = new_node.Parent.Level + 1

        if start == end:
            return new_node

        if key_for_node_index - 1 >= start:
            new_node.LeftChild = self._generate_tree(keys, new_node, start, key_for_node_index - 1)
        if key_for_node_index + 1 <= end:
            new_node.RightChild = self._generate_tree(keys, new_node, key_for_node_index + 1, end)

        return new_node

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node
