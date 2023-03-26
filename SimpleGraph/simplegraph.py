from operator import index


class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        index_of_empty = self._get_empty()
        if index_of_empty == None:
            return

        self.vertex[index_of_empty] = Vertex(v)
        print()

    def RemoveVertex(self, v):
        if not self._are_indexies_ok(v):
            return

        for i in range(len(self.m_adjacency)):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

        self.vertex[v] = None

    def IsEdge(self, v1, v2):
        if not self._are_indexies_ok(v1, v2):
            return None

        if self.m_adjacency[v1][v2] > 0:
            return True
        return False

    def AddEdge(self, v1, v2):
        if not self._are_indexies_ok(v1, v2):
            return None

        if self.vertex[v1] is None or self.vertex[v2] is None:
            return

        self.m_adjacency[v1][v2] += 1
        if v1 != v2:
            self.m_adjacency[v2][v1] += 1

    def RemoveEdge(self, v1, v2):
        if not self._are_indexies_ok(v1, v2):
            return None

        if self.m_adjacency[v1][v2] > 0:
            self.m_adjacency[v1][v2] -= 1
            if v1 != v2:
                self.m_adjacency[v2][v1] -= 1

    def _get_empty(self):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                return i
        return None

    def _are_indexies_ok(self, *indexies):
        if not self._are_indexies_in_range(*indexies):
            return False
        if not self._are_there_vertexes(*indexies):
            return False
        return True

    def _are_indexies_in_range(self, *indexies):
        """Проверяет, умещаются ли индексы в размер графа."""
        for i in indexies:
            if i > len(self.vertex) - 1:
                return False
        return True

    def _are_there_vertexes(self, *indexies):
        """Проверяет, сушествуют ли вершины."""
        for i in indexies:
            if self.vertex[i] == None:
                return False
        return True
