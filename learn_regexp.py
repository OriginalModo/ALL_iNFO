import calendar
import collections
import copy
import csv
import datetime
import dis
import functools
import itertools
import math
import operator
import random
import re

# text = 'Мама мыла раму'
# # match - ищет последовательность в начале строки
# result = re.match(r'Мама', 'Мама мыла раму')
# print(result[0])                                     # -> Мама    Находит только если pattern в начале
# print(result.group(0), result.group(), result[0])    # -> Мама Мама Мама
# print(result.span(), result.start(), result.end())   # -> (0, 4) 0 4
# result = re.match(r'мыла', 'Мама мыла раму')
# print(result)                                        # -> None    pattern находится НЕ в начале
# print('-'*145)
# # search - ищет первое совпадение с pattern
# result = re.search(r'Мама', 'Мама мыла раму')
# print(result[0])                                     # -> Мама    возвращает только первое даже если больше
# result = re.search(r'мыла', 'Мама мыла раму')
# print(result.group(0))                               # -> мыла    возвращает только первое даже если больше
# result = re.search(r'мыла', 'Мама мыла мыла раму')
# print(result[0])                                     # -> мыла    возвращает только первое даже если больше
# # finditer - ищет все совпадения с pattern. Возвращает итератор
# result = re.finditer(r'мыла', 'Мама мыла мыла раму')
# print([i for i in result])                           # -> ['мыла', 'мыла']
# # re-функции без возврата Match-объекта
# # findall - ищет все совпадения с pattern. Возвращает результирующие строки в виде списка  Работает как search/match
# result = re.findall(r'мыла', 'Мама мыла мыла раму')
# print(result)                                        # -> ['мыла', 'мыла']
# # split - для разделения строки на части по разделителю
# result = re.split(r' ', 'Мама мыла мыла раму', maxsplit=1)
# print(result)                                        # -> ['Мама', 'мыла', 'мыла', 'раму']
# # sub - для замены в строках
# result = re.sub('мыла', '!', 'Мама мыла мыла раму')  # -> Мама ! ! раму
# print(result)





import re
import string
import sys
import time
import timeit

import numpy
import pandas as pd



def validate_time(time):
    return re.match(r'2[0-3]|[01]?[0-9]:[0-5][0-9]', time)[0]




# print(validate_time('1:00'))
# print(validate_time('13:1'))
# print(validate_time('12:60'))
# print(validate_time('12:59'))
# print(validate_time('12: 60'))
# print(validate_time('24:00'))
# print(validate_time('00:00'))
# print(validate_time('24o:00'))
# print(validate_time('24:000'))
# print(validate_time(''))
# print(validate_time('09:00'))
# print(validate_time('2400'))
# print(validate_time('foo12:00bar'))
# print(validate_time('010:00'))
# print(validate_time('1;00'))




import re


# Нужно найти весь текст от start до end, текст может быть растянут на несколько строк.
text = '''start
Каждое
Слово
На
Новой
Строке
end'''




import re

import re
# text = input()

# Важно Можно использовать rf'' fr'' - строки в заменах
text = r'Мак-адрес моего друга:F0:98:9D:1C:93:F6. Мой мак-адрес: 0F:70:DE:55:60:19.'

pattern = re.compile(r'(?:[A-F0-9]{2}:){5}[A-F0-9]{2}')

# print(pattern.findall(text))  # -> <em>Курсив</em> и <strong>Жирный текст</strong>


'(?=...)'  'Должно совпасть справа'    'Positive Lookahead'
'(?!...)'  'НЕ Должно совпасть справа' 'Negative Lookahead'
'(?<=...)' 'Должно совпасть слева'     'Positive Lookbehind'
'(?<!...)' 'НЕ Должно совпасть справа' 'Negative Lookbehind'

import re
from string import ascii_lowercase
from collections import Counter

def subb(m):
    return m[0]+'o'+m[0]

def translate_to_robber_lang(lst):
    return re.sub(r'(?i)[^aeiou !]', subb, lst)

from functools import reduce
import operator

from collections import defaultdict
from functools import reduce


import re


sett = {'salad', 'soup', 'main_dish', 'drink', 'desert'}



from typing import List, Optional
from collections import deque
import re



# Функция-применитель  Посмотри ВСЕ Варианты

from itertools import accumulate
import re
# В dict comprehension прописывать условие k: v Посмотри

from functools import wraps
from typing import Collection

# Пробрасывает Аргументы декоратора дополнительно к аргументам которые передаются при вызове оригинальной функции
from functools import wraps

import decimal
from math import ceil, floor, pow


# contrib = int(input())
# rate = int(input())
# months = int(input())
# print((contrib * float('0.'+str(rate))) + contrib)

# contrib = float(input())
# rate = float(input())
# months = float(input())
import math


import re



# n = int(input())
# lst = input().split()
# lst = [int(i) for i in input().split()]
# res = []
# res_login = []

