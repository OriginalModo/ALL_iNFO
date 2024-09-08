import asyncio
import collections
import dataclasses
import functools
import heapq
import itertools
import json
import operator
import random
import sys
import time
import types
import re



# Замеры размеров структур Python  ПРОСТО ПОСМОТРЕТЬ!!!
"""
 --- Замеры размеров Python ---

                            -- Примеры Списков deque vs list --                                 <-----
my_list = [1, 2, 3, 4, 5]
print(f'getsizeof list:  {sys.getsizeof(my_list)} байт')     # -> getsizeof list:  104 байт
print(f'asizeof   list:  {asizeof.asizeof(my_list)} байт')   # -> asizeof   list:  264 байт

from collections import deque
my_deque = deque([1, 2, 3, 4, 5])
print(f'getsizeof deque: {sys.getsizeof(my_list)} байт')     # -> getsizeof deque: 104 байт
print(f'asizeof   deque: {asizeof.asizeof(my_deque)} байт')  # -> asizeof   deque: 760 байт



                            -- Примеры Кортежей namedtuple vs tuple --                          <-----
my_tuple = (1, 2, 3, 4, 5)
print(f'getsizeof tuple:       {sys.getsizeof(my_tuple)} байт')    # -> getsizeof tuple:       80 байт
print(f'asizeof   tuple:       {asizeof.asizeof(my_tuple)} байт')  # -> asizeof   tuple:       240 байт

from collections import namedtuple
nt_tuple = namedtuple('nt_tuple', ['a', 'b', 'c', 'd', 'e'])
p = nt_tuple(1, 2, c=3, d=4, e=5)
print(f'getsizeof namedtuple:  {sys.getsizeof(p)} байт')           # -> getsizeof namedtuple:  80 байт
print(f'asizeof   namedtuple:  {asizeof.asizeof(p)} байт')         # -> asizeof   namedtuple:  240 байт



                            -- Примеры Словарей OrderedDict vs dict --                          <-----
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(f'getsizeof dict:         {sys.getsizeof(my_dict)} байт')     # -> getsizeof dict:       224 байт
print(f'asizeof   dict:         {asizeof.asizeof(my_dict)} байт')   # -> asizeof   dict:       488 байт


from collections import OrderedDict
or_dict = OrderedDict({1: 'a', 2: 'b', 3: 'c'})

print(f'getsizeof OrderedDict:  {sys.getsizeof(or_dict)} байт')    # -> getsizeof OrderedDict: 448 байт
print(f'asizeof   OrderedDict:  {asizeof.asizeof(or_dict)} байт')  # -> asizeof   OrderedDict: 712 байт



                            -- Примеры Множества frozenset vs set --                            <-----
my_set = {1, 2, 3, 4, 5}
print(f'getsizeof set:        {sys.getsizeof(my_set)} байт')     # -> getsizeof set:       472 байт
print(f'asizeof   set:        {asizeof.asizeof(my_set)} байт')   # -> asizeof   set:       632 байт


fz_set = frozenset({1, 2, 3, 4, 5})

print(f'getsizeof frozenset:  {sys.getsizeof(fz_set)} байт')    # -> getsizeof frozenset:  472 байт
print(f'asizeof   frozenset:  {asizeof.asizeof(fz_set)} байт')  # -> asizeof   frozenset:  632 байт

# Если list внутри
fz_set = frozenset([1, 2, 3, 4, 5])

print(f'getsizeof frozenset:  {sys.getsizeof(fz_set)} байт')    # -> getsizeof frozenset:  728 байт
print(f'asizeof   frozenset:  {asizeof.asizeof(fz_set)} байт')  # -> asizeof   frozenset:  888 байт

# Если tuple внутри
fz_set = frozenset((1, 2, 3, 4, 5))

print(f'getsizeof frozenset:  {sys.getsizeof(fz_set)} байт')    # -> getsizeof frozenset:  728 байт
print(f'asizeof   frozenset:  {asizeof.asizeof(fz_set)} байт')  # -> asizeof   frozenset:  888 байт



                            -- Примеры Строки/Числа str vs int --                              <-----
my_string = "Hello, World!"

print(f'getsizeof str:  {sys.getsizeof(my_string)} байт')    # -> getsizeof str:  62 байт
print(f'asizeof   str:  {asizeof.asizeof(my_string)} байт')  # -> asizeof   str:  64 байт


my_int = 10000000000000000000000000000

print(f'getsizeof int:  {sys.getsizeof(my_int)} байт')       # -> getsizeof int:  40 байт
print(f'asizeof   int:  {asizeof.asizeof(my_int)} байт')     # -> asizeof   int:  40 байт



# Чем больше строка тем больше размер так же и с другими обьектами

my_string = "a"

print(f'getsizeof str:  {sys.getsizeof(my_string)} байт')    # -> getsizeof str:  50 байт
print(f'asizeof   str:  {asizeof.asizeof(my_string)} байт')  # -> asizeof   str:  56 байт


my_int = 1

print(f'getsizeof int:  {sys.getsizeof(my_int)} байт')       # -> getsizeof int:  28 байт
print(f'asizeof   int:  {asizeof.asizeof(my_int)} байт')     # -> asizeof   int:  32 байт



                            -- Сравнение slots vs no_slots --                                  <-----
                            -- @dataclass(slots=True)  vs  @dataclass() --
from dataclasses import dataclass

@dataclass(slots=True)
class WithSlots:
    value: int

with_slots = WithSlots(10)
print(f'getsizeof WithSlots:  {sys.getsizeof(with_slots)} байт')    # -> getsizeof WithSlots:  40 байт
print(f'asizeof   WithSlots:  {asizeof.asizeof(with_slots)} байт')  # -> asizeof   WithSlots:  72 байт


@dataclass
class NoSlots:
    value: int

no_slots = NoSlots(10)
print(f'getsizeof NoSlots:    {sys.getsizeof(no_slots)} байт')      # -> getsizeof NoSlots:    56 байт
print(f'asizeof   NoSlots:    {asizeof.asizeof(no_slots)} байт')    # -> asizeof   NoSlots:    440 байт
"""



