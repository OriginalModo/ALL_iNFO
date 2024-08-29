import asyncio
import collections
import functools
import itertools
import json
import operator
import random
import sys
import time
import types
import re




# Напишите  Обход в Обратном порядке в цикле for






# Обход в Обратном порядке в цикле for
"""
# Обход в Обратном порядке в цикле for
for i in range(10, -1, -1):
    print(i, end=' ')  # -> 10 9 8 7 6 5 4 3 2 1 0 
"""



# Используйте dis - Библиотека работы с Байт-кодом   import dis









# dis - Библиотека работы с Байт-кодом  from dis import dis
"""
from dis import dis
def func():
   a = 42
   return a
print(dis(func))


import dis
def func2():
    return 42
print(dis.dis(func2))
"""



# Перепиши примеры ниже   Понимание вложенных списков
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]









# Понимание вложенных списков
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# Сравни их
print([i for row in matrix for i in row])  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print([[i for i in row] for row in matrix])  # -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


# Все результаты будут одинаковые!!!

# Следующее понимание списка будет транспонировать строки и столбцы:
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)          # -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Тоже самое
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)          # -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# что, в свою очередь, аналогично:
transposed = []
for i in range(4):
    # следующие 3 строки реализуют вложенный listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)          # -> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# В реальном мире вам следует предпочесть встроенные функции
print(list(zip(*matrix)))  # -> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(list(zip(matrix)))   # -> [([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 10, 11, 12],)]  # Без распаковки *  исходный
"""



# Повтори примеры  МОРЖА/Walrus  Разные примеры!!!  Моржовый оператор/Walrus

# Перепиши с Моржом
n = 10
# print(5 <= n < 10 or 101 < n < 201)




s = "Hello"
# print(f'Если перевернуть слово "{s}", получится "{s[::-1]}".')





# Напечатайте индекс наименьшего числа в списке.
lst = [5, 8, 3, 2, 7, 4, 9]






# Использование МОРЖА/Walrus  Разные примеры!!!  Моржовый оператор/Walrus
"""
# Пример 1

# Без Моржика
n = 10
print(5 <= n < 10 or 101 < n < 201)          # -> # False
# 1 раз обьявляем Моржика := и потом используем
print(5 <= (с := 10) < 10 or 101 < с < 201)  # -> # False
# Переменная создана
print(с)  # -> 10


# Пример 2
print(f'Если перевернуть слово "{(s:="Hello")}", получится "{s[::-1]}".')
# -> Если перевернуть слово "Hello", получится "olleH".
print(s)  # -> Hello


# Пример 3
# match case и Моржик и несколько переменных сразу
match (a := 7), (b := 4):
    case 7, 4:
        print(6)  # -> 6
    case 10, 5:
        print(10)
    case 6, 3:
        print(4)

print(a, b)  # -> 7 4


# Пример 4
# Напечатайте индекс наименьшего числа в списке.
lst = [5, 8, 3, 2, 7, 4, 9]

print(abs(lst.index(min(lst))))                        # -> 3
print((arr := [5, 8, 3, 2, 7, 4, 9]).index(min(arr)))  # -> 3  # Морж классный  <-----
print(min(range(len(lst)), key=lst.__getitem__))       # -> 3


# Пример 5
# Моржика в условии нельзя
print((nn := 10) + 10 if nn % 2 == 0 else nn - 10)  # -> NameError: name 'n' is not defined
print(nn + 10 if (nn := 10) % 2 == 0 else nn - 10)  # -> 20"""



# Распарсить JSON-строку  json.loads()

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'









# Пример разбора JSON-строки
# 'json.loads()' для разбора JSON-строки.
"""
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

import json

data = json.loads(json_string)
print(data)          # -> {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(data['name'])  # -> Alice
"""



# Распарсить JSON-файл  json.load()
# Предположим, у вас есть файл 'data.json' с содержимым:
"""
{
    "employees": [
        {"name": "John", "age": 28},
        {"name": "Anna", "age": 22},
        {"name": "Mike", "age": 32}
    ]
}
"""







# Пример разбора JSON из файла
# json.load()` для разбора JSON-данных из файла
# Предположим, у вас есть файл 'data.json' с содержимым:
"""
{
    "employees": [
        {"name": "John", "age": 28},
        {"name": "Anna", "age": 22},
        {"name": "Mike", "age": 32}
    ]
}

import json

# Открытие файла и разбор JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Вывод результата
print(data)
print(data['employees'][0]['name'])  # "John"
"""


# Используйте метод 'json.dump()' с отступами   Перепишите пример ниже

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}







# Пример с 'json.dump()' с отступами
# `json.dump()` сериализует объект Python и записывает его в файл в формате JSON.
"""
import json

# Пример данных для сериализации
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Запись данных в файл в формате JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Данные успешно записаны в файл data.json")
"""


# Используйте метод 'json.dumps()' с отступами   Перепишите пример ниже

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}





# Пример с 'json.dumps()' с отступами
# `json.dumps()` сериализует объект Python и возвращает его в виде строкового представления JSON.

"""
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Сериализация данных в строку JSON с отступами
json_string = json.dumps(data, indent=4)

print("Строка JSON с форматированием:")
print(json_string)
"""


# Перепиши Ниже вариант match case  Кортеж/Список Всё Работает так же как и при обычной распаковке '*'

cmd = [1, "Learning", "Python", 2000.78, 5, 3, 5, 10]










# match case  Кортеж/Список Всё Работает так же как и при обычной распаковке '*'
"""
# Всё Работает так же как и при обычной распаковке '*'

cmd = [1, "Learning", "Python", 2000.78, 5, 3, 5, 10]  # 7 Элементов Список
author, title, price, *_ = cmd   # Так будет работать используем *    *_
author, title, price = cmd       # -> ValueError: too many values to unpack (expected 3)
print(author, title, price)      # -> 1 Learning Python


# Ограничить Размер Кортежа/Списка используем guard if     Можно использовать любые скобки () [] или без скобок
match cmd:
    case [_, str() as author, str(title), float() as price, *_] if len(cmd) >= 7 and len(title) < 10:   # guard
        print(f'Список: {author} {title} {price}')
    case _:  # wildcard
        print(f'Непонятный формат данных')
# -> Список: Learning Python 2000.78 [5, 3, 5, 10]
"""



# Перепиши Ниже    match case Словарь  dict '**'

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

def parse_json(data):
    pass



# print(parse_json(json_data))  # -> ('1234', {'email': 'xxx@mail.com'})
# print(parse_json(json_data))  # -> (True, '26.05.2023')







# match case    Словарь  dict '**'
"""
def parse_json(data):
    match data:
        case {'access': bool() as access, 'data': list([date, *_])}:
            return access, date
    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
print(parse_json(json_data))  # -> (False, '26.05.2023')

# Другой вариант
def parse_json(data):
    match data:
        case {'access': access, 'data': [_, {'login': login, **kwargs}, *_]} if access:
            return login, kwargs

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
print(parse_json(json_data))  # -> ('1234', {'email': 'xxx@mail.com'})
"""



# Разделить по Нулям(0) и получить сумму  Merge Nodes in Between Zeros

head = [0, 3, 1, 0, 4, 5, 2, 0]







