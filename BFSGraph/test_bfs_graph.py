from bfs_graph import *


# Test _get_unvisited_related

# Некорректные входные данные могут быть такими:
# 1) Вершины вне диапазона графа
# 2) Вершина в диапазоне, но несуществует
# 3) Передается None
# 4) Передается неверный тип (такое не возможно при моей эксплуатации
#    функции, а также в тестовой среде, так что не буду тестировать эту
#    ситуацию)
def test_get_unvis_related_input_out_of_range():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)

    assert g._get_unvisited_related(3) is None


def test_get_unvis_related_doesnt_exist():
    g = SimpleGraph(3)

    g.AddVertex(0)
    g.AddVertex(1)

    assert g._get_unvisited_related(2) is None


def test_get_unvis_related_none():
    g = SimpleGraph(3)
    g.AddVertex(0)
    g.AddVertex(1)
    assert g._get_unvisited_related(None) is None

# После того, как некорректные данные были отсеяны, можно обособиться и
# считать, что в функцию поступают лишь корректные данные. При работе с
# данными (матрицей компетенции), следует рассмотреть следующие
# ситуации:
# У вершины 0, 1, несколько смежных вершин;
# Граф целиком заполнен и не заполнен целиком;
# Смежные вершины могут быть посещены, а могут быть и не посещены;
# У вершины могут быть петли. 1 или несколько
# У вершины может быть несколько ребер со смежной вершиной


# Full graph

def test_get_unvis_related_0_related():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    assert g._get_unvisited_related(3) == []

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_1_related():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)

    assert g._get_unvisited_related(3) == [0]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_few_related():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)
    g.AddEdge(3, 2)

    assert g._get_unvisited_related(3) == [0, 2]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == [2]

    g.vertex[2].Hit = True

    assert g._get_unvisited_related(3) == []


# Not full graph

def test_get_unvis_related_0_related_not_full():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    assert g._get_unvisited_related(3) == []

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_1_related_not_full():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)

    assert g._get_unvisited_related(3) == [0]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_few_related_not_full():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)
    g.AddEdge(3, 2)

    assert g._get_unvisited_related(3) == [0, 2]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == [2]

    g.vertex[2].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_loops():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 3)

    assert g._get_unvisited_related(3) == [3]

    g.AddEdge(3, 3)

    assert g._get_unvisited_related(3) == [3]

    g.vertex[3].Hit = True

    assert g._get_unvisited_related(3) == []


def test_get_unvis_related_few_edges():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    g.AddEdge(3, 0)
    g.AddEdge(0, 3)
    g.AddEdge(3, 0)
    g.AddEdge(0, 3)

    assert g._get_unvisited_related(3) == [0]

    g.vertex[0].Hit = True

    assert g._get_unvisited_related(3) == []


# Test BFS

"""
Мысли о входных данных: На вход поступают два индекса вершин, очередь и
стек.

Возможная некорректность входных данных:

1) Индексы за пределами графа. Алгоритм обработает такую ситуацию. Но
    для этого ему прийдется обойти весь граф;
2) Индексы совпадают. В случае, если вершина имеет петлю- алгоритм решит
   задачу. Но если петли нет- пройдет весь граф и не обнаружит пути.
   Поскольку задача поиска пути из вершины_один в вершину_один является
   абсурдом- не будем об этом задумываться и будем выплевывать пустой
   список.
3) Индексы не принадлежат числовому типу (на самом деле стоило такую же
   проверку сделать и для предыдущей функции. Но ладно уж, прощу сам
   себе эту оплошность, но на будущее запомню);
4) Очередь может быть не пустой с самого начала. (Изложил этот случай в
   python jokes. Суть в том, что происходит замыкание и очередь может
   содержать объекты оставшиеся от прошлого запуска);
5) Стек может быть не пустым;

Чтобы избежать этого- при вызове функции поиска из "главной" функции
поиска, будем передавать пустые списки.

6) Неявные входные данные: не все узлы могут оказаться нетронутыми;
"""


def test_bfs_indexes_out_of_range():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    assert g.BreadthFirstSearch(0, 4) is None
    assert g.BreadthFirstSearch(4, 0) is None
    assert g.BreadthFirstSearch(4, 7) is None


def test_bfs_same_verticies():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    assert g.BreadthFirstSearch(0, 0) == []

    g.AddEdge(0, 0)

    assert g.BreadthFirstSearch(0, 0) == []


def test_bfs_wrong_type():
    g = SimpleGraph(4)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    assert g.BreadthFirstSearch('0', 1) is None
    assert g.BreadthFirstSearch(0, '1') is None
    assert g.BreadthFirstSearch(None, None) is None


def test_bfs_are_hits_false():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 3)
    g.AddEdge(4, 1)
    g.AddEdge(4, 5)

    verticies = g.vertex

    g.BreadthFirstSearch(0, 5)

    for v in verticies:
        assert v.Hit is False

    g.BreadthFirstSearch(1, 2)

    for v in verticies:
        assert v.Hit is False

    g.BreadthFirstSearch(4, 4)

    for v in verticies:
        assert v.Hit is False


"""
Тесты на работу с данными.
"""


def test_bfs_simple():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[3],
        g.vertex[4],
        g.vertex[5]
    ]


"""
Возможно несколько ситуаций, которые следует обработать:
- Петли
- Циклы
- Множественные ребра между двумя нодами
- Несвязный граф, в котором стартовая нода и искомая ноды находятся в
разных подграфах
"""


def test_bfs_loops():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    g.AddEdge(0, 0)
    g.AddEdge(0, 0)

    g.AddEdge(1, 1)
    g.AddEdge(1, 1)

    g.AddEdge(2, 2)
    g.AddEdge(2, 2)

    g.AddEdge(3, 3)
    g.AddEdge(3, 3)

    g.AddEdge(4, 4)
    g.AddEdge(4, 4)

    g.AddEdge(5, 5)
    g.AddEdge(5, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[3],
        g.vertex[4],
        g.vertex[5]
    ]


def test_bfs_cycles_1():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    g.AddEdge(1, 0)
    g.AddEdge(2, 0)
    g.AddEdge(3, 0)
    g.AddEdge(4, 0)

    res = g.BreadthFirstSearch(0, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[4],
        g.vertex[5]
    ]


def test_bfs_cycles_2():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[3],
        g.vertex[5]
    ]


def test_bfs_multiple_edges_cycles_loops():
    g = SimpleGraph(6)

    g.AddVertex(0)
    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)
    g.AddVertex(4)
    g.AddVertex(5)

    g.AddEdge(0, 1)
    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(1, 2)
    g.AddEdge(2, 3)
    g.AddEdge(2, 3)
    g.AddEdge(3, 4)
    g.AddEdge(3, 4)
    g.AddEdge(4, 1)
    g.AddEdge(4, 1)
    g.AddEdge(3, 5)
    g.AddEdge(3, 5)
    g.AddEdge(4, 5)
    g.AddEdge(4, 5)

    g.AddEdge(5, 5)
    g.AddEdge(4, 4)
    g.AddEdge(2, 2)

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5]
    ]