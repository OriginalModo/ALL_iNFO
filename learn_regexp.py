import calendar
import collections
import copy
import csv
import datetime
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




lst = [3,2,3]
lst1 = 9

t = ('one', 'two')
for i in t:
    print(i) # -> one two

# t = ('one')
# for i in t:
#     print(i) # -> o n e
#
#
# t = ()
# print(t) # -> ()




























































































































































































































































































































































































































































































