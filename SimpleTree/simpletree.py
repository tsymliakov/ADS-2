class SimpleTreeNode:

    def __init__(self, val, parent=None):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root: SimpleTreeNode):
        self.Root = root  # корень, может быть None
        self.nodes = [root]

    def _get_all_child(self, parent_node):
        if len(parent_node.Children) == 0:
            return []

        child_nodes = parent_node.Children[:]

        for node in child_nodes:
            child_nodes += self._get_all_child(node)

        return child_nodes



    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        if not isinstance(ParentNode, SimpleTreeNode):
            raise ValueError('ParentNode isn\'t SimpleTreeNode object.')
        if not isinstance(NewChild, SimpleTreeNode):
            raise ValueError('NewChild isn\'t SimpleTreeNode object.')
        if ParentNode not in self.nodes:
            pass #raise ValueError('ParentNode doesn\'t belong to tree.')

        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        self.nodes.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is self.Root:
            return
        
        # Нужно получить ссылки на все дочерние узлы и применить к ним ко всем
        # оператор del





        pass  # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return []

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        return []

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        # количество листьев в дереве
        return 0
