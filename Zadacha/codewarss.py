import dis
import functools
import gc
import heapq
import itertools
import operator
import random
import string
import sys
import time
import types
from functools import partial, reduce
from operator import add, sub, mul, truediv
from collections import Counter, OrderedDict, deque, defaultdict
from copy import copy, deepcopy
from itertools import chain, combinations, zip_longest, permutations, accumulate, groupby
import math
from math import copysign
from math import factorial as ffff
from numbers import Number
from fractions import Fraction
from time import perf_counter
import weakref
import statistics

import attr.validators
import numpy
from datetime import datetime, timedelta
import collections
from timeit import timeit
from pympler import asizeof
from collections import ChainMap
from more_itertools import distinct_permutations


# def two_highest(arg1):
#     arg2 = list(set(arg1))
#     heapq._heapify_max(arg2)
#     result = list([heapq._heappop_max(arg1), heapq._heappop_max(arg2)])
#     return result if len(arg2) > 1 else list(arg1)


import datetime

d = datetime.date.today()
print(d.strftime('%d/%m/%y'))  # -> '31/05/24'
print(d.strftime('%A %d. %B %Y'))  # -> 'Friday 31. May 2024'

dt = datetime.datetime.now()
print(dt.strftime('%H:%M - %m.%d.%Y года'))  # -> '15:46 - 05.31.2024 года'
print(dt.strftime('%H часов %M минут %m.%d.%Y года'))  # -> '15 часов 46 минут 05.31.2024 года'
print(dt.strftime('%m/%d/%y'))  # -> '05/31/24'
print(dt.strftime('%Y-%m-%d'))  # ->'2024-05-31'

# Можно использовать f-string вместо strftime
print(dt.strftime('%Y-%m-%d'))  # ->'2024-05-31'
print(f"{dt:%Y-%m-%d}")         # ->'2024-05-31'
print(f'День: {dt:%d}, Месяц: {dt:%B}, время: {dt:%H:%M}.')  # -> 'День: 31, Месяц: May, время: 15:46.'




# import heapq
# h = [20, 10, 1]
# print(h)         # -> [20, 10, 1]
# heapq.heapify(h) # создаем кучу(heap)
# print(h)         # -> [1, 10, 20]
# print(h[0])      # -> 1
# heapq.heappop(h)
# print(h)         # -> [10, 20]
# print(h[0])      # -> 10



# # Классное решение!!!
# def lottery(s):
#     return ''.join(dict.fromkeys(filter(str.isdigit, s))) or 'One more run!'
#
# print(lottery('wQ8Hy0y5m5oshQPeRCkG'))
# print(lottery('ffaQtaRFKeGIIBIcSJtg'))
# print(lottery('555'))
# print(lottery('HappyNewYear2020'))
# print(lottery('20191224isXmas'))
# print(lottery(''))


# def empty_values(lst):
# 	return [type(x)() for x in lst]

## РЕШЕНИЕ ЛЕГКОЕ ЕСТЬ! ОНО ВЫШЕ
# def empty_values(lst):
#     res = []
#     for i in lst:
#         if isinstance(i, int):
#             res.append(int())
#         elif isinstance(i, str):
#             res.append(str())
#         elif isinstance(i, float):
#             res.append(float())
#         elif type(i) == bool:
#             res.append(False)
#         elif isinstance(i, list):
#             res.append(list())
#         elif isinstance(i, tuple):
#             res.append(tuple())
#         elif isinstance(i, dict):
#             res.append(dict())
#         elif isinstance(i, set):
#             res.append(set())
#         elif i is None:
#             res.append(None)
#     return res
#
#
# print(empty_values([1, 2, 3]))
# print(empty_values([None, [None], (None,[None]), {None}, True, 7, "None"]))





# Как-то придумал же))))
# list1 = [
#     {'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python'},
#     {'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java'}
# ]
#
# def find_odd_names(lst):
#     return [i for i in lst if sum(map(ord, list(i['firstName']))) % 2 != 0]
#
# print(find_odd_names(list1))




# крутое решение - посчета количества круглых скобок
# def eval_parentheses(s):
#     return eval(s.replace(')(', ')+(').replace('()', '1').replace('(', '2*('))
#
#
# print(eval_parentheses("()"))
# print(eval_parentheses("(())"))
# print(eval_parentheses("()()"))
# print(eval_parentheses("((())())"))
# print(eval_parentheses("(()(()))"))