# Разделить по Нулям(0) и получить сумму  Merge Nodes in Between Zeros
"""
head = [0, 3, 1, 0, 4, 5, 2, 0]

def mergeNodes(head):
    res = re.sub(r'[,\s\]\[]', '', str(head))
    return [eval('+'.join(i)) for i in re.split(r'0', res) if i]

# Тоже самое но с map
def mergeNodes(head):
    res = ''.join([*map(str, head)]).split('0')
    return [sum(map(int, ' '.join(i).split())) for i in res if i]

print(mergeNodes(head))  # -> [4, 11]
"""




# Интересный пример Повтори кстати сам его придумал  a = 'aaaabbсaa' преобразуется в 'a4b2с1a2'

a = 'aaaabbcaa'










# a = 'aaaabbсaa' преобразуется в 'a4b2с1a2'  Считаем символы которые идут подряд
"""
a = 'aaaabbcaa'

# Придумал сам)
re.sub(r'(\w)\1+|\w', lambda x: f'{x[0][0]}{len(x[0])}', a)  # -> a4b2c1a2
"""


# Так можно разделить легко  Повтори

text = r'17383147371'









# Разделит число из тестовых данных на числа, в конце которых стоит единица. 1
"""
text = r'17383147371'

print(re.findall(r'\d*?1', text))  # -> ['1', '73831', '47371']
print(re.findall(r'\d*1', text))   # -> ['17383147371']          Без ?
"""




# Классный пример Повтори   По сути это if...else в Регулярках

text = 'ABC'






# По сути это if...else в Регулярках
"""
# Если находим A значит ищем B иначе ищем C     1 - Номер группы
re.search(r"(A)?(?(1)B|C)", 'ABC')  # -> <re.Match object; span=(0, 2), match='AB'>
re.search(r"(A)?(?(1)B|C)", 'BC')  # -> <re.Match object; span=(1, 2), match='C'>

# Можно и без последнего условия  Шаблон после | необязателен и может быть опущен.
re.search(r"(A)?(?(1)B)", 'ABC')  # -> <re.Match object; span=(0, 2), match='AB'>
re.search(r"(A)?(?(1)B)", 'BC')  # -> <re.Match object; span=(1, 2), match='C'>

# Если находим A значит ищем B иначе ищем C     name - Имя группы
print(re.search(r"(?P<name>A)(?(name)B|C)", 'ABC').group())   # -> AB
print(re.search(r"(?P<name>A)(?(name)BC)", 'ABC').group())    # -> ABC
"""


# Используйте re.compile

text = 'ABC123---'








# Использование re.compile
"""
regex = re.compile("[A-Za-z_]"      # letter or underscore             буква или подчеркивание
                   "[A-Za-z0-9_]*"  # letter, digit or underscore      буква, цифра или подчеркивание
                   )
re.findall(regex, 'ABC123---')  # -> ['ABC123']

# Тоже самое
regex.findall('ABC123---')  # -> ['ABC123']
"""


# Поменяйте местами в регулярке использую Обычные/Именованные группы или Перепишите

text = 'ABC 123'








# Замена по индексу группы: '\1' '\2'    МЕЖДУ/ПЕРЕД/ПОСЛЕ групп можно использовать любые знаки
"""
re.sub(r'(\w+)\s*(\d+)', r'+__\2  \1 !!+',  'ABC 123')                            # -> +__123  ABC !!+   # Поменяли местами
# Замена по Имени группы:   '\g<name>'
re.sub(r'(?P<first>\w+)\s*(?P<second>\d+)', r'\g<second> \g<first>',  'ABC 123')  # -> 123 ABC   # Поменяли местами
"""



# Напишите или Перепишите Обычные/Именованные группы

text = r'ggg wp'









# Обычные/Именованные группы
"""
text = r'ggg wp'
re.search(r'([a-zA-Zа-яА-ЯёЁ])\1\1', text).group()                           # -> ggg
re.search(r'([a-zA-Zа-яА-ЯёЁ])\1', text).group()                             # -> gg

# Тоже самое
re.search(r'(?P<first>[a-zA-Zа-яА-ЯёЁ])(?P=first)', text).group()            # -> gg
re.search(r'(?P<first>[a-zA-Zа-яА-ЯёЁ])(?P=first)(?P=first)', text).group()  # -> ggg
"""


# Напишите Обычную группу и  группу БЕЗ Захвата

text = "abc123"








# Группа С захватом ()   Группа БЕЗ захвата   (?:)
"""
re.findall("([abc])+", "abc")    # -> ['c']     # Группа С захватом
re.findall("(?:[abc])+", "abc")  # -> ['abc']   # Группа БЕЗ захвата   (?:)
"""


# Напишите   Lookahead   Lookbehind




# Lookahead   Lookbehind
# x(?=y) находит x, только если за x следует y             # Positive Lookahead
# x(?!y) находит x, только если за x НЕ следует y          # Negative Lookahead
# (?<=y)x находит x, только если перед x следует y         # Positive Lookbehind
# (?<!y)x находит x, только если перед x НЕ следует y      # Negative Lookbehind
"""
text = '123ABC'
print(re.findall(r'\d+(?=[A-Z])', text))   # -> ['123']
print(re.findall(r'\d+(?!\d+)', text))     # -> ['123']
print(re.findall(r'(?<=^)\d+', text))      # -> ['123']
print(re.findall(r'(?<!$)[A-Z]+', text))   # -> ['ABC']
"""


# Перепиши ниже Обновление Словаря/Множества

a_dict = {"a": 2}
b_dict = {"b": 3}

a_set = {"a", 2}
b_set = {"b", 3}







"""
# Обновление словаря
a_dict = {"a": 2}
a_dict.update({"b": 10})
print(a_dict)  # -> {'a': 2, 'b': 10}

# Обновление множества
a_set = {"a", 2}
a_set.update({"b": 10})
print(a_set)  # -> {'a': 2, 'b': 10}

a_set.update([1, 2], (3, 4))
print(a_set)  # -> {1, 2, 'b', 3, 4, 'a'}
"""


# Перепиши ниже Обьединение *   Объединения **   |

A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set

a = {"w": 5, "x": 6}
b = {"y": 7}






# Обьединение *   Объединения **   |

"""
from itertools import chain
# Обьединение *
A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set
L = [*A, *B, *C]
G = list(chain(A, B, C))
G = [*chain(A, B, C)]    # Тоже самое
print(L)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7]
print(G)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7]


# Объединения **
a = {"w": 5, "x": 6}
b = {"y": 7}
c = {"z": 8, **a, **b}
print(c)  # -> {'z': 8, 'w': 5, 'x': 6, 'y': 7}

# Тоже самое
c = {"z": 8}
c = c | a | b
print(c)  # -> {'z': 8, 'w': 5, 'x': 6, 'y': 7}
"""



# Написать решение чтобы каждый раз создавался новый обьект
# default  Аргументы по умолчанию в функциях:
"""
def f(a, L=[]):                       def f(a, L=set()):                    def f(key, value, L={}):
    L.append(a)                             L.add(a)                              L[key] = value
    return L                                return L                              return L
print(f.__defaults__) # -> ([],)      print(f.__defaults__) # -> (set(),)   print(f.__defaults__) # -> ({},)
print(f(1))           # -> [1]        print(f(1))           # -> {1}        print(f(1, 'A'))      # -> {1: 'A'}
print(f.__defaults__) # -> ([1],)     print(f.__defaults__) # -> ({1},)     print(f.__defaults__) # -> ({1: 'A'},)
print(f(2))           # -> [1, 2]     print(f(2))           # -> {1, 2}     print(f(2, 'B'))      # -> {1: 'A', 2: 'B'}
print(f.__defaults__) # -> ([1, 2],)  print(f.__defaults__) # -> ({1, 2},)  print(f.__defaults__) # -> ({1: 'A', 2: 'B'},)
"""










