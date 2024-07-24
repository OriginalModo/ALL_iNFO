import functools
from itertools import zip_longest
from timeit import timeit
import asyncio
from dataclasses import dataclass

from pympler import asizeof
from time import time, perf_counter
from functools import wraps


# # zip_longest
# MISSING = object()
#
# def combine(*args):
#     return [
#         j for i in zip_longest(*args, fillvalue=MISSING)
#         for j in i if j is not MISSING
#     ]
#
# print(combine(['a', 'b', 'c'], [1, 2, 3]))
# print(combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]))

# # Мультисловарь
# from collections import defaultdict
#
# a_dict = defaultdict(list)
# for char in 'hello':
#     a_dict[char].append(char)
#
# print(a_dict)

# from collections import deque # ДВУНАПРАВЛЕННАЯ ОЧЕРЕДЬ

# a_deque = deque()
# a_deque.append(1)
# a_deque.pop()
# print(a_deque)
# a_deque.appendleft(2)
# print(a_deque)

# a_deque = deque([1,2,3])
# a_deque.pop()
# print(a_deque)
# a_deque.popleft()
# print(a_deque)

# from collections import namedtuple
#
# Cat = namedtuple('Cat', 'name age color')
# tom = Cat('Tom', 4, 'yellow')
# print(tom)
# print(tom.name)
# print(tom.age)

# from operator import itemgetter, attrgetter # Работаем быстрее lambda
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Cat({self.name}, age is {self.age})'
#
#
# a_dict = {'a':3, 'b':2, 'd':1, 'c':4}
# print(sorted(a_dict.items(), key=lambda x:x[1]))
# print(sorted(a_dict.items(), key=itemgetter(1)))
# cats = [Cat('Tom', 3), Cat('Angela', 4)]
# print(sorted(cats, key=attrgetter('name')))
# print(sorted(cats, key=lambda x:x.name))

# # Факториал лямбда+рекурсия
# fact = lambda number: number * fact(number - 1) if number > 1 else number
#
# fact = lambda number: number * fact(number - 1) if number > 1 else (1 if number == 0 else number)
#
# fac = lambda x: 1 if x == 0 else x * fac(x - 1)
#
# factorial = lambda n: 1 if n <= 1 else factorial(n - 1) * n
#
# def factorial1(n):
#     if n >= 1:
#         return n * factorial(n - 1)
#     return 1
#
# print(factorial1(5))
#
# print(factorial(5))
# print(fact(5))
#
# from functools import reduce
# print(reduce(lambda x, y: x * y, range(1, 6), 1))  # !5  ->120
#
# print([(lambda x: x*x)(x) for x in range(10)])
# print([lambda x: x*x for x in range(10)])



# fact = lambda x: 1 if x == 0 else x * fact(x-1)
# print(fact(5))
#
# def factorial1(n):
#     if n >= 1:
#         return n * factorial1(n - 1)
#     return 1
#
#
# print(factorial1(5))

# factt = lambda x: 1 if x == 0 else x * factt(x-1)
# print(factt(5))

# from collections import deque
#
# a_deque = deque([1,2,3], maxlen=3)
# print(a_deque)
# a_deque.append(4)
# print(a_deque)


# from collections import defaultdict
#
# a_dict = defaultdict(int)
# print(0 in a_dict)
# for i in 'hello':
#     a_dict[i] +=1
#
# print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True)

# from collections import Counter
#
# counter = Counter('hello gppp   very')
# print(counter)
# print(counter.most_common(3))


# from collections import Counter
#
# counter = Counter('hello')
# print(counter)
# counter.update('world')
# print(counter)

# from collections import ChainMap
#
# first = {1: 1, 2: 2, 3:3}
# second = {4: 4, 5: 5}
#
# chain = ChainMap(first, second)
# print(chain)
# print(5 in chain)
# first[1]=100
# first[5]=200
# print(chain)

# from collections import OrderedDict
#
# first = {1: 1, 2: 2, 3:3}
# second = {2: 2, 1: 1}
#
# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
# # print(order1 == order2)
# # print(order1.popitem(last=False))
# # order1.move_to_end(1)
# order1.move_to_end(3, last=False)
# print(order1)