# l1 = [1, 4, 8, 7, 3, 15]
# l2 = [1, -2, 3, 0, -6, 1]
# l3 = [20, -13, 40]
# l4 = [1, 2, 3, 4, 1, 0]
# l5 = [10, 5, 2, 3, 7, 5]
# l6 = [4, -2, 3, 3, 4]
# l7 = [0, 2, 0]
# l8 = [5, 9, 13, -3]
# # l9 = [1] * 10000000
#
# def sum_pairs(ints, s):
#     lst = set()
#     for i in ints:
#         res = s - i
#         if res in lst:
#             return [res, i]
#         lst.add(i)


# print(sum_pairs([11, 3, 7, 5],         10))
# print(sum_pairs(l1,         8))
# print(sum_pairs(l2,         -6))
# print(sum_pairs(l3,         -7))
# print(sum_pairs(l4,         2))
# print(sum_pairs(l5,         10))
# print(sum_pairs(l6,         8))
# print(sum_pairs(l7,         0))
# print(sum_pairs(l8,         10))
# print(sum_pairs(l9,         13))
# print(sum_pairs(l9,         5))
# print(sum_pairs(l9,         16))


# pi = 3.141592
# result = 121
# print(f'{pi:.2f}')  # f'{pi:.2f <- сколько будет после запятой}'
# print(f'{result:06}') # запосление нулями
# print(f'{result:^12}') # заполение пробелы по центру
# print(f'{result:0^12}') # заполение нулями по центру
# print(f'{result:>12}') # заполение пробелами слева
# print(f'{result:<12}') # заполение пробелами справа

# def is_leap(n):
#     return eval('n%4==0 and n%100!=0 or n%400==0')
#
#
# print(is_leap(2000))
# print(is_leap(1692))
# print(is_leap(1731))
# print(is_leap(1987))
# print(is_leap(2001))
# print(is_leap(2014))
# print(is_leap(2012))


#elif symbol in close_symbols: # проходит условие
# if symbol in close_symbols: # Не проходит условие

# def is_balanced(source, caps):
#     open_symbols = caps[::2]
#     close_symbols = caps[1::2]
#     stack = []
#     for symbol in source:
#         if symbol in open_symbols:
#             if symbol in close_symbols and stack and stack[-1] == symbol:
#                 stack.pop()
#             else:
#                 stack.append(symbol)
#         elif symbol in close_symbols:
#         # if symbol in close_symbols: # Не проходит условие
#             if not stack or open_symbols[close_symbols.index(symbol)] != stack[-1]:
#                 return False
#             else:
#                 stack.pop()
#     return not stack
#
#
# print(is_balanced("(Sensei says yes!)", "()"))
# print(is_balanced("(Sensei says no!", "()"))
# print()
# print(is_balanced("(Sensei [says] yes!)", "()[]"))
# print(is_balanced("(Sensei [says) no!]", "()[]"))
# print()
# print(is_balanced("Sensei says -yes-!", "--"))
# print(is_balanced("Sensei -says no!", "--"))




# def is_balanced(source, caps):
#     source = [i for i in source if i in caps]
#     caps = dict(zip(caps[::2], caps[1::2]))
#     stack = []
#     for i in source:
#         if stack and i == caps.get(stack[-1], ''):
#             stack.pop()
#         else:
#             stack.append(i)
#     return not stack




# print(is_balanced("(Sensei says yes!)", "()"))
# print(is_balanced("(Sensei says no!", "()"))
# print()
# print(is_balanced("(Sensei [says] yes!)", "()[]"))
# print(is_balanced("(Sensei [says) no!]", "()[]"))
# print()
# print(is_balanced("Sensei says -yes-!", "--"))
# print(is_balanced("Sensei -says no!", "--"))






# def bin_to_decimal(inp):
#     return int(inp, 2)
#
#
# print(bin_to_decimal("0"))



# def make_readable(seconds):
#     return f"{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02}"


# def solution(s):
#     return [i[0]+i[1] for i in zip_longest(s[::2], s[1::2], fillvalue='_')]


# def high_and_low(numbers):
#     return ' '.join(i(numbers.split(), key=int) for i in (max, min))
#
# print(high_and_low("1 2 3 4 5"))


# print(a_dict)
# print(a_dict.update(a_dict2))
# print(a_dict)

# def adjacent_element_product(array):
#     return max(map(operator.mul, array, array[1:]))
#
# print(adjacent_element_product([5, 8]))
# print(adjacent_element_product([1, 2, 3]))