# Замеры ПУСТЫХ обьектом встроенных Python  ПРОСТО ПОСМОТРЕТЬ!!!
"""
 --- Замеры ПУСТЫХ обьектом встроенных Python ---
 
                            -- Примеры list vs [] vs deque() vs heapq --                       <-----
                            
my_list = list()
print(f'getsizeof list():      {sys.getsizeof(my_list)} байт')    # -> getsizeof list():       56 байт
print(f'asizeof   list():      {asizeof.asizeof(my_list)} байт')  # -> asizeof   list():       56 байт
 
my_list = []
print(f'getsizeof []:          {sys.getsizeof(my_list)} байт')    # -> getsizeof []:           56 байт
print(f'asizeof   []:          {asizeof.asizeof(my_list)} байт')  # -> asizeof   []:           56 байт


from collections import deque

my_deque = deque()
print(f'getsizeof deque():     {sys.getsizeof(my_deque)} байт')    # -> getsizeof deque():     760 байт
print(f'asizeof   deque():     {asizeof.asizeof(my_deque)} байт')  # -> asizeof   deque():     760 байт


import heapq

my_heapq = []
heapq.heapify(my_heapq)
print(f'getsizeof heapq:       {sys.getsizeof(my_heapq)} байт')    # -> getsizeof heapq:       56 байт
print(f'asizeof   heapq:       {asizeof.asizeof(my_heapq)} байт')  # -> asizeof   heapq:       56 байт





                            -- Примеры set() vs frozenset() --                                 <-----

my_set = set()
print(f'getsizeof set():       {sys.getsizeof(my_set)} байт')    # -> getsizeof set():         216 байт
print(f'asizeof   set():       {asizeof.asizeof(my_set)} байт')  # -> asizeof   set():         216 байт
  
my_set = frozenset()
print(f'getsizeof frozenset(): {sys.getsizeof(my_set)} байт')    # -> getsizeof frozenset():   216 байт
print(f'asizeof   frozenset(): {asizeof.asizeof(my_set)} байт')  # -> asizeof   frozenset():   216 байт





                            -- Примеры tuple() vs namedtuple() --                               <-----
my_tuple = tuple()
print(f'getsizeof tuple():    {sys.getsizeof(my_tuple)} байт')    # -> getsizeof tuple():       40 байт
print(f'asizeof   tuple():    {asizeof.asizeof(my_tuple)} байт')  # -> asizeof   tuple():       40 байт


from collections import namedtuple

my_tuple = namedtuple('C', '')
nt_tuple = my_tuple()
print(f'getsizeof namedtuple: {sys.getsizeof(nt_tuple)} байт')    # -> getsizeof namedtuple:    40 байт
print(f'asizeof   namedtuple: {asizeof.asizeof(nt_tuple)} байт')  # -> asizeof   namedtuple:    40 байт





                            -- Примеры dict() vs {} vs OrderedDict() vs defaultdict() vs ChainMap() --        <-----
my_dict = dict()
print(f'getsizeof dict():       {sys.getsizeof(my_dict)} байт')      # -> getsizeof dict():       64 байт
print(f'asizeof   dict():       {asizeof.asizeof(my_dict)} байт')    # -> asizeof   dict():       64 байт


my_dict = {}
print(f'getsizeof {{}}:         {sys.getsizeof(my_dict)} байт')      # -> getsizeof {}:           64 байт
print(f'asizeof   {{}}:         {asizeof.asizeof(my_dict)} байт')    # -> asizeof   {}:           64 байт


from collections import OrderedDict
 
my_OrDt = OrderedDict()
print(f'getsizeof OrderedDict:  {sys.getsizeof(my_OrDt)} байт')      # -> getsizeof OrderedDict:  128 байт
print(f'asizeof   OrderedDict:  {asizeof.asizeof(my_OrDt)} байт')    # -> asizeof   OrderedDict:  128 байт


from collections import defaultdict

my_defa = defaultdict(int)     # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(str)     # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(list)    # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(set)     # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(dict)    # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict()        # Все будут весить ОДИНАКОВО!!!
print(f'getsizeof defaultdict():  {sys.getsizeof(my_defa)} байт')    # -> getsizeof defaultdict():  72 байт
print(f'asizeof   defaultdict():  {asizeof.asizeof(my_defa)} байт')  # -> asizeof   defaultdict():  72 байт


from collections import ChainMap
 
my_chain = ChainMap()
print(f'getsizeof ChainMap():  {sys.getsizeof(my_chain)} байт')    # -> ggetsizeof ChainMap():  56 байт
print(f'asizeof   ChainMap():  {asizeof.asizeof(my_chain)} байт')  # -> aasizeof   ChainMap():  536 байт





                            -- Сравнение slots vs no_slots --                                  <-----
                            -- @dataclass(slots=True)  vs  @dataclass() --
                            
from dataclasses import dataclass

@dataclass(slots=True)
class WithSlots:pass

with_slots = WithSlots()
print(f'getsizeof WithSlots:  {sys.getsizeof(with_slots)} байт')    # -> getsizeof WithSlots:  32 байт
print(f'asizeof   WithSlots:  {asizeof.asizeof(with_slots)} байт')  # -> asizeof   WithSlots:  32 байт


@dataclass
class NoSlots:pass

no_slots = NoSlots()
print(f'getsizeof NoSlots:    {sys.getsizeof(no_slots)} байт')      # -> getsizeof NoSlots:    56 байт
print(f'asizeof   NoSlots:    {asizeof.asizeof(no_slots)} байт')    # -> asizeof   NoSlots:    352 байт





                            -- Обычные классы По размеру тоже самое что @dataclass(slots=True)  vs  @dataclass() --
                            -- Сравнение slots vs no_slots --
                            
class WithSlots:__slots__ = ()

with_slots = WithSlots()
print(f'getsizeof WithSlots:  {sys.getsizeof(with_slots)} байт')    # -> getsizeof WithSlots:  32 байт
print(f'asizeof   WithSlots:  {asizeof.asizeof(with_slots)} байт')  # -> asizeof   WithSlots:  32 байт


class NoSlots:pass

no_slots = NoSlots()
print(f'getsizeof NoSlots:    {sys.getsizeof(no_slots)} байт')      # -> getsizeof NoSlots:    56 байт
print(f'asizeof   NoSlots:    {asizeof.asizeof(no_slots)} байт')    # -> asizeof   NoSlots:    352 байт                            





                            -- Примеры int() float() complex() True False str() range(0) bytes() bytearray() --  <-----

my_int = int()
print(f'getsizeof int():  {sys.getsizeof(my_int)} байт')            # -> getsizeof int():      28 байт
print(f'asizeof   int():  {asizeof.asizeof(my_int)} байт')          # -> asizeof   int():      32 байт


my_float = float()
print(f'getsizeof float():  {sys.getsizeof(my_float)} байт')        # -> getsizeof float():    24 байт
print(f'asizeof   float():  {asizeof.asizeof(my_float)} байт')      # -> asizeof   float():    24 байт


my_comp = complex()
print(f'getsizeof complex():  {sys.getsizeof(my_comp)} байт')       # -> getsizeof complex():  32 байт
print(f'asizeof   complex():  {asizeof.asizeof(my_comp)} байт')     # -> asizeof   complex():  32 байт


# True
print(f'getsizeof True:  {sys.getsizeof(True)} байт')               # -> getsizeof True:       28 байт
print(f'asizeof   True:  {asizeof.asizeof(True)} байт')             # -> asizeof   True:       32 байт


# False
print(f'getsizeof False:  {sys.getsizeof(False)} байт')             # -> getsizeof False:      28 байт
print(f'asizeof   False:  {asizeof.asizeof(False)} байт')           # -> asizeof   False:      32 байт


my_str = str()
print(f'getsizeof str():  {sys.getsizeof(my_str)} байт')            # -> getsizeof str():      49 байт
print(f'asizeof   str():  {asizeof.asizeof(my_str)} байт')          # -> asizeof   str():      56 байт


my_range = range(0)
print(f'getsizeof range(0):  {sys.getsizeof(my_range)} байт')       # -> getsizeof range(0):   48 байт
print(f'asizeof   range(0):  {asizeof.asizeof(my_range)} байт')     # -> asizeof   range(0):   48 байт


my_bytes = bytes()
print(f'getsizeof bytes():  {sys.getsizeof(my_bytes)} байт')        # -> getsizeof bytes():    33 байт
print(f'asizeof   bytes():  {asizeof.asizeof(my_bytes)} байт')      # -> asizeof   bytes():    40 байт


my_b_arr = bytearray()
print(f'getsizeof bytearray():  {sys.getsizeof(my_b_arr)} байт')    # -> getsizeof bytearray():  56 байт
print(f'asizeof   bytearray():  {asizeof.asizeof(my_b_arr)} байт')  # -> asizeof   bytearray():  56 байт
"""







