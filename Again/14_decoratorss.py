# Основное предназначение ДЕКОРАТОРА изменить поведение функции(кода) не меняя реализацию этой функции
# Суть декоратора в том, что мы можем менять поведение декорируемого объекта,
# при этом не меняя его собственную реализацию, его код.
# Функция -полноправный обьект (обьект первого класса)
# внутренняя функция может захватывать переменные из внешней
from functools import wraps


def logger(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} started')
        result = func(*args, **kwargs)
        print(f'{func.__name__} finished')

        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


@logger
def summ(a, b):  # в этот момент summ=wrapper
    return a + b


if __name__ == '__main__':
    # function = logger(summ)
    # print(function)

    # print(logger(summ)(3,4))

    # summ = logger(summ)
    # print(summ(2,3))
    print(summ(2, 3))
    print(summ.__name__)
    # print(summ)
