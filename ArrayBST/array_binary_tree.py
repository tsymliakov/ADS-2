class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        if self.Tree[0] is None:
            return None

        return self._find(0, key)

    def _find(self, index, key):
        # Поздновато я принял во внимание, что метод поиска должен
        # возвращать индекс подходящего места для вставки ключа,
        # умноженный на -1. Алгоритм добавления ключа был реализован
        # раньше и мне жалко его удалять, чтобы заменить его на вызов
        # метода поиска

        if self.Tree[index] is None:
            return index * -1

        if self.Tree[index] == key:
            return index

        left_child_index = 2 * index + 1
        if left_child_index >= len(self.Tree):
            return None
        if key < self.Tree[index]:
            return self._find(left_child_index, key)

        right_child_index = 2 * index + 2
        if (2 * index + 2) >= len(self.Tree):
            return None
        if key > self.Tree[index]:
            return self._find(right_child_index, key)

    def AddKey(self, key):
        # индекс добавленного/существующего ключа или -1 если не удалось
        return self._add(0, key)

    def _add(self, index, key):
        if self.Tree[index] is None:
            self.Tree[index] = key
            return index

        if self.Tree[index] == key:
            return index

        left_child_index = 2 * index + 1
        if left_child_index >= len(self.Tree):
            return -1
        if key < self.Tree[index]:
            return self._add(left_child_index, key)

        right_child_index = 2 * index + 2
        if (2 * index + 2) >= len(self.Tree):
            return -1
        if key > self.Tree[index]:
            return self._add(right_child_index, key)