# type - это тип ВСЕХ типов, для которых НЕ указан явно иной метакласс  ПРОСТО ПОСМОТРЕТЬ!!!
"""
print(type(type))    # -> <class 'type'>
print(type(object))  # -> <class 'type'>
print(type(list))    # -> <class 'type'>
print(type(set))     # -> <class 'type'>
print(type(dict))    # -> <class 'type'>
print(type(bool))    # -> <class 'type'>
print(type(int))     # -> <class 'type'>
print(type(str))     # -> <class 'type'>
print(type(collections.deque))  # -> <class 'type'>

class Bar(object): pass
print(type(Bar))  # -> <class 'type'>
"""




# Напишите Релизацию своего класса имитируещего словарь  через []    Создание собственного класса для реализации словаря













# Ответ Релизация СЛОВАРЯ  Задача с собеседовании   Через  tuple()
# Релизация своего класса имитируещего словарь      Создание собственного класса для реализации словаря
"""
class MyDict:
    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        # Проверяем, есть ли ключ уже в словаре
        for i, (k, v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)  # Обновляем значение
                return
        self.data.append((key, value))  # Добавляем новый элемент

    def __getitem__(self, key):
        for k, v in self.data:
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]  # Удаляем элемент с данным ключом
                return
        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        return any(k == key for k, v in self.data)  # Проверяем наличие ключа

    def __len__(self):
        return len(self.data)  # Возвращаем количество элементов в словаре

    def __iter__(self):
        return (k for k, v in self.data)  # Итерирование по ключам

    def items(self):
        return self.data.copy()  # Возвращаем все пары (ключ, значение)

    def keys(self):
        return [k for k, v in self.data]  # Возвращаем список ключей

    def values(self):
        return [v for k, v in self.data]  # Возвращаем список значений


# Пример использования
my_dict = MyDict()
my_dict['apple'] = 1
my_dict['banana'] = 2

print(my_dict['apple'])     # Вывод: 1
print('banana' in my_dict)  # Вывод: True
print(len(my_dict))         # Вывод: 2

my_dict['apple'] = 3
print(my_dict['apple'])     # Вывод: 3

my_dict['cherry'] = 5
print(my_dict.items())      # Вывод: [('apple', 3), ('banana', 2), ('cherry', 5)]

del my_dict['banana']
print(my_dict.items())      # Вывод: [('apple', 3), ('cherry', 5)]



# Мой вариант на собеседовании ПРОСТОЙ   Через  tuple()

# Тоже самое  Но каждый раз будет создаватся новый список
@dataclass
class MyDict:
    data: list = field(default_factory=list)


class MyDict:
    def __init__(self):
        self.data = []

    def _add(self, key, value):
        if key:
            self.data.append((key, value))

    def _get(self, key):
        for i, (k, v) in enumerate(self.data):
            if key and k == key:
                return v
        raise KeyError


c = MyDict()
c._add(1, 'A')
print(c._get(1))  # -> A
print(c._get(2))  # -> KeyError
"""




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
# print(5 <= n < 10 or 101 < n < 201)  # -> False







s = "Hello"
# print(f'Если перевернуть слово "{s}", получится "{s[::-1]}".')





# Напечатайте индекс наименьшего числа в списке.
a = [5, 8, 3, 2, 7, 4, 9]








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


# Используйте метод 'json.dump()' с отступами  'data.json'  Перепишите пример ниже

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

# В findall так НЕ РАБОТАЕТ
re.findall(r'([a-zA-Zа-яА-ЯёЁ])\1', text)                                    # -> ['g']
re.findall(r'([a-zA-Zа-яА-ЯёЁ])\1\1', text)                                  # -> ['g']
"""


# Напишите Обычную группу и  группу БЕЗ Захвата

text = "abc123"











# Группа С захватом ()   Группа БЕЗ захвата   (?:)
"""
re.findall("([abc])+", "abc")    # -> ['c']     # Группа С захватом
re.findall("(?:[abc])+", "abc")  # -> ['abc']   # Группа БЕЗ захвата   (?:)
"""


# Напишите   Lookahead   Lookbehind

text = '123ABC'









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








# Ответ Обновление Словаря/Множества
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


it = iter([i for i in range(10)])
print(*it)    # -> 0 1 2 3 4 5 6 7 8 9
it = iter([i for i in range(10)])
print([*it])  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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


# eval vs exec   compile   Можно просто посмотреть







# Ответ eval vs exec   compile   Можно просто посмотреть
"""
Интересный пример
exec("print(aaaa)", globals(), {'aaaa': 42})  # -> 42
eval("print(aaaa)", globals(), {'aaaa': 42})  # -> 42


a = 5
# Возвращает Результат
print(eval('37 + a'))  # -> 42
# Возвращает None
print(exec('37 + a'))  # -> None

# exec Может создать переменную
print(exec('a = 47'))  # -> 47
# eval НЕ Может создать переменную
# print(eval('a = 47'))  # -> SyntaxError: invalid syntax


# eval() НЕ Будет работать!
x = eval('x = 5')  # INVALID; assignment is not an expression.
x = eval('if 1: x = 4')  # INVALID; if is a statement, not an expression.

# exec() Будет работать!
exec('x = 5')
print(x)  # -> 5
x = exec('if 1: x = 4')
print(x)  # -> None


# Выполняет блок кода exec()        # Ошибка eval()
program = '''                       program = '''                            
for i in range(2):                  for i in range(2):                            
    print("Python, sep=' '")            print("Python, sep=' '")                            
'''                                 '''                            
exec(program)                       eval(program)  # -> SyntaxError: invalid syntax                            
# Python, sep=' '                                   
# Python, sep=' '    

# Работает
exec(compile('for i in range(3): print(i, end=" ")', filename='<string>', mode='exec'))   # -> 0 1 2

# compile вызывает исключение, если исходный код содержит операторы или что-либо еще, кроме одного выражения:
# eval(compile('for i in range(3): print(i, end=" ")', filename='<string>', mode='eval'))
# for i in range(3): print(i)
#     ^^^
# SyntaxError: invalid syntax

# Работает
compiled_exec = compile('print("Hello")',  filename='<string>', mode='exec')
exec(compiled_exec)  # -> Hello
compiled_eval = compile('print("Hello")',  filename='<string>', mode='eval')
eval(compiled_eval)  # -> Hello                     
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


# Функцию Прибавили
res = lambda: 5
print((lambda x: x+res())(10))  # -> 15

# Можно использовать много +/++++ Разницы НЕТ
print((lambda y: y+2)(3))         # -> 5
print((lambda y: y++2)(3))        # -> 5
print((lambda y: y++++++++2)(3))  # -> 5

# Можно использовать много -/---- Разницы Есть!! четное количество - равно +     НЕ четное количество - равно -
print((lambda x: x-2)(3))     # -> 1
print((lambda x: x--2)(3))    # -> 5
print((lambda x: x---2)(3))   # -> 1
print((lambda x: x----2)(3))  # -> 5
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



# Использовать heapq   Написать    MaxHeap/MinHeap


minheap = [20, 10, 1, 2]






maxheap = [20, 10, 1, 2]