# Способ обойти это - использовать None по умолчанию и явно проверить его в теле функции:
"""
# list                               # set                                   # dict
def f(a, L=None):                    def f(a, L=None):                       def f(key, value, L=None):
    if L is None:                        if L is None:                           if L is None:
        L = []                               L = set()                               L = {}
    L.append(a)                          L.add(a)                                L[key] = value
    return L                             return L                                return L
print(f.__defaults__) # -> (None,)   print(f.__defaults__) # -> (None,)      print(f.__defaults__) # -> (None,)
print(f(1))           # -> [1]       print(f(1))           # -> {1}          print(f(1, 'A'))      # -> {1: 'A'}
print(f.__defaults__) # -> (None,)   print(f.__defaults__) # -> (None,)      print(f.__defaults__) # -> (None,)
print(f(2))           # -> [2]       print(f(2))           # -> {2}          print(f(2, 'B'))      # -> {2: 'B'}
print(f.__defaults__) # -> (None,)   print(f.__defaults__) # -> (None,)      print(f.__defaults__) # -> (None,)
"""


# Напишите функцию с docstring/name. Выведите документацию и название функции








# Ответ docstring/name
'''
def add_numbers(a, b):
    """This function takes in two numbers and returns their sum"""
    return a + b

print(add_numbers.__doc__)   # -> This function takes in two numbers and returns their sum
print(add_numbers.__name__)  # -> add_numbers
'''


# Напишите Итератор  range(10)








# Итератор  range(10)
"""
# Итератор
it = iter([i*i for i in range(10)])
"""


# Напишите Функцию-Генератор  range(5) и Обычный генератор










# Функцию-Генератор  range(5) и Обычный генератор
"""
# Генератор
def generate_ints(N):
    for i in range(N):
        yield i

for i in generate_ints(5):
    print(i, end=' ')  # -> 0 1 2 3 4

res = generate_ints(2)
print(next(res))
print(next(res))
print(next(res, 'HEHEHE'))  # -> HEHEHE
print(next(res))            # -> StopIteration

# Тоже самое
generate_ints = (i for i in range(5))
print(generate_ints)               # <generator object <genexpr> at 0x000001790AACC040> 

# Можно сразу в принте написать
print(i for i in range(5))         # <generator object <genexpr> at 0x000001790AACD220>     
"""


# Напишите Конструкцию yield from и ЕЁ аналог












# yield from  - это просто сокращенная форма for item in iterable: yield item
"""
def gen_list1(iterable):
    for i in list(iterable):
        yield i

# эквивалентно

def gen_list2(iterable):
    yield from list(iterable)

print(list(gen_list1('python')))  # -> ['p', 'y', 't', 'h', 'o', 'n']
print([*gen_list2('python')])     # -> ['p', 'y', 't', 'h', 'o', 'n']
"""



# Напишите Функцию-Генератор  range(1, 5) и Обычный генератор  range(1, 5)











# Функцию-Генератор  range(1, 5) и Обычный генератор  range(1, 5)
"""
# Например, такой генератор, как:
def squares(start, stop):
   for i in range(start, stop):
       yield i * i

generator = squares(1, 5)
print([i for i in generator])  # -> [1, 4, 9, 16]



# или эквивалентное выражение генератора (genexp)
generator = (i*i for i in range(1, 5))
print([i for i in generator])  # -> [1, 4, 9, 16]
"""


# Cоздайте свой Итератор












# Пример создания итератора Iterator:
"""
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            ret = self.counter
            self.counter += 1
            return ret
        else:
            raise StopIteration

iters = SimpleIterator(4)

print('Функция next:', next(iters))
# Функция next: 0

for i in iters:
   print('Цикл for ... in: ', i)
# Цикл for ... in:  1
# Цикл for ... in:  2
# Цикл for ... in:  3

next(iters)
# StopIteration
"""


# Для создания пользовательского итератора потребуется больше кода:
"""
class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):  # next in Python 2
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


iterator = Squares(1, 3)
for i in iterator:
    print(i, end=' ')    # -> 1 4

# Генератор — это итератор В частности, генератор является подтипом итератора.

print(issubclass(collections.abc.Generator, collections.abc.Iterator))  # -> True
print(issubclass(types.GeneratorType, collections.abc.Iterator))        # -> True
"""


# Напишите Замыкание или Перепишите












# Замыкание
"""
def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names
    return inner

boys = names()
boys('Vasya')
boys('Sasya')
print(boys.__closure__[0].cell_contents)  # -> ['Vasya', 'Sasya']

# Интересно как работает
print(names()((lambda x: x+5)(2)))        # -> [7]
"""


# Напишите Замыкание lambda или Перепишите












# Замыкание lambda
"""
def pow_(base):
    return lambda value: value ** base

res = pow_(2)
print(res(2))  # -> 4


# Тоже самое но вызов сразу
def pow_(base):
    return lambda x: x**base

print(pow_(2)(3))  # -> 9
"""


# Напишите лямбда-функцию с присвоением переменной и без. Сразу вызов











# Ответ lambda
"""
double = lambda x: x * 2
print(double(2))             # -> 4

# Тоже самое сразу вызываем функцию  Оборачиваем в ()
print((lambda x: x * 2)(2))  # -> 4
"""


# Повторите разные сортировки
from operator import itemgetter, attrgetter
ints = list(range(20))






a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}






class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'

cats = [Cat('Tom', 3), Cat('Angela', 4)]





# Разные Сортировки operator/lambda  Просто перепиши
"""
from operator import attrgetter, itemgetter

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'

if __name__ == '__main__':
    ints = list(range(20))
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, ints))))
    print([i ** 2 for i in range(20) if i % 2 == 0])

    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}
    print(sorted(a_dict.items(), key=lambda x: x[0]))
    print(sorted(a_dict.items(), key=itemgetter(1)))
    
    # Двойная сортировка в кортеже - Унарный минус работает только с числами!!! Работает как  reverse=True  Но к элементу
    print(sorted(a_dict.items(), key=lambda x: (-x[1], x[0])))
    
    cats = [Cat('Tom', 3), Cat('Angela', 4)]
    print(sorted(cats, key=lambda x: x.age))
    print(sorted(cats, key=attrgetter('age')))
    print(sorted(cats, key=attrgetter('name')))
"""



# Написать Решение с nonlocal и Решение с global   Переписать рещение выше чтобы НЕ было ошибки
# Ошибка UnboundLocalError:
"""
# Пример ошибки nonlocal:           Пример ошибки global:
x = 10                              x = 10
def foo():                          def foo():
    x = 10                              print(x)
    def bar():                          x += 1
        print(x)                    foo()
        x += 1                      # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    bar()
    print(x)
foo()
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
"""













# Ответ
"""
# Решение с nonlocal:                       Решение с global:
x = 10                                      x = 10
def foo():                                  def foo():
    x = 10                                      global x, z    # МОЖЕТ создать z 
    def bar():                                  print(x)
        nonlocal x # не может создать z         x += 1
        print(x)                                z = 100
        x += 1
    bar()
    #print(x)                               foo()    # -> 10
foo()      # -> 10, 11                      print(x) # -> 11   меняет x
print(x)   # -> 10  не меняет x             print(z) # -> 100  СОЗДАЕТ z
"""



# Использовать heapq       Можно найти минимальный или максимальный элемент

