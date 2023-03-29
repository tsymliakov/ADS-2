class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

    def __repr__(self) -> str:
        return f"Vertex {self.Value}"


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex] = [None] * size

    def AddVertex(self, v):
        index_of_empty = self._get_empty()
        if index_of_empty is None:
            return

        self.vertex[index_of_empty] = Vertex(v)

    def RemoveVertex(self, v: int):
        if not self._are_indexies_ok(v):
            return

        for i in range(len(self.m_adjacency)):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

        self.vertex[v] = None

    def IsEdge(self, v1: int, v2: int):
        if not self._are_indexies_ok(v1, v2):
            return None

        return self.m_adjacency[v1][v2] > 0

    def AddEdge(self, v1: int, v2: int):
        if not self._are_indexies_ok(v1, v2):
            return None

        if self.vertex[v1] is None or self.vertex[v2] is None:
            return

        self.m_adjacency[v1][v2] += 1
        if v1 != v2:
            self.m_adjacency[v2][v1] += 1

    def RemoveEdge(self, v1: int, v2: int):
        if not self._are_indexies_ok(v1, v2):
            return None

        if self.m_adjacency[v1][v2] > 0:
            self.m_adjacency[v1][v2] -= 1
            if v1 != v2:
                self.m_adjacency[v2][v1] -= 1

    def DepthFirstSearch(self, VFrom: int, VTo: int):
        for v in self.vertex:
            if v is not None:
                v.Hit = False

        if not self._are_indexies_ok(VFrom, VTo):
            return []

        full_path = self._depth_first_search(VFrom, VTo, [])

        return full_path

    def BreadthFirstSearch(self, VFrom: int, VTo: int):
        if not isinstance(VFrom, int) or not isinstance(VTo, int):
            return None
        if not self._are_indexies_in_range(VFrom, VTo):
            return None
        if VFrom == VTo:
            return []

        self.vertex[VFrom].Hit = True
        pathes = self._breadth_first_search(VFrom, VTo, [VFrom], [], {})

        self._unhit()

        return pathes[VTo]

    def _breadth_first_search(self, currV: int, VTo: int, q: list[int],
                              prev_vertecies: list[int], pathes: dict):
        q.pop(0)

        unvisited_related = self._get_unvisited_related(currV)

        for v in unvisited_related:
            # if v == VTo:
            #     return [self.vertex[currV], self.vertex[v]]
            if pathes.get(v) is None:
                pathes[v] = prev_vertecies + [self.vertex[currV], self.vertex[v]]
            if v == VTo:
                return pathes
            self.vertex[v].Hit = True
            q.append(v)

        if len(q) == 0:
            return pathes

        

        return self._breadth_first_search(q[0], VTo, q, prev_vertecies[:] + [self.vertex[currV]], pathes)

    def _get_unvisited_related(self, vertex_index: int):
        if vertex_index is None:
            return None
        if vertex_index >= len(self.vertex):
            return None
        if self.vertex[vertex_index] is None:
            return None

        related = self._get_related_vertexes(vertex_index)

        return [v for v in related if self.vertex[v].Hit is False]

    def _unhit(self):
        for v in self.vertex:
            v.Hit = False

    def _get_related_vertexes(self, vertex_index: int):
        relate = [i for i in range(len(self.m_adjacency[vertex_index])) if
                  self.m_adjacency[vertex_index][i] >= 1]

        return relate

    def _depth_first_search(self, currV: int, VTo: int, path: list[int]):
        self.vertex[currV].Hit = True
        path.append(self.vertex[currV])

        related = self._get_related_vertexes(currV)

        if VTo in related:
            self.vertex[VTo].Hit = True
            path.append(self.vertex[VTo])
            return path

        path_ = path[:]

        for v in related:
            if self.vertex[v].Hit is True:
                continue
            path_ = (self._depth_first_search(v, VTo, path_))

            if self.vertex.index(path_[-1]) == VTo:
                return path_

        path.pop()

        return path

    def _get_empty(self):
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                return i
        return None

    def _are_indexies_ok(self, *indexies: int):
        for i in indexies:
            if not isinstance(i, int):
                return False
        if not self._are_indexies_in_range(*indexies):
            return False
        if not self._are_there_vertexes(*indexies):
            return False
        return True

    def _are_indexies_in_range(self, *indexies: int):
        """Проверяет, умещаются ли индексы в размер графа."""
        for i in indexies:
            if i > len(self.vertex) - 1:
                return False
        return True

    def _are_there_vertexes(self, *indexies: int):
        """Проверяет, сушествуют ли вершины."""
        for i in indexies:
            if self.vertex[i] is None:
                return False
        return True