# a_list = ['aaa', 'bb', 'cc', 'd']
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Cat({self.name=}, {self.age=})'


# cats = [Cat('Tom', 3),Cat('Angela', 4),Cat('Bob', 5)]
# print(max(cats, key=lambda x: x.age))
# print(max(a_list,key=len))
# for line in iter(input, 'end'):
#     print(line.upper())

# ints = [int(i) for i in iter(input, '')]
# print(ints)


# a_list = [0, 0, 1, True, 'sd']
#
# if any(a_list):
#     print(list(filter(None, a_list)))
#     print([i for i in a_list if i])


# from itertools import combinations
#
# print(list(combinations('123', 2)))
#
# # [('1', '2'), ('1', '3'), ('2', '3')]
#
# from itertools import permutations
#
# print(list(permutations('123', 2)))
#
# # [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]


# from itertools import chain
#
# chained = chain('ab', [33])
# print(next(chained))
# print(next(chained))
# print(next(chained))

# from collections import namedtuple
#
# Point = namedtuple("Point", "x y")
# print(issubclass(Point, tuple))
#
# point = Point(2, 4)
# print(point)
#
# print(point.x)
# print(point.y)
#
# print(point[0])
# print(point[1])

# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0

# @dataclass()
# class MyIterator:
#     data: list = None
#     index: int = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration('nice')
#         result = self.data[self.index]
#         self.index += 1
#         return result
#
#
# cool_iter = MyIterator([1, 2])
# # print(next(cool_iter))
# # print(next(cool_iter))
# # print(next(cool_iter))
# for i in cool_iter:
#     print(i)


# def repeater(repeat=1):
#     """Повторение выполнения кода"""
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(repeat):
#                 print(f'{i+1}: ', end='')
#                 val = func(*args, **kwargs)
#             return val
#         return wrapper
#     return decorator
#
# @repeater(repeat=3)
# def say(name):
#     print(f'Hello {name}!')
#
# say('hi')


# def real_dcor(n):
#     def my_decor(func):
#         def wrapper(*args, **kwargs):
#
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return my_decor
#
#
# @real_dcor(5)
# def foo():
#     print('hello')
#
#
# foo()


# class Decor:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         res = self.func(*args, **kwargs)
#         finish = perf_counter()
#         print(f'{finish-start:.6}')
#         return res
#
# def real_decor(func):
#     def wrapper(*args, **kwargs):
#         start = perf_counter()
#         res = func(*args, **kwargs)
#         finish = perf_counter()
#         print(f'{finish-start:.4}')
#         # return func(*args, **kwargs)
#         return res
#     return wrapper
#
# @Decor
# @real_decor
# def fact(n):
#     pr = 1
#     for i in range(1,n+1):
#         pr*=i
#     return pr
#
# @Decor
# @real_decor
# def fib2(x: int):
#     return fib(x)
#
# # @real_decor
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#
#         return fib(n-1) + fib(n-2)
#
#
# # fact = real_decor(fact)(5)
# # fact = real_decor(fact)
# # print(fact(5))
# print(fib2(10))
# print(fact(5))


# def greet_deeply_curried(greeting):
#     def w_separator(separator):
#         def w_emphasis(emphasis):
#             def w_name(name):
#                 print(greeting + separator + name + emphasis)
#             return w_name
#         return w_emphasis
#     return w_separator
#
# greet = greet_deeply_curried("Hello")("...")(".")
# greet('German')
# greet('Ivan')

# from functools import reduce
#
# a_list = [1, 2, 3, 4]
#
# new_list = reduce(lambda x, y:x*y if x > y else x+y, a_list)
# print(new_list)
#
# all_max = reduce(lambda a,b: a if (a > b) else b, a_list)
# print(all_max)


# a_list = [1, 2, 3, 4]
# numbers = [1, 2, 3, 4]
#
# new_list = list(map(lambda x: x+ 2,
#                     (filter(lambda x: x > 2, a_list))))
# new_list2 = [i+2 for i in a_list if i > 2]
# print(new_list)
# print(new_list2)
#
# e = list(map(lambda x : x * 2,
#              filter(lambda x : x > 10,
#                     map(lambda x : x * 3,
#                         filter(lambda x : x > 3, numbers)))))
# print(e)