h = [20, 10, 1, 2]









# Пример heapq
"""
import heapq
h = [20, 10, 1]
print(h)          # -> [20, 10, 1]
heapq.heapify(h)  # создаем кучу(heap)
print(h)          # -> [1, 10, 20]
print(h[0])       # -> 1
heapq.heappop(h) 
print(h)          # -> [10, 20]
print(h[0])       # -> 10

# Мин/Мах элементы первый параметр сколько элементов нужно вывести
h = [20, 10, 1]
print(heapq.nsmallest(2, h))  # -> [1, 10]
print(heapq.nlargest(2, h))   # -> [20, 10]
"""


# Написать Рекурсию сумма Входного списка  Проверьте assert









# Пример Рекурсия со Списком(list):
"""
def my_sum(a_list: list) -> int:
   if not a_list:
       return 0
   if len(a_list) == 1:
       return a_list[0]
   return a_list[0] + my_sum(a_list[1:])


if __name__ == '__main__':
    print(my_sum([10, 20, 30]))  # -> 60
    assert my_sum([]) == 0
    assert my_sum([1]) == 1
    assert my_sum([-1]) == -1
    assert my_sum([2, 2]) == 4
    assert my_sum([1, 2, 3]) == 6
"""


# Использовать __slots__ Написать класс  no_slots/with_slots  Замерить размер структур  asizeof.asizeof/sys.getsizeof











# __slots__
"""
import sys
from pympler import asizeof

class NoSlots: pass
class WithSlots: __slots__ = ('a', 'b', 'c')

no_slots = NoSlots()
with_slots = WithSlots()

print(sys.getsizeof(with_slots))          # -> 56    # sys.getsizeof не учитывается «содержимое объекта», такое как словарь:
print(sys.getsizeof(no_slots))            # -> 56    # sys.getsizeof не учитывается «содержимое объекта», такое как словарь:
print(sys.getsizeof(no_slots.__dict__))   # -> 296   # Разница в потреблении памяти     БЕЗ __slots__
print(asizeof.asizeof(no_slots.__dict__)) # -> 296   # Разница в потреблении памяти     БЕЗ __slots__
print(asizeof.asizeof(no_slots))          # -> 352   # Разница в потреблении памяти     БЕЗ __slots__
print(asizeof.asizeof(with_slots))        # -> 56    # Разница в потреблении памяти     __slots__
print(no_slots.__dict__)                  # -> {}    Есть __dict__    БЕЗ __slots__



# Демонстрация __slots__ :
class Child:                                                class Child:
    __slots__ = ()  # Нельзя создавать атрибуты                 __slots__ = ('name',)  # Можно создать только указанные
b = Child()                                                 b = Child()
b.name = 'a'                                                b.name = 'a'
# AttributeError: 'Child' object has no attribute 'name'    b.name  # -> a
"""


# Использовать __slots__ в dataclasses











# __slots__ в dataclasses
"""
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: int = 0
    y: int = 0

p = Point()
p.__dict__  # -> AttributeError: 'Point' object has no attribute '__dict__'. Did you mean: '__dir__'?
p.a = 10    # -> AttributeError: 'Point' object has no attribute 'a'
"""




# Напишите Singleton











# Пример Singleton/Одиночка  # id Одинаковые     Гарантируется, что объект всегда будет один и тот же.
"""
class Singleton:
   instance = None

   def __new__(cls, *args, **kwargs):
       if cls.instance is None:
           cls.instance = super().__new__(cls)
       return cls.instance

sing = Singleton()
print(id(sing))         # -> 2796516321616   # id Одинаковые
sing_1 = Singleton()
print(id(sing_1))       # -> 2796516321616   # id Одинаковые
"""

# Пример Обычный класс  # id Разные
"""
class Singleton:
    pass

sing = Singleton()
print(id(sing))        # -> 1742792644624     # id Разные
sing_1 = Singleton()
print(id(sing_1))      # -> 1742792644240     # id Разные
"""

# Напишите Monostate












# Пример Моносостояние (Аналог Singleton)  # При создании экземпляра всем экземплярам присваивается ссылка на один и тот же словарь
"""
class Monostate:
   _shared_state = {'a': 1, 'b': 2}

   def __init__(self):
       self.__dict__ = self._shared_state

mono = Monostate()
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {'a': 1, 'b': 2}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {'a': 9999999999, 'b': 2}
print(mono_1.__dict__)  # -> {'a': 9999999999, 'b': 2}

"""

# Пример Monostate Обычный класс  # Смотри на словарь
"""
class Monostate:
    pass

mono = Monostate()
print(mono.__dict__)    # -> {}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {}
print(mono_1.__dict__)  # -> {'a': 9999999999}
"""


# Как создать класс без слова class?  И Создать такой же обычный class и dataclass










# Kласс можно создать без использования ключевого слова class, используя типы type:
"""
MyClass = type('MyClass', (), {'x': 42, 'foo': lambda self: self.x})
my_ = MyClass()
print(my_.x)       # -> 42 
print(my_.foo())   # -> 42
"""

# Тоже самое что и выше но с ключевым словом class!
"""
class MyClass:
   x = 42
   foo = lambda self: self.x  # Тоже самое что и функция ниже
   
   def foo(self):
       return self.x

my_ = MyClass()
print(my_.x)       # -> 42
print(my_.foo())   # -> 42
"""



# Использовать setattr/delattr/hasattr/getattr






# Использовать setattr/delattr/hasattr/getattr

# getattr(object, name)
# getattr(object, name, default)

# setattr(object, name, value)

# delattr(object, name)
# hasattr(object, name)
"""
from dataclasses import dataclass

@dataclass
class New:
    name: str = 'Chuck Norris'
    surname: str = 'Sasya'
    number: int = 10

setattr(New, 'name', 'SuperSasya')   # установили новый атрибут
delattr(New, 'surname')              # удалили атрибут
hasattr(New, 'surname')              # False
getattr(New, 'name')                 # 'SuperSasya'


getattr(New, 'AAAA', 'HEHE')         # HEHE
getattr(New, 'AAAA')                 # AttributeError: type object 'New' has no attribute 'AAAA'
"""



# Создайте класс с property: Создайте функции для управления получением, установкой и удалением атрибута







# __get__, __set__, __delete__
# Дескриптор — это то, как реализован тип Python property
# Функции/методы, связанные методы, property, classmethod и staticmethod все они используют эти специальные методы
# для управления доступом к ним с помощью ТОЧЕЧНОГО ПОИСКА.

# Встроенные объектов дескрипторы: classmethod, staticmethod, property, функции в целом
# свойства с property: Создайте функции для управления получением, установкой и удалением атрибута
'''
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x = 10
print(c.x)  # 10


# Примеры Примеры встроенных объектов дескрипторов: classmethod, staticmethod, property, функции в целом      <-----
def has_descriptor_attrs(obj):
    return set(['__get__', '__set__', '__delete__']).intersection(dir(obj))

def is_descriptor(obj):
    """obj can be instance of descriptor or the descriptor class"""
    return bool(has_descriptor_attrs(obj))

def has_data_descriptor_attrs(obj):
    return set(['__set__', '__delete__']) & set(dir(obj))

def is_data_descriptor(obj):
    return bool(has_data_descriptor_attrs(obj))



# Мы можем видеть, что это classmethod и staticmethod и функции в целом есть Non-Data-Descriptors:
print(is_descriptor(classmethod), is_data_descriptor(classmethod))    # -> True False
print(is_descriptor(staticmethod), is_data_descriptor(staticmethod))  # -> True False

# Обычные функция  Тоже Non-Data-Descriptors
def foo(): pass
my_func = lambda: 5

print(is_descriptor(foo), is_data_descriptor(foo))                    # -> True False
print(is_descriptor(my_func), is_data_descriptor(my_func))            # -> True False

# Только метод __get__
print(has_descriptor_attrs(classmethod))   # -> {'__get__'}
print(has_descriptor_attrs(staticmethod))  # -> {'__get__'}
# Обычные функции __get__
print(has_descriptor_attrs(foo))           # -> {'__get__'}
print(has_descriptor_attrs(my_func))       # -> {'__get__'}



# Дескриптор данных, @property    Data-Descriptor
# @property
print(is_data_descriptor(property))    # -> True
print(has_descriptor_attrs(property))  # -> {'__get__', '__delete__', '__set__'}
'''

