# аналог def!!
# можно писать всё что допустимо после retrun в def
# не выполняется до вызова ()!!!
# можно писать код без лямбд

from operator import attrgetter, itemgetter


def square(x):
    return x ** 2


def is_even(x):
    return x % 2 == 0

def second(x):
    return x[1]


any_ = lambda: abracadabra
any2 = lambda: square(use(it))


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'

if __name__ == '__main__':
    ints = list(range(20))
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, ints))))
    print([i**2 for i in range(20) if i % 2 == 0])
    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}
    print(sorted(a_dict.items(), key=lambda x: x[0]))
    print(sorted(a_dict.items(), key=itemgetter(1)))
    cats = [Cat('Tom', 3), Cat('Angela', 4)]
    print(sorted(cats, key=lambda x: x.age))
    print(sorted(cats, key=attrgetter('age')))
