

class FlatIterator:

    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.list_iter = iter(self.list)
        self.nested_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.list_iter)
        return self.nested_list[self.cursor]


def flat_generator(list):
    # Генератор возвращает элементы из списка с двойным уровнем вложенности
    for sub_list in list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    print('-'*10)

    print('Работа итератора')
    for item in FlatIterator(nested_list):
        print(item)
    print('-' * 10)

    print('Работа компрехеншен')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('-' * 10)

    print('Работа генератора')
    for item in flat_generator(nested_list):
        print(item)
    print('-' * 10)