# Ответ Использовать heapq   Написать    MaxHeap/MinHeap     _heapify_max или умножение на -1 или добавить - к числу
"""
import heapq

# MinHeap
minheap = [20, 10, 1, 2]
heapq.heapify(minheap)
print(minheap[0])                     # -> 1
print(heapq.heappop(minheap))         # -> 1


# MaxHeap  через метод _heapify_max
maxheap = [20, 10, 1, 2]
heapq._heapify_max(maxheap)
print(maxheap[0])                     # -> 20
print(heapq.heappop(maxheap))         # -> 20


# MaxHeap   через добавление минуса
maxheap_2 = [20, 10, 1, 2]
res = [-i for i in maxheap_2]
print(res)                            # -> [-20, -10, -1, -2]
heapq.heapify(res)
print(res[0])                         # -> -20
print(heapq.heappop(res))             # -> -20


# MaxHeap   через умножение на -1
maxheap_3 = [20, 10, 1, 2]
res = [i*(-1) for i in maxheap_3]
heapq.heapify(res)
print(res[0])                         # -> -20
print(heapq.heappop(res))             # -> -20
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
# Через from dataclasses import dataclass
@dataclass
class Singleton:
    _instance: 'Singleton' = None


# Через Обычный Класс
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



# Напишите Monostate Обычный class/dataclass












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

# Тоже самое через dataclass    __post_init__
"""
@dataclass
class Monostate:
    _shared_state: dict = None

    def __post_init__(self):
        if Monostate._shared_state is None:
            Monostate._shared_state = {'a': 1, 'b': 2}
        self.__dict__ = Monostate._shared_state 

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

# Пример Monostate dataclass  # Смотри на словарь  Для каждого ЭК свой словарь    <-----
"""
from dataclasses import dataclass, field

@dataclass
class Monostate:
    _shared_state: dict = field(default_factory=lambda: {'a': 1, 'b': 2})

    def __post_init__(self):
        self.__dict__ = self._shared_state


mono = Monostate()
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {'a': 1, 'b': 2}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
print(mono_1.__dict__)  # -> {'a': 9999999999, 'b': 2}
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

from dataclasses import dataclass

@dataclass
class New:
    name: str = 'Chuck Norris'
    surname: str = 'Sasya'
    number: int = 10









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


# Примеры встроенных объектов дескрипторов: classmethod, staticmethod, property, функции в целом      <-----
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

first = {1: 1, 2: 2, 3: 3}
second = {4: 4, 5: 5}









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

text = 'hello'










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

first = {1: 1, 2: 2, 3: 3}
second = {2: 2, 1: 1}








# Ответы OrderedDict
"""
from collections import OrderedDict

first = {1: 1, 2: 2, 3: 3}
second = {2: 2, 1: 1}

order1 = OrderedDict(first)
order2 = OrderedDict(second)

print(order1.popitem(last=False))         # -> (1, 1)

print(order1)                             # -> OrderedDict([(2, 2), (3, 3)])
order1.move_to_end(3, last=False)
print(order1)                             # -> OrderedDict([(3, 3), (2, 2)])

# Сравниваем порядок внутри
a_dict = {1: 1, 2: 2}
dict_a = {2: 2, 1: 1}
print(a_dict==dict_a)                     # -> True

order3 = OrderedDict({1: 1, 2: 2})
order4 = OrderedDict({2: 2, 1: 1})
print(order3==order4)                     # -> False
"""



# -- class collections.defaultdict(default_factory=None, /[, ...]) --
# Использовать defaultdict


text = 'hello'









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
print(tom)       # -> ('Tom', 4, 'yellow')
Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)       # -> Cat(name='Tom', age=4, color='yellow')
print(tom.name)  # -> Tom


Point = namedtuple('Point', ['x', 'y'])  # Тоже самое
Point = namedtuple('Point', ('x', 'y'))  # Тоже самое
Point = namedtuple('Point', {'x', 'y'})  # Тоже самое
Point = namedtuple('Point', 'x y')       # Тоже самое  Тут будет работать split  print('x y'.split())  # -> ['x', 'y']
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


# deque НЕ поддерживает pop(1)/popleft(1) с аргументом(Индексом)                            <-----   

b_list = list([1, 2])
b_list.pop(0)
print(b_list)  # -> [2]

b_deque = deque([1, 2])
b_deque.pop(1)      # -> TypeError: deque.pop() takes no arguments (1 given)
b_deque.popleft(1)  # -> TypeError: deque.popleft() takes no arguments (1 given)
"""



# --- Модуль itertools в Python, эффективные итераторы для циклов   - сборник полезных итераторов ---

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

print(list(accumulate([1, 2, 3, 4, 5])))                # -> [1, 3, 6, 10, 15]
print(list(accumulate([1, 2, 3, 4, 5], initial=100)))   # -> [100, 101, 103, 106, 110, 115]
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

a = [1, 2, [3, 3], [4, 4]]
b, c, d = [1, 2], [1, 2], [1, 2]








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

a = ['foo', ['one', 'two', [1, 2]]]








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

a = [1, 4, 6, 4, 1]








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


a = [1, 4, 6, 4, 1]









# Ответы takewhile
"""
from itertools import takewhile, dropwhile

print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))    # -> [1, 4]

print((list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))))  # -> [6, 4, 1]
"""



# itertools.filterfalse(predicate, iterable)
# Использовать filterfalse


a = range(1, 5)







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

gen = (i for i in range(5))








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


# Используем срезы slice()
print(list([1, 2, 3][slice(None, 2)]))         # -> [1, 2]
print(list([1, 2, 3][slice(None, None, -1)]))  # -> [3, 2, 1]          # Только 3 параметра!!!   <-----
"""


# itertools.pairwise(iterable)
# Использовать pairwise

a = [1, 2, 3]












# Ответы pairwise
"""
from itertools import pairwise
result = pairwise([1, 2, 3])

print(list(result))  # -> [(1, 2), (2, 3)]
"""


# itertools.starmap(function, iterable)
# Использовать starmap

a = [(2, 5, 4), (3, 2, 1), (10, 3, 8)]







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


# Интересный вариант Присмотрись                                     Важно   <----- 
a = [(2, 5, 4), (3, 2, 1), (10, 3, 8)]  

print([*itertools.starmap(min, a)])                    # -> [2, 1, 3]   
print([*itertools.starmap(lambda x, y, z: x*y+z, a)])  # -> [14, 7, 38]
"""


# itertools.tee(iterable, n=2)
# Использовать tee

a = [1, 2, 3]







# Ответы tee
"""
from itertools import tee

rez = tee([1, 2, 3], 3)
print([list(i) for i in rez])  # -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""




# itertools.zip_longest(*iterables, fillvalue=None)     zip(*iterables, strict=False)
# Использовать zip_longest

a = [1, 2]
b = [1, 2, 3]







# Ответы zip_longest
"""
from itertools import zip_longest

rez = zip_longest([1, 2], [1, 2, 3], fillvalue=100)
print(list(rez))  # -> [(1, 1), (2, 2), (100, 3)]


# встроенная функция zip()
rez = zip([1, 2], [1, 2, 3])
print(list(rez))  # -> [(1, 1), (2, 2)]



# zip vs zip_longest
a = [1, 2]
b = [1, 2, 3]

# zip vs zip_longest
print([*itertools.zip_longest(a, b)])  # -> [(1, 1), (2, 2), (None, 3)]
print([*zip(a, b, strict=False)])      # -> [(1, 1), (2, 2)]
print([*zip(a, b, strict=True)])       # -> ValueError: zip() argument 2 is longer than argument 1
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

