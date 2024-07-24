# dict - словарь, отображение, хеш-мап, ассоциативный массив, коллекция пар ключ-значение,
# где ключом может быть только hashable тип, доступ по ключу и проверка наличия ключа 0(1), с питона 3.7 хранит порядок вставки
# пустой словарь создавать лучше через {}, а не dict(), под капотом сразу будет создано 8 элементов

# Hashable != Immutable
# Immutable - означает что наш класс(обьект) больше не меняется
# Hashable - означает что наш класс(обьект) реализует dunder метод __hash__

# set - множество, хешсет, неупорядоченный набор hashable обьектов, доступ и проверка наличия 0(1)
# frozenset - неизменяемый брат множества
#
# Получаем хеш -> высчитываем позицию в массиве -> если элемента нет то действует соответственно задаче ->
# если элемент есть то сравниваем по ключ == тому что ищем -> если ключ не равен искомому то ищем дополнительный бакет

# По умолчанию самописные классы возвращают хеш основанный на id, если переопределяете хеш, то всегда проверяйте,
# что у равных обьектов одинаковый хеш
# Что можно положить в сет/словарь и проверка на содержимое

#           !!!Вопросы!!!

# Вопрос 1: tuple можно положить в dict или в set?
# Ответ 1: Tuple можно положить в dict или в set, но только если он содержить ХЭШИРУЕМЫЕ элементы

# Вопрос 2: А можно ли set или dict положить в set или dict?
# Ответ 2: Нет Нельзя!!!
# set и dict используют один и тот же алгоритм хэширования

# Коллизия - если у двух не равных элементов hash одинаковый(больше относиться к самописным классам)

import dis
from timeit import timeit
from terminaltables import AsciiTable

# x = timeit('dict()')
# y = timeit('{}')
# print(x)
# print(y)
# print(dis.dis('dict()'))
# print(dis.dis('{}'))


# a_dict = dict(x=1, y=2, z=3)
# a_set = set('xyz')
# b_set = {1, 2, 3, 4, 5, 123123123, -1231244, 0}
# print(a_dict)
# print(a_set)
# print(b_set)


# a_list = list(range(10_000))
# a_set = set(a_list)
# a_tuple = tuple(a_list)
# a_dict = {i: None for i in a_list}
# in_list = timeit('5_000 in a_list', 'from __main__ import a_list', number=100)
# in_tuple = timeit('5_000 in a_tuple', 'from __main__ import a_tuple', number=100)
# in_set = timeit('5_000 in a_set', 'from __main__ import a_set', number=100)
# in_dict = timeit('5_000 in a_dict', 'from __main__ import a_dict', number=100)
# in_dict2 = timeit('9999 in a_dict', 'from __main__ import a_dict', number=100)
# in_dict3 = timeit('50_000 in a_dict', 'from __main__ import a_dict', number=100)
# print(f'{in_list:.6f}')
# print(f'{in_tuple:.6f}')
# print(f'{in_set:.6f}')
# print(f'{in_dict:.6f}')
# print(f'{in_dict2:.6f}')
# print(f'{in_dict3:.6f}')


# a_list = [['        '] * 8]
# print(AsciiTable(a_list).table)
# print(a_list)
# a_list[0][3] = '("a", 1)'
# a_list[0][0] = '("A", 1)'
# a_list[0][7] = '("b", 2)'
# print(AsciiTable(a_list).table)

# для самописных классов если мы не переопределяем __hash__
# hash будет равен адрес в памяти // поделенный на 16
class Cat:
    pass

tom = Cat()
print(hash(tom))
print(id(tom))
print(id(tom)//16)



# class Cat:
#     __hash__ = None
#
#
# print(hash(Cat()))

# a_tuple = (1, 2, 3)
# a_tuple = (1, 2, 3, [])
# a_set = {a_tuple}
# print(a_set)

# a_set = {1, 2, 3}
# b_set = {a_set}
# print(b_set)


# a_set = {1, 2, 3, 4}
# print([] in a_set)


# a_dict = {}
# a_set = set()
# a_list = []
# a_tuple_list = (1,2,3, [])
# a_tuple = (1,2,3)
# a_str = 'hhh'
# a_int = 5

# print(hash(a_dict))
# print(hash(a_set))
# print(hash(a_list))
# print(hash(a_tuple))
# print(hash(a_tuple_list))
# print(hash(a_str))
# print(hash(a_int))
