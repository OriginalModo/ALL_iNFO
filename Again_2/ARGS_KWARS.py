# позиционные аргументы всегда идут вначале
# / - всё что слева - только позиционные аргументы
# * - всё что справа - только keyward аргументы
# *args собирает все позиционные аргументы в кортеж
# *kwargs собирает все keyward аргументы в словарь


# a, *b = [1, 2, 3]
a, *_, c = 'abcd'


# a, b, c = 'abc'

def example(a, b, /, c, *, d):
    print(a)
    print(b)
    print(c)
    print(d)


def my_print(*args, **kwargs):
    print(f'Got keywards: {kwargs}')
    for arg in args:
        print(str(arg), **kwargs)


if __name__ == '__main__':
    # print(f'{a=}')
    # print(f'{b=}')
    # print(f'{c=}')
    # print(*[1, 2, 3])
    # example(1, 2, d=True, c=False)
    # my_print(1, 2, 3, 4, 5, sep=':', end='-')
    print(1, 2, **{'sep': ':', 'end': '-'})
    print(1, 2, sep=':', end='-')