a = [1, 2]






a, b = [1, 2], [3, 3]





# Ответы product
"""
from itertools import product

print(list(product([1, 2], repeat=2)))  # -> [(1, 1), (1, 2), (2, 1), (2, 2)]
print(list(product([1, 2], repeat=3)))  # -> [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

pairs = ['Aa', 'Bb']
gams = list([x for x in product(*pairs)])
print(gams)  # -> [('A', 'B'), ('A', 'b'), ('a', 'B'), ('a', 'b')]


# Интересный пример
a = [1, 2]
print(list(itertools.product(a, repeat=1)))     # -> [(1,), (2,)]
print(list(itertools.product(a, repeat=2)))     # -> [(1, 1), (1, 2), (2, 1), (2, 2)]

a, b = [1, 2], [3, 3]
print(list(itertools.product(a, b, repeat=1)))  # -> [(1, 3), (1, 3), (2, 3), (2, 3)]
print(list(itertools.product(a, b, repeat=2)))
# [(1, 3, 1, 3), (1, 3, 1, 3), (1, 3, 2, 3), (1, 3, 2, 3), (1, 3, 1, 3), (1, 3, 1, 3), (1, 3, 2, 3), (1, 3, 2, 3), ...
"""


# itertools.permutations(iterable, r=None)
# Использовать permutations

a = 'XYZ'







# Ответы permutations
"""
from itertools import permutations

print(list(permutations('XY', 2)))  # -> [('X', 'Y'), ('Y', 'X')]
print(list(permutations('XYZ', 3)))
# [('X', 'Y', 'Z'), ('X', 'Z', 'Y'), ('Y', 'X', 'Z'), ('Y', 'Z', 'X'), ('Z', 'X', 'Y'), ('Z', 'Y', 'X')]
# По дефолту
print(list(itertools.permutations('XYZ')))
# [('X', 'Y', 'Z'), ('X', 'Z', 'Y'), ('Y', 'X', 'Z'), ('Y', 'Z', 'X'), ('Z', 'X', 'Y'), ('Z', 'Y', 'X')]
"""



# itertools.combinations(iterable, r)
# Использовать combinations

a = 'XYZ'







# Ответы combinations
"""
from itertools import combinations

print(list(combinations('XYZ', 2)))  # -> [('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
print(list(combinations('XYZ', 3)))  # -> [('X', 'Y', 'Z')]
"""



# itertools.combinations_with_replacement(iterable, r)
# Использовать combinations_with_replacement

a = 'XYZ'








# Ответы combinations_with_replacement
"""
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('XYZ', 2)))  # -> [('X', 'X'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Y'), ('Y', 'Z'), ('Z', 'Z')]
print(list(combinations_with_replacement('XYZ', 3)))
# [('X', 'X', 'X'), ('X', 'X', 'Y'), ('X', 'X', 'Z'), ('X', 'Y', 'Y'), ('X', 'Y', 'Z'), ('X', 'Z', 'Z'), ('Y', 'Y', 'Y'),
# ('Y', 'Y', 'Z'), ('Y', 'Z', 'Z'), ('Z', 'Z', 'Z')]
"""



# --- Отличия    combinations  vs  combinations_with_replacement vs  permutations ---

a = 'XYZ'







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

a = [1, 2, 3, 4]








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

# ИЛИ Сразу вызываем но нужно все аргументы прокидывать
print(partial(multiply, 3, 3)())  # 9
print(partial(multiply, 5, 5)())  # 25
print(partial(multiply, 5)())     # TypeError: multiply() missing 1 required positional argument: 'y'
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



# Тоже самое через dataclass        from typing import Callable   - Чтобы указать аннотацию функция

from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Timer:
    func: Callable[[int], str]  # Аннотация типа для функции, принимающей int и возвращающей str

    def __call__(self, *args, **kwargs):
        s = time.perf_counter()
        res = self.func(*args, **kwargs)
        f = time.perf_counter()
        print(f-s)
        return res

@Timer
def plus(a, b):
    return a + b

print(plus(2, 2))
"""

# 1.2) Написать dataclass
# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
# kw_only=False, slots=False, weakref_slot=False)











# Ответ 1.2)
# Декорирование класса в Python:

# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
# kw_only=False, slots=False, weakref_slot=False)
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


# 1.3) Сделать по умолчанию пустой список и НЕ пустой  Сравнение __eq__()  уже встроенно в dataclass












# Ответ 1.3)
# Сделать по умолчанию пустой список и НЕ пустой  Сравнение __eq__()  уже встроенно в dataclass
"""
from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Foo:
    n: int
    s: str = 'a'
    ss: str = field(default='AAA')
    items: list[str] = field(default_factory=list)              # <-- и всё это - чтобы по умолчанию был пустой список
    items_2: list[str] = field(default_factory=lambda: [1, 2])  # <-- и всё это - чтобы по умолчанию было [1, 2]
    a_dict: dict = field(default_factory=lambda: {1: 2})
    # a_list: list = field(default=[1, 2])                      # Так будет ошибка
    # a_dict: dict = field(default={3:3})                       # Так будет ошибка
    # ValueError: mutable default <class 'list'> for field a_list is not allowed: use default_factory


f = Foo(1)
f1 = Foo(1)

print(f.__dict__)      # -> {'n': 1, 's': 'a', 'ss': 'AAA', 'items': [], 'items_2': [1, 2], 'a_dict': {1: 2}}
print(f.__eq__(f1))    # -> True
print(f == f1)         # -> True

ff = Foo(11111)
ff1 = Foo(1)
print(ff.__eq__(ff1))  # -> False
print(ff == ff1)       # -> False
print(f >= f1)         # -> True       order=True  Будут работать
f.a = 10               # -> dataclasses.FrozenInstanceError: cannot assign to field 'a'   frozen=True
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















# Ответ Создать Абстрактный класс  и Унаследоваться от него     from abc import ABC, abstractmethod
"""
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



# Интересный момент с \     SyntaxError: unexpected character after line continuation character    <-----
from abc import ABC, abstractmethod

class C(ABC):
    @abstractmethod
    def fff(self):
        pass

class CC(C):

    # def fff(self):
    #     return \     # SyntaxError: unexpected character after line continuation character

    def fff(self):
        return \

c = CC()
print(c.fff())  # -> None
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
    
    
# Названия generator object    coroutine object
def gen():
    x = 10
    print(x)
    yield x

# Не правильное использование
async def example():
    print(100)


print(gen())      # -> <generator object gen at 0x00000208FA74B2A0>

print(example())  # -> <coroutine object example at 0x00000208FA67E080>
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback


# Хороший пример с замером времени БЕЗ БЛОКИРУЮЩЕГО КОДА 3 СЕК   # C БЛОКИРУЮЩИМ КОДОМ  7 СЕК
async def one():                                                 async def one():                                                                               
    print('Start one')                                               print('Start one')                                                                                   
    await asyncio.sleep(1)                                           await asyncio.sleep(1)                                                                                       
    print('Stop one')                                                print('Stop one')                                                                                   
                                                                                                                                 
async def two():                                                 async def two():                                                                               
    print('Start two')                                               print('Start two')                                                                                   
    await asyncio.sleep(2)                                           await asyncio.sleep(2)                                                                                       
    # time.sleep(5)                                                  time.sleep(5)            # Тут   БЛОКИРУЮЩИЙ КОД                                                                 
    print('Stop two')                                                print('Stop two')                                                                                   
                                                                                                                                 
async def three():                                               async def three():                                                                               
    print('Start three')                                             print('Start three')                                                                                       
    await asyncio.sleep(3)                                           await asyncio.sleep(3)                                                                                       
    print('Stop three')                                              print('Stop three')                                                                                   
                                                                                         
async def main():                                                async def main():                                       
    await asyncio.gather(one(), two(), three())                      await asyncio.gather(one(), two(), three())                                                                   
                                                                                         
                                                                                         
if __name__ == '__main__':                                       if __name__ == '__main__':                                               
    start = time.time()                                              start = time.time()                                           
    asyncio.run(main())                                              asyncio.run(main())                                           
    print(time.time() - start)  # -> 2.994696855545044               print(time.time() - start)  # -> 7.008123874664307                                                                           
"""


