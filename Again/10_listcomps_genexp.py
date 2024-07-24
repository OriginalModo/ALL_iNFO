import pprint
from time import sleep

# List comprehension = Listcomps (однострочник) киллер фича языка
# Generator expressions - genexp (однострочник) киллер фича языка

# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# переменные в листкомпс недоступны извне
# читается слева направо
# для словаря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ
# генератор вернет обьект, а не коллецию
# генератор ленивый, не выполняет действий и не занимает память пока не потребуется (next)
# генератор проверяет источник при создании!!! чтобы он был iterable
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

matrix = [list(range(x, x + 3)) for x in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'} # set comprehension

alphabet = {key: value for key, value in enumerate('abcdefghijklo', 1)}

positives_gen = (i for i in ints if i > 0)

def some_source():
    print('!!!')
    # sleep(3)
    return 1,2,3

def some_filter(x):
    sleep(1)
    return True

def some_mapping(x):
    sleep(1)
    return x

if __name__ == '__main__':
    it = (some_mapping(i) for i in some_source() if some_filter(i))
    print(next(it))


    # print({value: key for key, value in alphabet.items()})
    # print(letters)
    # pprint.pprint(matrix, indent=1, width=15)
