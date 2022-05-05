from decs import log, log_path

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

@log
@log_path(path='logs_path.txt')
def flat_generator(list):
    # Генератор возвращает элементы из списка с двойным уровнем вложенности
    for sub_list in list:
        for elem in sub_list:
            yield elem

class FlatIteratorEnhanced:

    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)   # получаем следующий элемент списка
            except StopIteration:  # или исключение, если нет следующего элемента
                if not self.iterators_queue:  # если не осталось элементов, возвращаем исключение
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()  # или получаем следующий элемент очереди
                    continue
            if isinstance(self.current_element, list):  # проверяем тип следующего элемента
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:  # если элемент не список, возвращаем этот элемент
                return self.current_element

@log
@log_path(path='logs_path.txt')
def flat_generator_enhanced(_list):
    for elem in _list:
        if isinstance(elem, list):  # проверяем тип следующего элемента
            for sub_elem in flat_generator_enhanced(elem):  # если список, то рекурсивно вызываем этот же генератор
                yield sub_elem
        else:
            yield elem  # если не список, возвращаем элемент

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    # print('-'*10)

    # print('Работа итератора')
    # for item in FlatIterator(nested_list):
    #     print(item)
    # print('-' * 10)

    # print('Работа компрехеншен')
    # flat_list = [item for item in FlatIterator(nested_list)]
    # print(flat_list)
    # print('-' * 10)
    #
    print('Работа генератора')
    for item in flat_generator(nested_list):
        print(item)
    print('-' * 10)
    #
    nested_list = [
        ['a', ['b'], 'c'],
        ['d', 'e', [[[[['f']]]]], 'h', False],
        [1, [[[2]]], None],
    ]
    #
    # print('Вызов расширенного итератора')
    # for item in FlatIteratorEnhanced(nested_list):
    #     print(item)
    # print('-' * 10)
    #
    print('Вызов расширенного генераторра')
    for item in flat_generator_enhanced(nested_list):
        print(item)
    print('-' * 10)
    #
    # print('Вызов компрехеншен')
    # flat_list = [item for item in FlatIteratorEnhanced(nested_list)]
    # print(flat_list)
    # print('-' * 30)
