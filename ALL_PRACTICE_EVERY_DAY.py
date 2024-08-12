import collections
import time
import types


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
"""def names():
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



# Написать Рекурсию сумма Входного списка




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


# Использовать __slots__



# Демонстрация __slots__ :
"""
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


# Как создать класс без слова class?




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




print('1' if True else '0')  # -> 1











































































































































































































































































































































































