# Как запустить что-то в потоке и вывести результат?   from concurrent.futures import ThreadPoolExecutor















# Ответ  Как запустить что-то в потоке и вывести результат?  from concurrent.futures import ThreadPoolExecutor
"""
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











# Ответ Как запустить что-то в Процессах и вывести результат?   # lambda не сериализуется pickle   ProcessPoolExecutor
"""
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



# БЕЗ ФУНКЦИИ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.


d = [-1, -3, 2, 4, 5, 7, 8, 9]
target = 9













# Ответ БЕЗ ФУНКЦИИ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.
# Важно отметить, что массив должен быть ОТСОРТИРОВАН для применения бинарного поиска.
"""
d = [-1, -3, 2, 4, 5, 7, 8, 9]
n = len(d)

search_v = 9
left, right = 0, n-1

while left <= right:
    middle = (left + right) // 2
    v = d[middle]
    if v == search_v:
        print(v, middle)   # 9 7
        break
    elif v < search_v:
        left = middle+1
    elif v > search_v:
        right = middle-1
else:
    print('Значение не найдено')
"""



# ФУНКЦИЮ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.

d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 9


def binary_search(arr, target):
    pass



# print(binary_search(d, target))  # -> 8




# Ответ ФУНКЦИЮ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.
# Важно отметить, что массив должен быть ОТСОРТИРОВАН для применения бинарного поиска.
"""
d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 9

def binary_search(arr, target):
    arr = sorted(arr)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Находим середину

        if arr[mid] == target:
            return mid  # Нашли элемент, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return -1  # Элемент не найден


print(binary_search(d, target))  # -> 8
"""





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







# --- Django  Чуть-чуть ---

# Напишите raw-запрос










# Ответ Напишите raw-запрос
"""
people = Person.objects.raw("SELECT id, name FROM hello_person")
"""



# Перепишите lookups











# Ответ Перепишите lookups
"""
 Model.objects.filter(budget=1000)                    ==   фильтр на равенство поля
 Model.objects.filter(budget__gt=1000)                 >   фильтр на поле больше значения (great then)
 Model.objects.filter(budget__lt=1000)                 <   фильтр на поле меньше значения
 Model.objects.filter(budget__gte=1000)               >=   фильтр на поле больше либо равно значения
 Model.objects.filter(budget__lte=1000)               <=   фильтр на поле меньше либо равно значения
 Model.objects.exclude(budget=1000)                   !=   фильтр на поле не равно значению
 Model.objects.filter(year__isnull=True)                   фильтр на поле пустое (False - не пустое)
 Model.objects.filter(year__isnull=True, name=’Avatar’)    фильтр на два поля
 Model.objects.exclude(budget=1000).filter(name=’Avatar’)  фильтр на два поля
 Model.objects.filter(name__contains=’Avatar’)             поле содержит значение, чувствителен к регистру
 Model.objects.filter(name__icontains=’Avatar’)            поле содержит значение, НЕ чувствителен к регистру
 Model.objects.filter(name__startswith=’a’)                поле начинается с “a”
 Model.objects.filter(name__endswith=’a’)                  поле заканчивается на “a”
 Model.objects.filter(id__in=[3,5,6]’)                     выбираются все значения из списка
 
 # Очень полезные методы   __regex  - чувствительное к регистру       __iregex - НЕчувствительное к регистру
 Model.objects.filter(adv_images__regex=r'^\d\.')[:3]
 Model.objects.filter(adv_images__iregex=r'^\d\.')[:3]
 Model.objects.get(title__regex=r"^(An?|The) +")
"""







# Задачи на ORM
"""
class City(models.Model):
   name = models.CharField()


class Person(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City)
    """

# 1)Вывести список людей и городов где они живут?
# 2)Вывести всех людей, живущих в городе N
# 3)Вывести 5 городов с наибольшим населением, упорядочив по убыванию.





# Ответ:
# Вот пример определения моделей с учетом этих деталей:
"""
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
     name = models.CharField(max_length=255)
     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='people')

     def __str__(self):
         return self.name
"""



# -- Теперь перейдем к выполнению задач --:


# 1. Вывести список людей и городов, где они живут:











# Ответ 1. Вывести список людей и городов, где они живут:
"""
people_with_cities = Person.objects.select_related('city').values('name', 'city__name')
for person in people_with_cities:
    print(f'Человек: {person["name"]}, Город: {person["city__name"]}')
"""



# 2. Вывести всех людей, живущих в городе N:

city_name = 'N'  # укажите название города













# Ответ 2. Вывести всех людей, живущих в городе N:
"""
city_name = 'N'  # укажите название города
people_in_city_n = Person.objects.filter(city__name=city_name)

for person in people_in_city_n:
    print(f'Человек: {person.name}')
"""




# 3. Вывести 5 городов с наибольшим населением, упорядочив по убыванию.
# Для этого нам нужно будет добавить поле для хранения количества людей в каждом городе. Однако, чтобы подсчитать
# это количество динамически, мы можем использовать аннотирование с `Count`.













# Ответ 3. Вывести 5 городов с наибольшим населением, упорядочив по убыванию.
"""
from django.db.models import Count

top_cities = City.objects.annotate(population=Count('people')).order_by('-population')[:5]

for city in top_cities:
    print(f'Город: {city.name}, Население: {city.population}')
"""





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





# --- Задачи с Собеседования Python ---



# Задача "Правильная скобочная последовательность"    Valid Braces  Codewars    Мир Танков/World of Tanks


# Написать 3 варианта
def is_correct_brackets(text):
    pass






# print(is_correct_brackets('(((())))'))  # True
# print(is_correct_brackets('(((())'))  # False
# print(is_correct_brackets('())))'))  # False
# print(is_correct_brackets('((((){}[]{}[])))'))  # True
# print(is_correct_brackets('(){}[]{}[])))'))  # False
# print(is_correct_brackets('(){}[]{}[]'))  # True







