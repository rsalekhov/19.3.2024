class FlatIterator:
    def __init__(self, list_of_lists):
        self.data = list_of_lists
        self.index_outer = 0
        self.index_inner = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_outer < len(self.data):
            if self.index_inner < len(self.data[self.index_outer]):
                item = self.data[self.index_outer][self.index_inner]
                self.index_inner += 1
                return item
            else:
                self.index_outer += 1
                self.index_inner = 0
                return next(self)
        else:
            raise StopIteration()


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
