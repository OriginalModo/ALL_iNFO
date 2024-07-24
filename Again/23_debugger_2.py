# Важные моменты:
# 1) в стеке вызовов мы можем посмотреть состояние нашей программы (переменных) на прошлых этапах выполнения.
# Это позволяет понять откуда пошла проблема
# 2) Evaluate - это инструмент, который позволяет выполнять какие то вычисления,
# проверять код и даже менять значения в текущем скоупе, что может быть удобно
# для проверки каких то предположений об ошибке
# 3) Отслеживание (watches) - помогает нам следить за значениями каких-либо переменных по ходу выполнения программы

def one(x, y):
    result = x + y
    return two(result)


def two(result):
    result = f'{result}!!'
    return three(result)


def three(result):
    return 100 / result.count('!')


def cycle(value):
    even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
    for i in range(6):
        value += i
        print(value)
    return value


if __name__ == '__main__':
    cycle(50)
