import pprint
from time import sleep

# List comprehension = Listcomps
# Generator expressions - genexp

# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# переменные в листкомпс недоступны извне
# читается слева направо
# для словаря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ
# генератор вернет обьект, а не коллецию
# генератор ленивый, не выполняет действий и не занимает память пока не потребуется
# генератор проверяет источник при создании!!!
# генератор одноразовый, если исчерпан то бросает StopIteration
# цикл for перехватывает StopIteration
# используйте генэксп вместо компс, кроме случаев когда нужна длина len или индексы


squares = [i ** 2 for i in range(10) if i % 2 == 0]

text = 'hello world'
words = [i.capitalize() for i in text.split()]

ints = [-1, -2, 0, 3, -4]
positives = [i for i in ints if i > 0]

squares2 = []
for i in range(10):
    if i % 2 == 0:
        squares2.append(i ** 2)

letters = [letter for word in text.split() for letter in word if letter < 'l']

matrix = [list(range(i, i + 3)) for i in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

alphabet = {index: letter for index, letter in enumerate('abcdefghijklnop', 1)}

positives_gen = (i for i in range(10_000) if i > 0)


def some_source():
    print('!!!')
    sleep(3)
    return [1, 2, 3]


def some_source_1():
    return 1, 2, 3


def some_filer(x):
    sleep(1)
    return 1


def some_mapping(x):
    sleep(1)
    return x


if __name__ == '__main__':
    # pprint.pprint(matrix, indent=1, width=15)
    # print({value: key for key, value in alphabet.items()})
    # print(next(positives_gen))
    gen = (i for i in some_source())
    it = (some_mapping(i) for i in some_source_1() if some_filer(i))
    print(next(it))