# Ответ Задача "Правильная скобочная последовательность"    Valid Braces  Codewars    Мир Танков/World of Tanks
"""
# Первый Вариант
def is_correct_brackets(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')

    # Возвращаем True, если text с пустой строкой
    return not text


print(is_correct_brackets('(((())))'))  # True
print(is_correct_brackets('(((())'))  # False
print(is_correct_brackets('())))'))  # False
print(is_correct_brackets('((((){}[]{}[])))'))  # True
print(is_correct_brackets('(){}[]{}[])))'))  # False
print(is_correct_brackets('(){}[]{}[]'))  # True


# Второй Вариант
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


print(validBraces('(((())))'))  # True
print(validBraces('(((())'))  # False
print(validBraces('())))'))  # False
print(validBraces('((((){}[]{}[])))'))  # True
print(validBraces('(){}[]{}[])))'))  # False
print(validBraces('(){}[]{}[]'))  # True


# Третий Вариант
def validBraces(string):
    for _ in string:
        string = string.replace('{}', '').replace('()', '').replace('[]', '')
    return not string


print(validBraces('(((())))'))  # True
print(validBraces('(((())'))  # False
print(validBraces('())))'))  # False
print(validBraces('((((){}[]{}[])))'))  # True
print(validBraces('(){}[]{}[])))'))  # False
print(validBraces('(){}[]{}[]'))  # True


# Ответ ChatGPT
def is_valid(s: str) -> bool:
    # Создаем стек для хранения открывающих скобок
    stack = []
    # Словарь для сопоставления открывающих и закрывающих скобок
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        # Если символ — закрывающая скобка
        if char in mapping:
            # Извлекаем верхнюю скобку из стека, если стек не пуст
            # В противном случае используем символ-знак
            top_element = stack.pop() if stack else '#'
            # Проверяем, соответствует ли открывающая скобка закрывающей
            if mapping[char] != top_element:
                return False
        else:
            # Если это открывающая скобка, добавляем её в стек
            stack.append(char)

    # Если стек пуст, значит все скобки корректны
    return not stack


# Примеры использования
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
________________________________________________________________________________________________________________________
"""



# Создать функцию которая убирает дубликаты           Задача с Live Coding Собеседования


# Написать 2 варианта
def clean_duplicates(lst):
    pass





# print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]







# Ответ Создать функцию которая убирает дубликаты           Задача с Live Coding Собеседования
"""
# Первый вариант
def clean_duplicates(lst: list[dict]) -> list[dict]:
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]


# Второй вариант
def clean_duplicates(lst: list[dict]) -> list[dict]:
    res = []
    [res.append(i) for i in lst if i not in res]
    return res

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]


# Третий вариант
def clean_duplicates(lst: list[dict]) -> list[dict]:
    return list([eval(i) for i in set(tuple([str(i) for i in lst]))])

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]


# Интересный вариант                    # Тоже самое         
def clean_duplicates(lst):              def clean_duplicates(lst):            
    res = set()                             res = {str(i) for i in lst}
    for i in lst:                           return [eval(i) for i in res]    
        res.add(str(i))                         
    return [eval(i) for i in res]

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]
________________________________________________________________________________________________________________________
"""



# Yandex-Маркет Задача Отсортировать по двум параметрам. Как я сделал я не знаю

xs = [
    '1_a.txt',
    '2_b.txt',
    '1_c.txt',
    '3_d.txt',
    '1_e.txt',
]







# Ответ  Yandex-Маркет Задача Отсортировать по двум параметрам. Как я сделал я не знаю
"""
xs = [
    '1_a.txt',
    '2_b.txt',
    '1_c.txt',
    '3_d.txt',
    '1_e.txt',
]

def sub_fun(x):
    return -int(re.sub(r'[^\d]+', '', x)), re.search(r'(?<=_)[a-z]+(?=\.)', x, flags=re.I).group()

def my_func(lst: list) -> list:
    return sorted(lst, key=sub_fun)

print(my_func(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']

print(sorted(xs, key=lambda x: (-int(x[0]), x[1])))
print(sorted(xs, key=lambda x: (-int(re.sub(r'[^\d]+', '', x)), re.search(r'(?<=_)[a-z]+(?=\.)', x, flags=re.I).group())))
print(sorted(xs, key=sub_fun))
# ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
# ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
# ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']

# Через split() хз как улучшить
print(sorted(xs, key=lambda x: (-int(''.join(x.split('.')).split('_')[0]), ''.join(x.split('.')).split('_')[1])))


# Интересный вариат                                     # Тоже самое    
def my_func(x):                                         def my_func(x):
    return -int(x.split('_')[0]), x.split('_')[1]           a, b = x.split('_')                                    
                                                            return -int(a), b        

def get_sorted(lst):
    return sorted(lst, key=my_func)


print(get_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
print(get_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
________________________________________________________________________________________________________________________
"""







# Two Sum Задача с собеседования  YADRO

lst = [2, 7, 9, 10, 11]
target = 9


# Написать 2 варианта
def twoSum(nums, target):
    pass





# print(twoSum(lst, target))  # -> [[0, 1]]






# Ответ Two Sum Задача с собеседования  YADRO
"""
lst = [2, 7, 9, 10, 11]
target = 9

# Хороший вариант                                     # Тоже самое с МОРЖОМ      
def twoSum(nums, target):                             def twoSum(nums, target):                                  
    res = []                                              res = []                      
    for i in range(len(nums)-1):                          for i in range(len(nums)-1):                                          
        if nums[i] + nums[i+1] == target:                     if sum(((a:=nums[i]), (b:=nums[i+1]))) == target:                                                  
            res.append(nums.index(nums[i]))                       res.append(nums.index(a))                                                  
            res.append(nums.index(nums[i+1]))                     res.append(nums.index(b))                                                      
    return res                                            return res                      
                                                                
print(twoSum(lst, target))  # -> [0, 1]


# Пример 1
from itertools import pairwise
                                                                # Тоже самое но ВЫВОД  [0, 1]  
def twoSum(nums, target):                                       def twoSum(nums, target):                                                                                    
    res = []                                                        res = []                                                                        
    for i, v in enumerate(pairwise(nums)):                          for i, j in itertools.pairwise(nums):                                    
        if sum([v[0], v[1]]) == target:                                 if i+j == target:                                
            res.append([nums.index(v[0]), nums.index(v[1])])                res.append((nums.index(i), nums.index(j)))                                                        
    return res                                                      return [j for i in res for j in i]        
                                                                     
print(twoSum(lst, target))  # -> [[0, 1]]                       print(twoSum(lst, target))  # -> [0, 1]                                    


# Тоже самое slice(1, None, 2) - Принимает только 3 аргумента      Тут создает такие пары  [(2, 7), (9, 10)]
def twoSum(nums, target):                                          lst = [2, 7, 9, 10, 11]     
    res = []
    for i, v in enumerate(zip(nums[slice(None, None, 2)], nums[slice(1, None, 2)])):
        if sum([v[0], v[1]]) == target:
            res.append([i, i + 1])
    return res

print(twoSum(lst, target))  # -> [[0, 1]]


# Тут создает такие пары  [(2, 7), (9, 10)]     lst = [2, 7, 9, 10, 11]     
# Пример 2                                                # Тоже самое                  
def twoSum(nums, target):                                 def twoSum(nums, target):                 
    res = []                                                  res = []
    for i, v in enumerate(zip(nums[::2], nums[1::2])):        for i, (k, v) in enumerate(zip(nums[::2], nums[1::2])):
        if sum([v[0], v[1]]) == target:                           if sum([k, v]) == target:
            res.append([i, i+1])                                      res.append([i, i + 1])
    return res                                                return res

print(twoSum(lst, target))  # -> [[0, 1]]                   print(twoSum(lst, target))  # -> [[0, 1]]


# Пример 3
from itertools import combinations
def twoSum(nums, target):
    res = list(*[i for i in combinations(nums, 2) if sum(i) == target])
    return [i for i, v in enumerate(nums) if v in res]

print(twoSum(lst, target))  # -> [0, 1]


# Ответ ChatGPT
def twoSum(lst, target):
    res = []
    n = len(lst)
    # Ищем все пары индексов
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                res.append((i, j))
    return res

# Пример использования
print(twoSum(lst, target))  # -> [(0, 1)]
________________________________________________________________________________________________________________________
"""