# def valid_parentheses(paren_str):
#     braces = {"(": ")"}
#     stackk = []
#     for i in paren_str:
#         if i in braces.keys():
#             stackk.append(i)
#         else:
#             if len(stackk) == 0 or braces[stackk.pop()] != i:
#                 return False
#     return len(stackk) ==0

# def valid_parentheses(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0

# print(valid_parentheses("()"))

# def valid_braces(s):
#     stk, matcher =  [], {')':'(', "]":"[", "}":"{"}
#     for c in s:
#         if c in "([{": stk.append(c)
#         elif c in ")]}":
#             if not stk or stk[-1] != matcher[c]:
#                 return False
#             stk.pop()
#     return not stk



# def valid_braces(string):
#     braces = {'(': ')', '{': '}','[': ']'}
#     stackk = []
#     for i in string:
#         if i in braces.keys():
#             stackk.append(i)
#         else:
#             if len(stackk) == 0 or braces[stackk.pop()] != i:
#                 return False
#     return len(stackk) == 0



# def valid_braces(string):
#     while '[]' in string or '{}' in string or '[]' in string:
#         string = string.replace('()','')
#         string = string.replace('{}', '')
#         string = string.replace('[]', '')
#     return not string


# print(valid_braces("(){}[]"))
# print(valid_braces("(){}[]"))
# print(valid_braces("[({})](]"))
# print(valid_braces("())({}}{()][]["))


# oppp = {
#     'AND': lambda a, b: a & b,
#     'OR': lambda a, b: a | b,
#     'XOR': lambda a, b: a ^ b,
# }
#
# def logical_calc(array1, op):
#     return functools.reduce(oppp[op], array1[1:], array1[0])
#
#
# print(logical_calc([True, False], "AND"))
# print(logical_calc([True, False], "OR"))



# def zero(func=None): return 0 if not func else func(0)
# def one(func=None): return 1 if not func else func(1)
# def two(func=None): return 2 if not func else func(2)
# def three(func=None): return 3 if not func else func(3)
# def four(func=None): return 4 if not func else func(4)
# def five(func=None): return 5 if not func else func(5)
# def six(func=None): return 6 if not func else func(6)
# def seven(func=None): return 7 if not func else func(7)
# def eight(func=None): return 8 if not func else func(8)
# def nine(func=None): return 9 if not func else func(9)
#
# def plus(value):
#     return lambda x: x + value
#
# def minus(value):
#     return lambda x: x - value
#
# def times(value):
#     return lambda x: x * value
#
# def divided_by(value):
#     return lambda x: x // value
#
#
# print(seven(times(five())))
# print(seven(divided_by(four())))

# def zero(number=0):
#     if number == 0:
#         return number
#     return eval(f'0 {number}')
#
# def one(number=1):
#     if number == 1:
#         return number
#     return eval(f'1 {number}')
# def two(number=2):
#     if number == 2:
#         return number
#     return eval(f'2 {number}')
# def three(number=3):
#     if number == 3:
#         return number
#     return eval(f'3 {number}')
# def four(number=4):
#     if number == 4:
#         return number
#     return eval(f'4 {number}')
# def five(number=5):
#     if number == 5:
#         return number
#     return eval(f'5 {number}')
# def six(number=6):
#     if number == 6:
#         return number
#     return eval(f'6 {number}')
# def seven(number=7):
#     if number == 7:
#         return number
#     return eval(f'7 {number}')
#
# def eight(number=8):
#     if number == 8:
#         return number
#     return eval(f'8 {number}')
# def nine(number=9):
#     if number == 9:
#         return number
#     return eval(f'9 {number}')
#
# def plus(value):
#     return f'+ {value}'
# def minus(value):
#     return f'- {value}'
# def times(value):
#     return f'* {value}'
# def divided_by(value):
#     return f'// {value}'
#
# print(seven(times(five())))
# print(seven(divided_by(four())))



# def factory(x):
#     return lambda xx: list(map(lambda z: x * z, xx))
#
#
# facctt = factory(3)
# print(facctt([1, 2, 3]))
#
#
# class A:
#     pass
#
#
# print(weakref.getweakrefcount(A))
# print(sys.getrefcount(A))
# print(A.__dict__)
# print(A.__weakrefoffset__)


# def combine(*args):
#     FILL = object()
#     return [i for i in chain(*zip_longest(*args, fillvalue=FILL)) if i is not FILL]
#
#
# print(combine(['a', 'b', 'c'], [1, 2, 3]))
# print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]))

