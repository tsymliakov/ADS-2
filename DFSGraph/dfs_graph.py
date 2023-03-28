class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex] = [None] * size

    def AddVertex(self, v):
        index_of_empty = self._get_empty()
        if index_of_empty is None:
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

        return self.m_adjacency[v1][v2] > 0

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

    def DepthFirstSearch(self, VFrom, VTo):
        if not self._are_indexies_ok(VFrom, VTo):
            return []

        if VFrom == VTo:
            return []

        full_path = self._depth_first_search(VFrom, VTo, [])

        for v in self.vertex:
            v.Hit = False

        return full_path

    def _get_related_vertexes(self, vertex_index):
        relate = [i for i in range(len(self.m_adjacency[vertex_index])) if
                  self.m_adjacency[vertex_index][i] == 1]

        return relate

    def _depth_first_search(self, currV, VTo: Vertex, path):
        self.vertex[currV].Hit = True
        path.append(self.vertex[currV])

        related: list[Vertex] = self._get_related_vertexes(currV)

        if len(related) == 0:
            return []

        if VTo in related:
            path.append(self.vertex[VTo])
            return path

        path_ = []
        for v in related:
            if self.vertex[v].Hit is False:
                path_ = self._depth_first_search(v, VTo, path)
            if len(path_) != 0:
                return path_

        return []

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
            if self.vertex[i] is None:
                return False
        return True
