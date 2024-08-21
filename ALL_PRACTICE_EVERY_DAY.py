import collections
import functools
import time
import types


# Перепиши ниже Обновление словаря/множества




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





# Обьединение *   Объединения **   |

"""
from itertools import chain
# Обьединение *
A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set
L = [*A, *B, *C]
G = list(chain(A, B, C))
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


# Написать решение чтобы каждый раз создавался новый обьект








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






"""
# Итератор
it = iter([i*i for i in range(10)])
"""


# Напишите Функцию-Генератор  range(5) и Обычный генератор





"""
# Генератор
def generate_ints(N):
    for i in range(N):
        yield i

for i in generate_ints(5):
    print(i, end=' ')  # -> 0 1 2 3 4


# Тоже самое
generate_ints = (i for i in range(5))
print(generate_ints)
"""


# Напишите Функцию-Генератор  range(1, 5) и Обычный генератор  range(1, 5)








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
    
    cats = [Cat('Tom', 3), Cat('Angela', 4)]
    print(sorted(cats, key=lambda x: x.age))
    print(sorted(cats, key=attrgetter('age')))
    print(sorted(cats, key=attrgetter('name')))
"""


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

# Написать Решение с nonlocal и Решение с global   Переписать рещение выше чтобы НЕ было ошибки






# Ответ
"""
# Решение с nonlocal:                       Решение с global:
x = 10                                      x = 10
def foo():                                  def foo():
    x = 10                                      global x, z
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


# Как создать класс без слова class?  И Создать такой же обычный dataclass







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
   
   def foo(self):
       return self.x

my_ = MyClass()
print(my_.x)       # -> 42
print(my_.foo())   # -> 42
"""



# 1) Написать декоратор, который выводит на экран время работы произвольной функции:








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
for _ in range(10):
    print(next(fib_gen), end=' ')  # Выведет первые 10 чисел Фибоначчи начиная с a=1, b=2  # -> 1 2 3 5 8 13 21 34 55 89
"""


# Напишите Фибоначчи с кэшем и замер скорости работы timeit   globals=globals()/setup="from __main__ import fibonacci__3"






# Решения с мемоизацией КЭШ  Скорость O(n)
"""
import timeit
from pympler import asizeof
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


# # Создать Абстрактный класс  и Унаследоваться от него     from abc import ABC, abstractmethod





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


# Как запустить что-то в потоке и вывести результат?  ThreadPoolExecutor






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






























































































































































































































































































































































































































































































































































































