from string import ascii_lowercase, ascii_uppercase
from itertools import groupby, accumulate, cycle
from functools import reduce
import operator
import heapq
from datetime import date, timedelta, datetime
from calendar import leapdays, isleap, monthrange
from itertools import chain, islice, groupby
from collections import defaultdict, deque, Counter
import re

a_dict = defaultdict(list)
a_dict_2 = defaultdict(list)


# lst = [int(i) for i in input().split()]
# int(input())
# input()
# lst = [float(input()), float(input()), float(input()),]

# Использование __import__   Найти цифры длиной 5 символов
a = 2020
from functools import reduce

# a = '1 2 3'.split()
# c = '1 1'.split()
# n = int(input())
# a = int(input())


# Vitorio Zanzara
# Алекс Глозман
# Анастасия Иванникова
# Олег Галеев

import re
# a, b = [int(i) for i in input().split()]
a, b = [int(i) for i in '1 5'.split()]


# a = input()
a = '359'
res_4 = ''


# Vitorio Zanzara
# Алекс Глозман
# Анастасия Иванникова
# Олег Галеев
# Виктор Григорович +







# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)
# matrix = [list(map(int, input().split())) for i in range(int(input()))]
matrix = [[1, 4, 5], [6, 7, 8], [1, 1, 6]]

# n, m = map(int, input().split())
# n, m = [int(input()) for _ in 'aa']
# print(m // n, m % n, sep='\n')




# from datetime import datetime, timedelta
#
#
#
# dt = datetime(year=1, month=1, day=1, minute=0, second=0)
# # delta = timedelta(seconds=int(input())*60)
# delta = timedelta(seconds=3602)
# res = dt + delta
# print(res.hour, res.minute, res.second)

# print(f"The next number for the number {(n:=int(input()))} is {n+True}.")
# print(f"The previous number for the number {(n:=int(input()))} is {n-True}.")

from datetime import datetime, timedelta

# a, b, c, d = [int(input()) for _ in range(4)]
# a, b, c, d = [int(input()) for _ in range(4)]

# Выведите его дробную часть.
a = 17.9
a = '1.79'

# a, b = [int(input()) for _ in 'aa']



# Функции eval() и ast.literal_eval() интерпретируют строки как код Python.
# ast.literal_eval() - обрабатывает только строки, представляющие литералы, более безопасный в применении.
# eval()             - функция способна выполнить любые команды.


# register_check = lambda x: len(__import__('re').findall(r'yes', str(x)))
# register_check = lambda x: len(__import__('re').findall(r'yes', str(x)))


import re






# JavaScript предоставляет встроенный метод parseInt. Его можно использовать следующим образом:
# parseInt("10")              возвращается 10
# parseInt("10 apples") также возвращается 10


# Реализуйте функцию createTemplate, которая принимает строку с тегами, упакованными {{brackets}}в качестве входных
# данных, и возвращает замыкание, которое может заполнять строку данными (плоский объект, где ключами являются имена тегов).

# Пример что должно быть на выходе

# template = create_template("{{name}} likes {{animalType}}")
# template(name="John", animalType="dogs")  # ->  John likes dogs



'aeiouy'
'bcdfghjklmnpqrstvwxzy'

import re
from itertools import pairwise, zip_longest

def sub_fun(m):
    if m[0] == 'FIRE':
        return

import re















# a = (1, 2, 3)
# b = (3, 4, 5)

# print(tuple({*a, *b}))
# print(tuple(set(a)+set(b)))

# a = ('John', 'Peter')
# b = (1, 2)
#
# print({key: value for key, value in zip(a, b)})
# print({key: value for key, value in (a, b)})
# print(dict(keys=a, value=b))
# print({key: b[i] for i, key in enumerate(a)})


# class Base:
#     def __init__(self):
#         self.val = 0
#
#     def add_one(self):
#         self.val += 1
#
#     def add_many(self, x):
#         for i in range(x):
#             self.add_one()
#
#
# class Derived(Base):
#     def add_one(self):
#         self.val += 10
#
#
# a = Derived()
# a.add_one()
#
# b = Derived()
# b.add_many(3)
#
# print(a.val)
# print(b.val)



from more_itertools import chunked


from itertools import tee

x = list(range(9, 15))
rez = tee(x, 3)

# for l in rez:
#     print(list(l))

# [9, 10, 11, 12, 13, 14]
# [9, 10, 11, 12, 13, 14]
# [9, 10, 11, 12, 13, 14]

# print([list(i) for i in tee([1, 2, 3], 2)])  # -> [[1, 2, 3], [1, 2, 3]]




import re








"""
ВАЖНО:
-   можно пользоваться поиском и документацией
-   плюсом будет применение чистых функций, функций высшего порядка
    и синтаксического сахара
-   также при написании web-сервиса будет большим плюсом
    распределение кода по модулям
***
ЗАДАЧА
* Уровень 1 *
1.  Распарсить CSV-строку в список словарей, ключи для которых взять из заголовка
    (built-in СТРОКОВЫМИ средствами)
2.  Нормализовать данные в словарях в соответствии с правилами
    Правила определить, исходя из наблюдаемых в данных отклонениях
* Уровень 2 *
Используя средства FastAPI разработать сервис с 1 методом,
принимающим на вход CSV-строку (валидация через MIME-тип)
и возвращающим JSON со списком словарей, нормализованных по правилам
* Уровень 3 *
Добавить параметры запроса для сортировки по одному полю
в режимах по убыванию и по возрастанию
(используя сущности FastAPI, Pydantic и стандартные средства типизации)
"""