# Релизация своего класса имитируещего СЛОВАРЬ   ML















#  Ответ Релизация своего класса имитируещего СЛОВАРЬ   ML
"""
# Мой вариант на собеседовании ПРОСТОЙ

class MyDict:
    def __init__(self):
        self.data = []

    def _add(self, key, value):
        if key:
            self.data.append((key, value))

    def _get(self, key):
        for i, (k, v) in enumerate(self.data):
            if key and k == key:
                return v
        raise KeyError


c = MyDict()
c._add(1, 'A')
print(c._get(1))  # -> A
print(c._get(2))  # -> KeyError



# Более Правильный вариант Сложный
class MyDict:
    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        # Проверяем, есть ли ключ уже в словаре
        for i, (k, v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)  # Обновляем значение
                return
        self.data.append((key, value))  # Добавляем новый элемент

    def __getitem__(self, key):
        for k, v in self.data:
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]  # Удаляем элемент с данным ключом
                return
        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        return any(k == key for k, v in self.data)  # Проверяем наличие ключа

    def __len__(self):
        return len(self.data)  # Возвращаем количество элементов в словаре

    def __iter__(self):
        return (k for k, v in self.data)  # Итерирование по ключам

    def items(self):
        return self.data.copy()  # Возвращаем все пары (ключ, значение)

    def keys(self):
        return [k for k, v in self.data]  # Возвращаем список ключей

    def values(self):
        return [v for k, v in self.data]  # Возвращаем список значений


# Пример использования
my_dict = MyDict()
my_dict['apple'] = 1
my_dict['banana'] = 2

print(my_dict['apple'])     # Вывод: 1
print('banana' in my_dict)  # Вывод: True
print(len(my_dict))         # Вывод: 2

my_dict['apple'] = 3
print(my_dict['apple'])     # Вывод: 3

my_dict['cherry'] = 5
print(my_dict.items())      # Вывод: [('apple', 3), ('banana', 2), ('cherry', 5)]

del my_dict['banana']
print(my_dict.items())      # Вывод: [('apple', 3), ('cherry', 5)]
________________________________________________________________________________________________________________________
"""




# Задачи с собеседования  X5


# Задача 1

# Есть список чисел. Нужно отсортировать нечетные числа по возрастанию, оставив четные на месте


def sort_array(arr):
    pass




numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(sort_array(numbers))  # -> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]




# Задача 2

'''Напишите функцию flatten, которая принимает любое кол-во аргументов
и 'разглаживает' их в один список. Все вложенные списки, неважно каких уровней вложенности,
должны разгладиться в один результирующий список'''


# Написать 2 варианта
def flatten(*args):
    pass



# print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> [1, 2, 2, 3, 4, 4]
# print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> [1, 2, 2, 3, 4, 4, 5, 5]




# Ответ Задачи с собеседования  X5

"""
# Задача 1

# Есть список чисел. Нужно отсортировать нечетные числа по возрастанию, оставив четные на месте

def sort_array(arr):
    odds = sorted([i for i in arr if i % 2])
    odd_index = 0
    res = []
    for i in arr:
        if i % 2:
            res.append(odds[odd_index])
            odd_index += 1
        else:
            res.append(i)
    return res

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(numbers))  # -> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# Ответ ChatGPT
def sort_array(source_array):
    odds = sorted(filter(lambda i: i % 2 != 0, source_array))
    odds_iter = iter(odds)
    return [next(odds_iter) if i % 2 != 0 else i for i in source_array]

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(numbers))  # -> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# Задача 2

'''Напишите функцию flatten, которая принимает любое кол-во аргументов
и 'разглаживает' их в один список. Все вложенные списки, неважно каких уровней вложенности,
должны разгладиться в один результирующий список'''


# Тоже самое  extend                                           # Тоже самое  +=
def flatten(*args):                                            def flatten(*args):
    res = []                                                       res = []
    for i in args:                                                 for i in args:
        if not isinstance(i, list):                                    if isinstance(i, list):
            res.append(i)                                                  res += flatten(*i)
        else:                                                          else:
            res.extend(flatten(*i))                                        res.append(i)
    return res                                                     return res

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Второй вариант
def flatten(*args):
    res = re.sub(r'[\]\[]', '', str(args))
    return eval(re.sub(r',?\)|\(', lambda x: '[' if x[0] == '(' else ']', res))

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Интересный вариант
from ast import literal_eval

def flatten(*args):
    res = re.sub(r'[\]\[]', '', str(args))
    res_2 = re.sub(r'\(|,\)', '', res)
    return literal_eval(f"[{res_2}]")
    # return eval(f"[{res_2}]")

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Интересный вариант
def flatten(*args):
    res = []
    for i in args:
        match i:
            case list():
                res += flatten(*itertools.chain(i))
            case _:
                res.append(i)
    return res

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Интересный вариант
def flatten(*args):
    try:
        return [*map(int, [i for i in re.findall(r'[^\[\]()]', str(args)) if i not in ' ,'])]
    except:
        print('not good')

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]
________________________________________________________________________________________________________________________
"""



# Задача максимальная последовательность чисел  СБЕР


# Написать 2 варианта
def longest_sequence(arr):
    pass




arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
# print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]




# Ответ Задача максимальная последовательность чисел  СБЕР
"""
# Мой вариант                                                   # Тоже самое          
def longest_sequence(arr):                                      def longest_sequence(arr):                                                                                                                                         
    if not arr:                                                     if not arr:                               
        return []                                                       return []                                                   
    res = []                                                        res = []                                      
    for i in range(len(arr)-1):                                     for i in range(len(arr)-1):                                              
        if arr[i] < arr[i+1]:                                           if arr[i] < arr[i+1]:                                      
            res.append(arr[i])                                              res.append(arr[i])                                                        
        else:                                                           else:                                                      
            res.append(arr[i])                                              res.append(arr[i])                                                                                
            res.append('A')                                                 res.append('A')                                                          
    if arr[-1] > res[-1]:                                           res_2 = ' '.join([str(i) for i in res]).split('A')                            
        res.append(arr[-1])                                         return max([i.split() for i in res_2], key=len)   
    res_2 = [i.strip().split() for i in ' '.join(map(str, res)).split('A')]                                                                      
    return [*map(int, max(res_2, key=len))]                                                

arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]


# Еще один вариант МОЙ
def longest_sequence(arr):
    res = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            res.append(arr[i])
        else:
            res.append(arr[i])
            res.append('A')
    res_2 = ' '.join(map(str, res)).split('A')
    return [*map(int, max([i.strip().split() for i in res_2], key=len))]


arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]


# Вариант ChatGPT
def longest_sequence(arr):
    if not arr:
        return []

    max_seq = []
    current_seq = []

    for i in range(len(arr)):
        # Если текущий элемент больше предыдущего
        if i == 0 or arr[i] > arr[i - 1]:
            current_seq.append(arr[i])
        else:
            # Если последовательность прерывается, проверяем и обновляем max_seq
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
            current_seq = [arr[i]]  # Начинаем новую последовательность

    # Проверяем последний текущий сегмент
    if len(current_seq) > len(max_seq):
        max_seq = current_seq
    return max_seq

arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]
"""













































































































































































































































































































































































































































































































































































