# --- Контейнерные типы данных модуля collections ---


# -- class collections.ChainMap(*maps) --
# Использовать ChainMap





# Ответы ChainMap
"""
from collections import ChainMap

first = {1: 1, 2: 2, 3: 3}
second = {4: 4, 5: 5}

chain = ChainMap(first, second)

print(chain)  # -> ChainMap({1: 1, 2: 2, 3: 3}, {4: 4, 5: 5})
chain[1] = 200
print(chain)  # -> ChainMap({1: 200, 2: 2, 3: 3}, {4: 4, 5: 5})
"""



# -- class collections.Counter([iterable-or-mapping]) --
# Использовать Counter





# Ответы Counter
"""
from collections import Counter

counter = Counter('hello')
print(counter)                 # -> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
counter.update('world')
print(counter.most_common(3))  # -> [('l', 3), ('o', 2), ('h', 1)]
"""



# -- class collections.OrderedDict([items]) --
# Использовать OrderedDict






# Ответы OrderedDict
"""
from collections import OrderedDict

first = {1: 1, 2: 2, 3: 3}
second = {2: 2, 1: 1}

order1 = OrderedDict(first)
order2 = OrderedDict(second)
print(order1==order2)                     # -> False
print(order1.popitem(last=False))         # -> (1, 1)
print(order1.move_to_end(3, last=False))  # -> None
print(order1)                             # -> OrderedDict([(3, 3), (2, 2)])
"""



# -- class collections.defaultdict(default_factory=None, /[, ...]) --
# Использовать defaultdict






# Ответы defaultdict
"""
from collections import defaultdict

a_dict = defaultdict(list)
for char in 'hello':
    a_dict[char].append(char)

print(a_dict)  # -> defaultdict(<class 'list'>, {'h': ['h'], 'e': ['e'], 'l': ['l', 'l'], 'o': ['o']})


a_dict = defaultdict(int)
for char in 'hello':
    a_dict[char]+=1

print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))  # -> [('l', 2), ('h', 1), ('e', 1), ('o', 1)]
"""


# -- collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None) --
# Использовать namedtuple






# Ответы namedtuple

"""
from collections import namedtuple

Point = namedtuple('Point', 'x y')

tom = ('Tom', 4, 'yellow')
Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)       # -> Cat(name='Tom', age=4, color='yellow')
print(tom.name)  # -> Tom


Point = namedtuple('Point', ['x', 'y'])  # Тоже самое
Point = namedtuple('Point', 'x y')       # Тоже самое
Point = namedtuple('Point', 'x, y')      # Тоже самое
p = Point(11, y=22)
print(p)                # -> Point(x=11, y=22)

# Поддерживает только getattr!!!                            <-----
print(getattr(p, 'x'))  # -> 11
d = {'x': 11, 'y': 22}
print(Point(**d))       # -> Point(x=11, y=22)
"""



# -- class collections.deque([iterable[, maxlen]]) --
# Использовать deque






# Ответы deque
"""
from collections import deque


a_deque = deque([1, 2, 3], maxlen=3)
print(a_deque)     # -> deque([1, 2, 3], maxlen=3)
a_deque.append(4)
print(a_deque)     # -> deque([2, 3, 4], maxlen=3)


a_deque = deque()
a_deque.append(1)
# a_deaue.pop(1)         # -> TypeError: deque.popleft() takes no arguments (1 given)
print(a_deque)
a_deque.appendleft(2)    # -> deque([1])
# a_deaue.popleft(2)     # -> TypeError: deque.popleft() takes no arguments (1 given)
print(a_deque)           # -> deque([2, 1])


# deque НЕ поддерживает pop(1)/popleft(1) с аргументом(Индексом)

b_list = list([1, 2])
b_list.pop(0)
print(b_list)  # -> [2]

b_deque = deque([1, 2])
b_deque.pop(1)      # -> TypeError: deque.pop() takes no arguments (1 given)
b_deque.popleft(1)  # -> TypeError: deque.popleft() takes no arguments (1 given)
"""



# --- Модуль itertools в Python, эффективные итераторы для циклов   - сборник полезных итераторов --- ---

# --- Бесконечные итераторы   Infinite iterators ---


# itertools.count(start=0, step=1)
# Использовать count







# Ответы count
"""
from itertools import count
for i in count(10):
    if i > 15:
        break
    else:
        print(i, end=' ')  # 10 11 12 13 14 15


# Другой способ ограничить вывод бесконечного итератора - использовать другую функцию из itertools с именем islice().
from itertools import islice, count

for i in islice(count(10), 5):
    print(i, end=' ')  # 10 11 12 13 14
    
    
print(list(islice(count(10), 2, 5)))  # -> [12, 13, 14]
"""




# itertools.cycle(iterable)
# Использовать cycle






# Ответы cycle
"""
from itertools import cycle, islice

for index, value in enumerate(cycle('XYZ')):
    if index > 5:
        break
    print(value, end=' ')
# X Y Z X Y Z


# Пример с islice
for i in islice(cycle([1, 2, 3]), 5):
    print(i, end=' ')  # 1 2 3 1 2 
"""



# itertools.repeat(object[, times])
# Использовать repeat








# Ответы repeat
"""
from itertools import repeat

print(list(repeat(10, 3)))  # -> [10, 10, 10]


# Обычное использование для itertools.repeat() - предоставить поток постоянных значений для map() или zip():

# квадраты элементов списка
print(list(map(pow, range(10), repeat(2))))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 
# кубы элементов списка
print(list(map(pow, range(10), repeat(3))))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Интересный пример с zip
fruits = ['apples', 'oranges', 'bananas']

# Initialize inventory to zero for each fruit type.
inventory = dict(zip(fruits, repeat(2)))
print(inventory)  # -> {'apples': 2, 'oranges': 2, 'bananas': 2}

inventory = dict(zip(fruits, repeat(0)))
print(inventory)  # -> {'apples': 0, 'oranges': 0, 'bananas': 0}


# Классный пример 
from itertools import chain, repeat, cycle

fruits = ['apples', 'oranges', 'bananas', 'pineapples','grapes',"berries"]

inventory = list(zip(fruits, chain(repeat(10, 2), cycle(range(1, 3)))))
print(inventory)  # -> [('apples', 10), ('oranges', 10), ('bananas', 1), ('pineapples', 2), ('grapes', 1), ('berries', 2)]
"""



# --- Конечные итераторы    Iterators terminating on the shortest input sequence ---
# --- Итераторы, оканчивающиеся на самой короткой входной последовательности ---


