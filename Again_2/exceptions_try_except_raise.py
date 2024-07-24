class ArgumentEqualZeroError(Exception):
    """Выбрасывается когда делитель равен 0"""
    pass
class ArgumentIsNotIntegerError(Exception):
    """Выбрасывается если агрумент не целое число"""
    pass

def divide(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentIsNotIntegerError('Аргументы должны быть целыми числами')
    if b == 0:
        raise ArgumentEqualZeroError('Делитель не может быть равен 0')
    return a // b


if __name__ == '__main__':
    try:
        result = divide(4, 0)
    except (ArgumentIsNotIntegerError, ArgumentEqualZeroError) as exc:
        print(exc)
    finally:
        print('Finish')

