class SimpleTreeNode:
    def __init__(self, val, parent=None):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def __repr__(self) -> str:
        return f'{self.NodeValue}'


class SimpleTree:
    def __init__(self, root: SimpleTreeNode):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        if not isinstance(ParentNode, SimpleTreeNode):
            raise ValueError('ParentNode isn\'t SimpleTreeNode object.')
        if not isinstance(NewChild, SimpleTreeNode):
            raise ValueError('NewChild isn\'t SimpleTreeNode object.')

        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        parent = NodeToDelete.Parent
        if parent is not None:
            parent.Children = [
                child for child in parent.Children if child is not NodeToDelete]

    def _find_parent_of_node(self, node: SimpleTreeNode, node_to_delete: SimpleTreeNode) -> SimpleTreeNode:
        if len(node.Children) == 0:
            return

        parent_node = None

        for child in node.Children:
            if child is node_to_delete:
                parent_node = node
                return parent_node

        for child in node.Children:
            parent_node = self._find_parent_of_node(child, node_to_delete)
            if parent_node:
                return parent_node

    def GetAllNodes(self, node=None):
        if node is None:
            node = self.Root
        all_nodes = [node]
        all_nodes.extend(self._get_all_child(node))
        return all_nodes

    def _get_all_child(self, node):
        if len(node.Children) == 0:
            return []

        child_nodes = node.Children[:]

        for child in child_nodes:
            # Its insane :-/
            # I don't understand why searching stops work if
            # child_nodes += self._get_all_child(child)
            child_nodes = child_nodes + self._get_all_child(child)

        return child_nodes

    def FindNodesByValue(self, val):
        all_nodes = self.GetAllNodes()
        return [node for node in all_nodes if node.NodeValue == val]

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        if OriginalNode is self.Root:
            return
        if OriginalNode is NewParent:
            return

        parent_of_orig = OriginalNode.Parent
        parent_of_orig.Children = [c for c in parent_of_orig.Children if
                                   c is not OriginalNode]

        NewParent.Children.append(OriginalNode)

    def Count(self):
        return self._count_all_nodes(self.Root)

    def _count_all_nodes(self, node: SimpleTreeNode):
        counted_nodes = 1

        if len(node.Children) == 0:
            return counted_nodes

        for child in node.Children:
            counted_nodes += self._count_all_nodes(child)

        return counted_nodes

    def LeafCount(self):
        return self._count_all_leaf(self.Root)

    def _count_all_leaf(self, node: SimpleTreeNode):
        leaf_count = 0

        if len(node.Children) == 0:
            leaf_count = 1
            return leaf_count

        for child in node.Children:
            leaf_count += self._count_all_leaf(child)

        return leaf_count

    def EvenTrees(self):
        if self.Count() % 2 != 0:
            return []

        lifs = [i for i in self.GetAllNodes() if len(i.Children) == 0]
        node_connection = []
        for i in range(len(lifs)):
            node = lifs[i]
            while node.Parent != self.Root:
                if self._count_all_nodes(node.Parent) % 2 == 0 and node.Parent not in node_connection:
                    node_connection.append(node.Parent.Parent)
                    node_connection.append(node.Parent)
                node = node.Parent
        return node_connection
