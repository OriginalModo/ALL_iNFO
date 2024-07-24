# Функция -полноправный обьект
# внутренняя функция может захватывать переменные из внешней


def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b):  # в этот момент summ=wrapper
    return a + b


if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))

    # print(logger(summ(2, 3)))
    # summ = logger(summ)
    # print(summ(2, 3))

    print(summ(2, 3))