# itertools.accumulate(iterable[, function, *, initial=None])
# Использовать accumulate









# Ответы accumulate
"""
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4, 5])))  # -> [1, 3, 6, 10, 15]
print(list(accumulate([1, 2, 3, 4, 5], initial=100)))  # -> [100, 101, 103, 106, 110, 115]
print(list(accumulate([1, 2, 3, 4, 5], operator.mul)))  # -> [1, 2, 6, 24, 120]
print(list(accumulate([1, 2, 3, 4, 5], operator.sub)))  # -> [1, -1, -4, -8, -13]
"""



# itertools.batched(iterable, n)  Работает с версии Питона 3.12 +
# Использовать batched




# Ответы batched
"""
from itertools import batched
flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
unflattened = list(batched(flattened_data, 2))
print(unflattened)  # -> [('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]
"""





# itertools.chain(*iterables)
# Использовать chain








# Ответы chain
"""
from itertools import chain
A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set
D = {'A': '11', 'B': '22'}  # dict

G = list(chain(A, B, C, D))
L = [*chain(A, B, C, D)]    # Тоже самое

print(L)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7, 'A', 'B']
print(G)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7, 'A', 'B']

# НЕ распакует вложенные без *
print(list(chain([[1, 2, 3]])))   # -> [[1, 2, 3]]
print(list(chain(*[[1, 2, 3]])))  # -> [1, 2, 3]
"""




# classmethod chain.from_iterable(iterable)
# Использовать chain.from_iterable









# Ответы chain.from_iterable

"""
from itertools import chain

lst = ['foo', ['one', 'two', [1, 2]]]

# Сравнение chain vs chain.from_iterable

# itertools.chain(*iterables)
print(list(chain.from_iterable(lst)))  # -> ['f', 'o', 'o', 'one', 'two', [1, 2]]
print([*chain.from_iterable(lst)])     # -> ['f', 'o', 'o', 'one', 'two', [1, 2]]


# chain.from_iterable(iterable)
print(list(chain(lst)))                 # -> ['foo', ['one', 'two', [1, 2]]]
print([*chain(lst)])                    # -> ['foo', ['one', 'two', [1, 2]]]
"""



# itertools.compress(data, selectors)
# Использовать compress





# Ответы compress
"""
from itertools import compress
print(list(compress('ABCDEF', [1,0,1,0,1,1])))  # -> ['A', 'C', 'E', 'F']        
print([*compress('ABCDEF', [1,0,1,0,1,1])])     # -> ['A', 'C', 'E', 'F']    
"""



# itertools.dropwhile(predicate, iterable)
# Использовать dropwhile





# Ответы dropwhile
"""
from itertools import dropwhile
# Пример 1
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  # -> [6, 4, 1]

# Пример 2
def trigger_to_five(x):
    return x > 5

lst = [6, 7, 8, 9, 1, 2, 3, 10]
print(list(dropwhile(trigger_to_five, lst)))  # -> [1, 2, 3, 10]
"""


# itertools.takewhile(predicate, iterable)
# Использовать takewhile





# Ответы takewhile
"""
from itertools import takewhile, dropwhile

print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))    # -> [1, 4]

print((list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))))  # -> [6, 4, 1]
"""



# itertools.filterfalse(predicate, iterable)
# Использовать filterfalse





# Ответы filterfalse
"""
from itertools import filterfalse

print(list(filterfalse(lambda x: x > 5, [6, 7, 8, 9, 1, 2, 3, 10])))  # -> [1, 2, 3]
print(list(filterfalse(lambda x: x < 5, [6, 7, 8, 9, 1, 2, 3, 10])))  # -> [6, 7, 8, 9, 10]
print(list(filterfalse(lambda x: x % 2 == 0, [6, 7, 8, 9])))          # -> [7, 9]
"""



# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop[, step])
# Использовать islice





# Ответы islice
"""
from itertools import islice
from more_itertools import islice_extended

a_gen = (i for i in range(10))
print(list(itertools.islice(a_gen, None, 5)))  # -> [0, 1, 2, 3, 4]


a_gen = (i for i in range(10))

# Используем islice_extended для отрицательных индексов
print(list(islice_extended(a_gen, None, None, -1)))  # -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(list(islice(a_gen, None, None, -1)))  # -> ValueError: Step for islice() must be a positive integer or None.


# Используем срезов slice()
print(list([1, 2, 3][slice(None, 2)]))         # -> [1, 2]
print(list([1, 2, 3][slice(None, None, -1)]))  # -> [3, 2, 1]
"""


# itertools.pairwise(iterable)
# Использовать pairwise





# Ответы pairwise
"""
from itertools import pairwise
result = pairwise([1, 2, 3])

print(list(result))  # -> [(1, 2), (2, 3)]
"""


# itertools.starmap(function, iterable)
# Использовать starmap





# Ответы starmap
"""
from itertools import starmap

x = starmap(max, [(2, 5, 4), (3, 2, 1), (10, 3, 8)])
print(list(x))  # -> [5, 3, 10]


# Пример 1: Важно Понимать отличие примера     map   vs   starmap
def add_plus(a, b):
    return a + b


for item in starmap(add_plus, [(2, 3), (4, 5)]):
    print(item, end=' ')
# 5 9
print()

for item in map(add_plus, [(2, 3)], [(4, 5)]):
    print(item, end=' ')
print()
# (2, 3, 4, 5)
for item in map(add_plus, [2, 3], [4, 5]):
    print(item, end=' ')
# 6 8
"""


# itertools.tee(iterable, n=2)
# Использовать tee





# Ответы tee
"""
from itertools import tee

rez = tee([1, 2, 3], 3)
print([list(i) for i in rez])  # -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""




# itertools.zip_longest(*iterables, fillvalue=None)
# Использовать zip_longest





# Ответы zip_longest
"""
from itertools import zip_longest

rez = zip_longest([1, 2], [1, 2, 3], fillvalue=100)
print(list(rez))  # -> [(1, 1), (2, 2), (100, 3)]


# встроенная функция zip()
rez = zip([1, 2], [1, 2, 3])
print(list(rez))  # -> [(1, 1), (2, 2)]
"""



# itertools.groupby(iterable, key=None)
# Повтори from itertools import groupby

res = 'AAAABBBCCDAABBB'








# Пример from itertools import groupby
"""
from itertools import groupby
[k for k, g in groupby('AAAABBBCCDAABBB')] #→ A B C D A B    # -> ['A', 'B', 'C', 'D', 'A', 'B']
[list(g) for k, g in groupby('AAAABBBCCD')]#→ AAAA BBB CC D  # -> [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
"""




# --- Комбинаторные итераторы   Combinatoric iterators ---


# itertools.product(*iterables, repeat=1)
# Использовать product





# Ответы product
"""
from itertools import product

print(list(product([1, 2], repeat=2)))  # -> [(1, 1), (1, 2), (2, 1), (2, 2)]
print(list(product([1, 2], repeat=3)))  # -> [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

pairs = ['Aa', 'Bb']
gams = list([x for x in product(*pairs)])
print(gams)  # -> [('A', 'B'), ('A', 'b'), ('a', 'B'), ('a', 'b')]
"""


# itertools.permutations(iterable, r=None)
# Использовать permutations





# Ответы permutations
"""
from itertools import permutations

