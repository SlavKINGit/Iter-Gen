class FlatIterator:

    def __init__(self, list_of_lists_2):
        self.list = list_of_lists_2
        self.idx = 0
    
    def reform(self, data):
        new_list = []
        for i in data:
            if isinstance(i, list):
                new_list.extend(self.reform(i))
            else:
                new_list.append(i)
        return new_list

    def __iter__(self):
        self.new_list = self.reform(self.list)
        return self

    def __next__(self):
        if self.idx >= len(self.new_list):
            raise StopIteration
        item = self.new_list[self.idx]
        self.idx += 1
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()