# Closure Замыкание
# Замыкание(Closure) - Внутренняя функция которая возвращается из внешней и при этом
# использует переменные из внешенго Scope(Область видимости)
# каждое замыкание хранит своё состояние, они не пересекаются
# хранит состояние(данные), предоставляет интерфейс для работы с ними, "скрывает" данные и помогает избегать global

def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


# def pow_(base):
#
#     def inner(value):
#         return value ** base
#
#     return inner


def pow_(base):
    return lambda value: value ** base


if __name__ == '__main__':
    p = pow_(2)
    print(p(5))


    boys = names()
    boys('Vasya')
    print(boys.__closure__[0].cell_contents)


    # pow__ = pow_(2)
    # pow__2 = pow_(3)
    # print(pow__(5))
    # print(pow__(6))
    # print(pow__(7))
    # print(pow__2(5))
    # print(pow__2(6))
    # print(pow__2(7))
