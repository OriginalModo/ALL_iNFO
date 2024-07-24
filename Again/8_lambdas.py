# аналог def!!
# можно писать всё что допустимо после retrun в def
# не выполняется до вызова ()!!!
# значения по умолчанию вычисляются в момент создания функции (аргумент функции)
# можно писать код без лямбд
#  # с 3.8 itemgetter работает бысрее лямбд

from operator import attrgetter, itemgetter


def square(x):
    return x ** 2


def is_even(x):
    return x % 2 == 0


def second(x):
    return x[1]


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'


_any = lambda: abracadabra  # не выполняется до вызова ()!!!
_any2 = lambda: square(use(it))  # не выполняется до вызова ()!!!

if __name__ == '__main__':
    ints = list(range(10))
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, ints))))
    print([i ** 2 for i in ints if i % 2 == 0])
    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}
    print(sorted(a_dict.items(), key=lambda x: x[0]))
    print(sorted(a_dict.items(), key=itemgetter(0)))
    cats = [Cat('Tom', 3), Cat('Angela', 4)]
    print(sorted(cats, key=lambda cat: cat.age))
    print(sorted(cats, key=attrgetter('age')))

# TRY THIS 3


# if __name__ == '__main__':
#     x = 2
#     result = lambda n=x: n ** 2
#     x = 3
#     result2 = lambda n=x: n ** 2
#     print(result())
#     print(result2())
#


# TRY THIS 2

# if __name__ == '__main__':
#     x = 2
#     result = lambda: x ** 2
#     x = 3
#     result2 = lambda: x ** 2
#     print(result())
#     print(result2())


# TRY THIS 1

# def square(x):
#     ggg
#     return x ** 2
#
# # square2 = lambda x: x ** 2
# # even_ood = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'
# # even_ood = lambda x: x**2 if x % 2 == 0 else 'gg'
#
# _any = lambda: abracadabra # не выполняется до вызова ()!!!
# _any2 = lambda: square(use(it)) # не выполняется до вызова ()!!!
#
# if __name__ == '__main__':
#     abracadabra = 100
#     print(_any())
#     print(_any2)
#     print(square)