# def foo(bar=None):
#     if bar is None:
#         bar = []
#     bar.append(1)
#     return bar
#
#
# print(foo())
#
# print(foo())
#
# print(foo())

# l = list(range(1000000))
# d = dict.fromkeys(l)
# s = set(l)
# t = tuple(l)
# def iter_list():
#     for i in l:
#         pass
#
# def iter_dict():
#     for i in d:
#         pass
# def iter_set():
#     for i in s:
#         pass
# def iter_tuple():
#     for i in t:
#         pass
#
# print(timeit(iter_list, number=1000))
#
# print(timeit(iter_tuple, number=1000))
#
# print(timeit(iter_dict, number=1000))
#
# print(timeit(iter_set, number=1000))

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

# # словарь своими руками
# class MyDictionary:
#     def __init__(self):
#         self.size = 10
#         self.keys = [None] * self.size
#         self.values = [None] * self.size
#
#     def __setitem__(self, key, value):
#         index = hash(key) % self.size
#         self.keys[index] = key
#         self.values[index] = value
#
#     def __getitem__(self, item):
#         index = hash(item) % self.size
#         return self.values[index]
#
#
# d = MyDictionary()
# d['apple'] = 'red'
# print(d['apple'])

# a_list = list(range(10))
#
# print(asizeof.asizeof(a_list))
# print(timeit('list(range(10))'))
# print(timeit('a_list', 'from __main__ import a_list'))

# import sys
# arr_1 = []
# arr_2 = arr_1
# print(sys.getrefcount(arr_1))


# b_list = [1, 2, 3, 4, 5]
# a_list = [1, 2, 3]
# print(all(i in b_list for i in a_list))
# print(set(b_list).issubset(a_list))


# a_list = [1, 2, 3]
# a_set = {1, 2, 3}
# a_tuple = (1, 2, 3)
# a_dict = {'good': 'a', 2: 'b'}
# a_frosenset = frozenset({1, 2, 3, 4, })
# print(type(a_frosenset))
# print(a_dict['good'])
# print(hash(a_frosenset))
# # a_list.sort(reverse=True)
# a_list = sorted(a_list, key=lambda x: x > 2)
# b_list = [i for i in a_list if i >= 2]
# c_list = list(filter(lambda x: x >= 2, a_list))
# # sorted(a_list, reverse=True)
# print(a_list, b_list, c_list, sep='\n')
# print(map())


# first_tuple = (1, 2, 3, 4, 5)
# second_tuple = (2, 4, 5)
#
# dupli1 = all(i in first_tuple for i in second_tuple)
# dupli2 = set(second_tuple).issubset(first_tuple)
# print(dupli1)
# print(dupli2)

# import asyncio
#
# async def first():
#     await asyncio.sleep(1)
#     print('first')
#
# async def two():
#     await asyncio.sleep(2)
#     print('two')
#
# async def main():
#     await asyncio.gather(first(), two())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# a = [[1, 2, 3], [4, 5, 6]]
# # b = list(a)
# b = a.copy()
# # b = a[:]
# print(a)
# # [[1, 2, 3], [4, 5, 6]]
# print(b)
# # [[1, 2, 3], [4, 5, 6]]
# a[0][1] = 10
# print(a)
# # [[1, 10, 3], [4, 5, 6]]
# print(b) # b changes too -> Not a deepcopy.
# # [[1, 10, 3], [4, 5, 6]]
# print(id(a), id(b))
# print('-'*20)
# import copy
# a = [[1, 2, 3], [4, 5, 6]]
# b = copy.deepcopy(a)
# print(a)
# # [[1, 2, 3], [4, 5, 6]]
# print(b)
# # [[1, 2, 3], [4, 5, 6]]
# a[0][1] = 10
# print(a)
# # [[1, 10, 3], [4, 5, 6]]
# print(b) # b changes too -> Not a deepcopy.
# # [[1, 10, 3], [4, 5, 6]]
