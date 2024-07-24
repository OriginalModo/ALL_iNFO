import doctest


def divide(a: int, b: int) -> int:
    """
    Делит первое число на второе и возвращает результат плюс 1
    :param a: целое число(делимое)
    :param b: целое число(делитель)
    :return: результат деления (частное) плюс 1
    :raises ValueError: если делитель равен нулю

    >>> divide(10,5)
    3
    >>> divide(2,2)
    2
    """
    if b == 0:
        raise ValueError('На 0 делить нельзя')
    return (a // b) + 1


if __name__ == '__main__':
    doctest.testmod()
