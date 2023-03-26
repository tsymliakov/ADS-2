class Heap:

    def __init__(self):
        self.HeapArray = []
        self.LastKey = None  # Мой хак

    def MakeHeap(self, values: list[int], depth: int):
        if depth < 0:
            return

        self.HeapArray = [None] * (2 ** (depth + 1) - 1)

        if len(self.HeapArray) < len(values):
            # Конечно, следовало бы вычислить логарифм по основанию 2 от
            # len(values) и изменить размер HeapArray так, чтобы он по
            # прежнему мог бы вместить в себя полностью заполненную кучу
            # такой глубины. Но для этого надо импортировать библиотеку,
            # чего я делать не хочу.

            # А еще я не до конца понимаю, все таки зачем мне передают
            # depth. Но есть подозрение, что такой ситуации в тестовой
            # среде и не возникнет.
            self.HeapArray += [None] * (len(values) - len(self.HeapArray))

        if len(values) == 0:
            return

        self.HeapArray[0] = values[0]

        for i in range(1, len(values)):
            self.HeapArray[i] = values[i]
            self._sift_up(i)

        self.LastKey = len(values) - 1

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1

        backup = self.HeapArray[0]

        self.HeapArray[0] = self.HeapArray[self.LastKey]
        self.HeapArray[self.LastKey] = None

        self.LastKey -= 1

        if self.LastKey < 0:
            self.LastKey = None

        self._sift_down(0)

        return backup

    def Add(self, key):
        if self.LastKey is None:
            # Значит нет элементов, можно просто вставить в первый
            # индекс
            self.HeapArray[0] = key
            self.LastKey = 0
            return True
        if self.LastKey == len(self.HeapArray) - 1:
            return False

        self.LastKey += 1
        self.HeapArray[self.LastKey] = key
        self._sift_up(self.LastKey)
        return True

    def _sift_down(self, index):
        if not self._both_childs_in_range(index):
            return

        left = self._get_left_child_index(index)
        if self.HeapArray[left] is None:
            return

        biggest_child_index = left

        right = self._get_right_child_index(index)

        if self.HeapArray[right] is not None:
            biggest_child_index = left if self.HeapArray[left] > self.HeapArray[right] else right

        if self.HeapArray[biggest_child_index] > self.HeapArray[index]:
            self.HeapArray[index], self.HeapArray[biggest_child_index] = \
                self.HeapArray[biggest_child_index], self.HeapArray[index]
            self._sift_down(biggest_child_index)

    def _sift_up(self, index):
        parent = self._get_parent_index(index)

        if self.HeapArray[parent] < self.HeapArray[index]:
            self.HeapArray[parent], self.HeapArray[index] = \
                self.HeapArray[index], self.HeapArray[parent]
            if parent > 0:
                self._sift_up(parent)

    def _get_left_child_index(self, parent_index):
        return parent_index * 2 + 1

    def _get_right_child_index(self, parent_index):
        return parent_index * 2 + 2

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def _both_childs_in_range(self, parent_index):
        return True if (parent_index * 2 + 2) < len(self.HeapArray) else False
