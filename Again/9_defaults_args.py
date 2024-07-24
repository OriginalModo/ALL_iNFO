# Интерпретатор проходит один раз
# Аргумент по умолчанию будет создан 1 раз при интерпретации

# Важно:
# 1) значение аргументу по умолчанию присваивается один раз при интерпретации кода. Только 1 раз!
# Сколько бы мы ни вызывали функцию, она будет использовать ссылку на один и тот же объект.
# 2) в аргументах по умолчанию используем только неизменяемые типы, например строки, числа, None
# 3) если по логике нашей функции все же нужен изменяемый тип
# (список, сет, словарь, объект нашего класса), то в аргументе приравниваем к None, а уже внутри функции прописываем логику.

from time import time, sleep

def print_n_times(value: str, n:int=10):
    for _ in range(n):
        print(value)
    some_function()

def some_function():
    print('some_function caled')
    return 1

# def calc(time_=[]):
def calc(time_=None):
    if time_ is None:
        time_ = []
    time_.append(1)
    return time_



if __name__ == '__main__':
    print(calc([1]))
    print(calc([22]))
    print(calc([]))
    print(calc([]))

# TRY THIS

# def print_n_times(value: str, n:int=10):
#     for _ in range(n):
#         print(value)
#     some_function()
#
# def some_function():
#     print('some_function caled')
#     return 1
#
# def calc(time_=some_function()):
#     print(time_)
#
#
#
# if __name__ == '__main__':
#     calc()
#     calc()
#     calc()
#     calc()
#     calc()


# TRY THIS

# def calc(time_=time()):
#     print(time_)
#
# if __name__ == '__main__':
#     calc()
#     calc()
#     sleep(2)
#     calc()