# Задача Заказчик Открытые Решения

RAW_DATA = '''phone, fullname, some_amount, rating_position
+7 993 0965431, Абдуллаев Рамиль Ахмед оглы, 5432, 5
89615421187, Васильев Михаил Борисович, 1577.93, 3
+7 (905) 127-00-01, Филипс    Тревор, 7 311.63, 1
8-987-654-3210, Иванова    Мария Сергеевна, 104, 4
8931 077 2267, Петрова-Васильева     Светлана   Александровна, 35 567.92, 7
955-43-88-102, Крестовоздвиженский    Войцишек  Станислав   Август, 191, 6
7911-631-07-80,    Романов   Борис Анатольевич, 13.2, 2'''







"""
Тестовое задание: бинарная классификация на основе транзакционных аггрегатов
Описание задачи
Клиент приходит в банк и подает заявку на кредит. Необходимо оценить по данным об имеющихся транзакциях клиента выйдет
 ли он в дефолт (просрочка платежа более 90 дней за перый год жизни кредита).

У банка есть исторические данные о транзакциях клиентов и вызревших заявках (с временем жизни более года, чтобы была
 возможность адекватно оценить нашу целевую переменную)

Используя эти данные необходимо построить модель бинарной классификации (Выполнить задания ниже)

Описание данных
Данные:

Application.csv (Таблица заявок)
client_id (id клиента, уникальный ключ таблицы)
app_date (дата заявки)
flag_dr (флаг выхода в дефолт - бинарная переменная (0, 1), целевой признак)
Transaction.csv (Таблица транзакций)
client_id (id клиента)
trans_date (дата транзакции)
amount (сумма транзакции)
category (категория транзакции)
"""


# Task 1
"""Прочитайте данные
Присоедините к заявкам все актуальные на момент заявки транзакции"""


# Task 2
"""
Поисследуйте данные:

Посчитатйте среднее количество транзакций у клиента
Выведите список уникальных категорий транзакций
Посчитайте среднюю сумму транзакций для каждой категории
Постройте график распределения количества транзакций у клиента
Постройте target rate в динамике по месяцам
"""


# Task 3.1
"""
Соберите следующие агрегаты:

Флаг наличия транзакции типа petrol (бинарная)
Количество транзакций типа alcohol
Посчитать отношение суммы трат к сумме поступлений (поступления - income_tranz, траты - все остальное)
Средняя велична последних 3 транзакций типа income_tranz
"""



# Task 3.2

"""
Выведите посчитанные значения для клиентов с id 2851, 463, 1281, 1530, 774, 1816
"""


# Task 4

"""
Разделите выборку на train/test следующим образом:

Train - заявки до июня 2020 включительно
Test - заявки с июля 2020 включительно
"""


# Task 5

"""
Используя полученные фичи, постройте модель логистической регрессии и посчитайте метрику roc auc score на Train и Test выборках
"""





# SOLID - РАСПИСАТЬ ПРИМЕРЫ
# ВСЕ МИНУСЫ С СОБЕСА ПРОЧИТАТЬ!!!


# Миша Горелик  Высокопроизводительные Python-приложения.    # High Performance Python" by Micha Gorelick and Ian Ozsvald
# Марк Лутц  Изучаем Python

# Написать все алгоритмы сортировок


class Data:
    def __del__(self):
        print('Data.__del__')


class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []


    # НИКОГДА ТАК НЕ ДЕЛАЙТЕ
    # ПОКАЗАНО ТОЛЬКО ДЛЯ ДЕМОНСТРАЦИИ ПАТОЛОГИЧЕСКОГО ПОВЕДЕНИЯ
    def __del__(self):
        del self.data
        del self.parent
        del self.children

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# В ЭТОМ СЛУЧАЕ СТУРУКТУРА ДАННЫХ НИКОГДА НЕ БУДЕТ УДАЛЕНА СБОРЩИКОМ МУСОРА
a = Node()
a.add_child(Node())
# Data.__del__
# Data.__del__
del a            # Нет сообщения (не собрано)
import gc
gc.collect()     # Нет сообщения (не собрано)


# БУДЕТ УДАЛЕНА СБОРЩИКОМ МУСОРА   Слабые ссылки решают проблему ссылочных циклов   <-----
import weakref
a = Node()      # -> Data.__del__
a_ref = weakref.ref(a)
print(a_ref)    # -> <weakref at 0x0000029705565490; to 'Node' at 0x000002977FACEAD0>
print(a_ref())  # -> <__main__.Node object at 0x000001AD3FA8EB10>
del a
Data.__del__
print(a_ref())  # -> None



























































































































































































