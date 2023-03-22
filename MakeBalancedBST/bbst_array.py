def _generateBBSTArray(keys: list, bst : list, put_index):
    if len(keys) == 1:
        bst[put_index] = keys[0]
        return

    bst[put_index] = keys[len(keys) // 2]

    _generateBBSTArray(keys[:len(keys) // 2], bst, put_index * 2 + 1)
    _generateBBSTArray(keys[-(len(keys) // 2):], bst, put_index * 2 + 2)



def GenerateBBSTArray(a: list):
    """Получает на вход список значений, равный списку, представляющему
    собой полностью заполненное бинарное дерево. Возвращает список-
    заполненной дерево."""

    # Построение двоичного дерева таким способом происходит за
    # O(N * log N) + O(N). Первым делом происходит сортировка, а далее
    # единичный проход по элементам входного массива

    if len(a) == 0:
        return []

    keys = a[:]
    keys.sort()
    bst_array = [None] * len(keys)

    _generateBBSTArray(keys, bst_array, 0)

    return bst_array