print(list(permutations('XY', 2)))  # -> [('X', 'Y'), ('Y', 'X')]
print(list(permutations('XYZ', 3)))
# [('X', 'Y', 'Z'), ('X', 'Z', 'Y'), ('Y', 'X', 'Z'), ('Y', 'Z', 'X'), ('Z', 'X', 'Y'), ('Z', 'Y', 'X')]
"""



# itertools.combinations(iterable, r)
# Использовать combinations





# Ответы combinations
"""
from itertools import combinations

print(list(combinations('XYZ', 2)))  # -> [('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
print(list(combinations('XYZ', 3)))  # -> [('X', 'Y', 'Z')]
"""



# itertools.combinations_with_replacement(iterable, r)
# Использовать combinations_with_replacement





# Ответы combinations_with_replacement
"""
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('XYZ', 2)))  # -> [('X', 'X'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Y'), ('Y', 'Z'), ('Z', 'Z')]
print(list(combinations_with_replacement('XYZ', 3)))
# [('X', 'X', 'X'), ('X', 'X', 'Y'), ('X', 'X', 'Z'), ('X', 'Y', 'Y'), ('X', 'Y', 'Z'), ('X', 'Z', 'Z'), ('Y', 'Y', 'Y'),
# ('Y', 'Y', 'Z'), ('Y', 'Z', 'Z'), ('Z', 'Z', 'Z')]
"""



# --- Отличия    combinations  vs  combinations_with_replacement vs  permutations ---






# Ответ
#  --- Отличия    combinations  vs  combinations_with_replacement vs  permutations ---
"""
from itertools import permutations, combinations, combinations_with_replacement

print(list(permutations('XY', 2)))                    # -> [('X', 'Y'), ('Y', 'X')]
print(list(combinations('XY', 2)))                    # -> [('X', 'Y')]
print(list(combinations_with_replacement('XY', 2)))   # -> [('X', 'X'), ('X', 'Y'), ('Y', 'Y')]
"""





# --- functools — Функции высшего порядка и операции над вызываемыми объектами ---


# functools.reduce(function, iterable[, initializer])
# Напишите from functools import reduce/eval   Используя lambda/operator   eval - НЕ забудь

lst = [1, 2, 3, 4]










# Ответ  reduce/eval   lambda/operator
"""
import functools, operator
lst = [1, 2, 3, 4]
print(functools.reduce(operator.add, lst))      # -> 10
print(functools.reduce(lambda x, y: x+y, lst))  # -> 10
# Тоже самое
print(eval('+'.join([str(i) for i in lst])))    # -> 10
print(eval('+'.join(map(str, lst))))            # -> 10
"""


# @functools.cache(user_function)
# Использовать cache






# Ответ @functools.cache(user_function)
"""
from functools import cache
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(10))  # -> 3628800
print(factorial(5))   # -> 120
print(factorial(12))  # -> 479001600
"""




# @functools.lru_cache(user_function)
# @functools.lru_cache(maxsize=128, typed=False)
# Напишите Фибоначчи с кэшем и замер скорости работы timeit   globals=globals()/setup="from __main__ import fibonacci__3"










# Решения Фибоначч с мемоизацией КЭШ  Скорость O(n)  @functools.lru_cache
"""
import timeit
from pympler import asizeof
from functools import lru_cache

@__import__('functools').lru_cache(maxsize=None)  #  Так тоже можно импортировать
# @functools.lru_cache(maxsize=None)
def fibonacci__3(n):
    if n < 2:
        return n
    else:
        return fibonacci__3(n - 1) + fibonacci__3(n - 2)

print(fibonacci__3(50))                                                              # -> 12586269025
# Замеры с параметром 50!!!
print(timeit.timeit('fibonacci__3(50)', globals=globals()))                          # -> 0.10358340013772249

# Тоже самое но с setup()
print(timeit.timeit('fibonacci__3(50)', setup="from __main__ import fibonacci__3"))  # -> 0.09871609997935593
"""



# functools.partial(func, /, *args, **keywords)
# Используйте функцию from functools import partial


def multiply(x, y):
    return x * y









# partial функция from functools import partial
"""
from functools import partial

def multiply(x, y):
    return x * y

doubleNum = partial(multiply, 2)
tripleNum = partial(multiply, 3)
res = multiply(10, 2)

print(res)  # 20
print(multiply(10, 2))  # 20
print(doubleNum(20))  # 40
print(tripleNum(20))  # 60
"""




# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 1) Написать декоратор, который выводит на экран время работы произвольной функции и используем   from functools import wraps









# Ответ 1)
"""
from functools import wraps
from time import time, perf_counter

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        finish = perf_counter()
        print(f"Время выполнения функции '{func.__name__}': {finish - start:.4f} секунд")
        return res
    wrapper.__name__ = func.__name__   # Тоже самое что   @wraps(func)  Только ручное  
    wrapper.__doc__ = func.__doc__     # Тоже самое что   @wraps(func)  Только ручное
    return wrapper

@timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
example_function(1000000)  # -> Время выполнения функции 'example_function': 0.0738 секунд
"""


# 1.1) Написать Класс как ДЕКОРАТОР, который выводит на экран время работы произвольной функции:










# Ответ 1.1)
# Класс как ДЕКОРАТОР
"""
from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция {self.fn.__name__} отработала за {finish - start}")
        return result

@Timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
example_function(1000000)  # -> Время выполнения функции 'example_function': 0.0738 секунд
"""

# 1.2) Написать dataclass










# Ответ 1.2)
# Декорирование класса в Python:
"""
from dataclasses import dataclass
@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity: int = 0

item = InventoryItem(name="HEHE", unit_price=12, quantity=100)
print(item.__dict__)  # -> {'name': 'HEHE', 'unit_price': 12, 'quantity': 100}
"""


# 1.3) Сделать по умолчанию пустой список  Сравнение __eq__()  уже встроенно в dataclass










# Ответ 1.3)
# Сделать по умолчанию пустой список  Сравнение __eq__()  уже встроенно в dataclass
"""
from dataclasses import dataclass, field

@dataclass
class Foo:
    n: int
    s: str = 'a'
    items: list[str] = field(default_factory=list)  # <-- и всё это - чтобы по умолчанию был пустой список

f = Foo(1)
f1 = Foo(1)

print(f.__dict__)    # -> {'n': 1, 's': 'a', 'items': []}
print(f.__eq__(f1))  # -> True
print(f == f1)       # -> True

ff = Foo(11111)
ff1 = Foo(1)
print(ff.__eq__(ff1))  # -> False
print(ff == ff1)       # -> False
"""


# 1.4) Использовать Pydantic







# Ответ 1.4)
# Сравните это с пидантиком(Pydantic), в котором, кажется, думают о людях:
"""
from pydantic import BaseModel

class MyDate(BaseModel):
    n: int
    s: str = 'a'
    items: list[str] = []

m = MyDate(n=1)
m1 = MyDate(n=1)

print(m.__dict__)    # -> {'n': 1, 's': 'a', 'items': []}

print(m == m1)       # -> True
print(m.__eq__(m1))  # -> True


# Так будет ошибка  <-----   Важно 
mm = MyDate(1)
mm1 = MyDate(1)
"""




# 2) Написать декоратор, который возвращает либо результат, либо экземпляр исключения:











# Ответ 2)
"""
def safe_decorator(func):
   @__import__('functools').wraps(func)
   def wrapper(*args, **kwargs):
       try:
           return func(*args, **kwargs)
       except ZeroDivisionError as e:
           return e
   return wrapper

@safe_decorator
def divide(a, b):
    return a / b

print(divide(10, 0))  # -> division by zero
print(divide(10, 2))  # -> 5.0
"""


# Напишите декоратор с ПАРАМЕТРАМИ/Аргументами












# ДЕКОРАТОР С ПАРАМЕТРАМИ - ЭТО ДОБАВЛЕНИЕ ЕЩЕ ОДНОГО УРОВНЯ ВЛОЖЕННОСТИ ДЛЯ ТОГО ЧТОБЫ ПЕРЕДАТЬ КАКОЙ-ТО ПАРАМЕТР А
# ВНУТРИ ЛЕЖИТ ОБЫЧНЫЙ ДЕКОРАТОР.
"""
def typed(type_):  # ->   Добавили уровень вложенности
    def real_decorator(function):  # ->   Внутри обычный декоратор
        @__import__('functools').wraps(function)
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип должен быть {type_}')
            return function(*args)
        return wrapper
    return real_decorator  # ->   нужно вернуть еще одну функцию как и другие вложенности

@typed(int)  # @real_decorator
def calculate(a, b, c):
    # Logic
    return a + b + c

@typed(str)  # @real_decorator
def convert(a, b):
    # Logic
    return a + b

if __name__ == '__main__':
    # calculate = typed(int)(calculate) # Под капотом работает так! Ручное декорирование без @             <-----
    print(calculate(2, 2, 2))           
    print(convert('1', 'hello'))            
    # convert = typed(str)(convert)     # Под капотом работает так! Ручное декорирование без @             <-----
"""



# 3) Написать генератор Фибоначчи от a и b.  Вывести первые 10 чисел Фибоначчи









# Ответ 3)
"""
def fibonacci_generator(a, b):
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fib_gen = fibonacci_generator(1, 1)
for _ in range(10):
    print(next(fib_gen), end=' ')  # Выведет первые 10 чисел Фибоначчи              # -> 1 1 2 3 5 8 13 21 34 55
"""

# 4) Получить из файла текст в юникоде.










# Ответ 4)
"""
def read_unicode_file(file_path):
   with open(file_path, 'r', encoding='utf-8') as f:
       content = f.read()
   return content

# Пример использования
текст = read_unicode_file('path_to_your_file.txt')
print(текст)
"""

# 5) Написать генератор чисел Фибоначчи вида def fib(a=1, b=2):








# Ответ 5)
"""
def fib(a=1, b=2):
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fib_gen = fib()
[print(next(fib_gen), end=' ') for _ in range(10)]
# Выведет первые 10 чисел Фибоначчи начиная с a=1, b=2  # -> 1 2 3 5 8 13 21 34 55 89
"""



# Создать Абстрактный класс  и Унаследоваться от него     from abc import ABC, abstractmethod










"""
# Создать Абстрактный класс  и Унаследоваться от него     from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

s = Shape()  # -> TypeError: Can't instantiate abstract class Shape with abstract method area

class MyClass(Shape):
    pass

c = MyClass()  # -> TypeError: Can't instantiate abstract class Shape with abstract method area


# Всё работает
class MyClass(Shape):
    def area(self):
        return 1000

c = MyClass()
print(c.area())  # -> 1000
"""


# Написать Асинхронный код













# Ответ Асинхронный код
"""
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello")

async def world():
    await asyncio.sleep(2)
    print("World")

async def main():
    await asyncio.gather(hello(), world())

if __name__ == '__main__':
    asyncio.run(main())
"""


# Как запустить что-то в потоке и вывести результат?   from concurrent.futures import ThreadPoolExecutor











"""
# Как запустить что-то в потоке и вывести результат?  ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

fn = lambda: 5
with ThreadPoolExecutor(max_workers=5) as pool:
    future = pool.submit(fn)
    print(future.result())  # -> 5

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 10, 3)
    print(future.result())  # -> 1000.0
"""


# Как запустить что-то в Процессах и вывести результат?   # lambda не сериализуется pickle   ProcessPoolExecutor











"""
# Как запустить что-то в Процессах и вывести результат? 

from concurrent.futures import ProcessPoolExecutor

# lambda не сериализуется pickle
fn = lambda: 5

if __name__ == "__main__":
# Создание ProcessPoolExecutor с 4 рабочими процессами
    with ProcessPoolExecutor(max_workers=4) as executor:
        future = executor.submit(fn)
        result = future.result()
        print(result)  # -> 16
# _pickle.PicklingError: Can't pickle <function <lambda> at 0x000001C4AA9B8860>: attribute lookup <lambda> on __main__ failed



# Так будет работать

def task_function(param):
    return param ** 5

if __name__ == "__main__":
# Создание ProcessPoolExecutor с 4 рабочими процессами
    with ProcessPoolExecutor(max_workers=4) as executor:
        future = executor.submit(task_function, 10)
        result = future.result()
        print(result)  # -> 100000
"""





# --- Алгоритмы сортировки Python ---




# Задача с собеседования
# Написать Quick Sort/Быстрая сортировка








# Реализация Quick Sort/Быстрая сортировка
"""
# Вариант 1: Опорный элемент — последний элемент массива
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    middle = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)
            
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)  # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]



# Вариант 2: Опорный элемент — средний элемент массива
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr)//2
    pivot = arr[pivot_index]
    left = []
    right = []
    middle = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)

    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)  # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]



# Вариант 3: Случайный выбор опорного элемента

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Случайный опорный элемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)  # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]
"""


# Написать Сортировку пузырьком (Bubble Sort)











# Сортировка пузырьком (Bubble Sort)
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("(Bubble Sort):", sorted_arr) # -> (Bubble Sort): [11, 12, 22, 25, 34, 64, 90]
"""


# Написать Сортировку выбором (Selection Sort)











# Сортировка выбором (Selection Sort)
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("(Selection Sort):", sorted_arr)  # -> (Selection Sort): [11, 12, 22, 25, 64]
"""



# Написать Сортировку вставками (Insertion Sort)











# Сортировка вставками (Insertion Sort)
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11]
sorted_arr = insertion_sort(arr)
print("(Insertion Sort):", sorted_arr)  # -> (Insertion Sort): [11, 12, 22, 25, 34, 64]
"""



# Написать Быстрая сортировка (Quick Sort)











# Быстрая сортировка (Quick Sort)
"""
def quick_sort(arr):
    match arr:
        case x if len(x) <= 1:
            return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("(Quick Sort):", sorted_arr)  # -> (Quick Sort): [11, 12, 22, 25, 34, 64, 90]
"""



# Написать Сортировку слиянием (Merge Sort)












# Сортировка слиянием (Merge Sort)
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("(Merge Sort):", sorted_arr)  # -> (Merge Sort): [11, 12, 22, 25, 34, 64, 90]
"""



# Дальше Добавь Другие сортировки...







# Напиши SQL Задачу с собеседования ---






# --- SQL Задача с собеседования ---

"""
Таблицы:
users (пользователи):
    id (INT, PRIMARY KEY)
    name (VARCHAR)
    email (VARCHAR)
    registration_date (DATE)

products (продукты):
    id (INT, PRIMARY KEY)
    name (VARCHAR)
    category (VARCHAR)
    price (DECIMAL)

orders (заказы):
    id (INT, PRIMARY KEY)
    user_id (INT, FOREIGN KEY на users.id)
    product_id (INT, FOREIGN KEY на products.id)
    order_date (DATE)
    quantity (INT)


# Будем сцепляться по id    
select u.name from users as u
left join products as p on u.id = p.id
"""



















































































































































































































































































































































































































































































































































































































