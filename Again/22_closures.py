# Closure Замыкание
# Замыкание(Closure) - Внутренняя функция которая возвращается из внешней и при этом
# использует переменные из внешенго Scope(Область видимости)
# каждое замыкание хранит своё состояние, они не пересекаются
# хранит состояние(данные), предоставляет интерфейс для работы с ними,
# "скрывает" данные и помогает избегать global

# Каждый объект замыкания независим, они не пересекаются, у каждого свои данные.
# Замыкания это еще один шаг в сторону ООП, так как тут мы имеем некоторое состояние (данные)
# сокрытое от посторонних глаз и с которым можно взаимодействовать только с помощью заранее написанного интерфейса (функция).
# Замыкания могут быть полезны для того чтобы избегать использования global, а также и в других случаях,
# когда нам важно, чтобы наши данные не изменили невалидным способом, чтобы с данными работали только через нашу логику.
# НО(!) до этих данных тоже можно добраться при определенном желании, нужно понимать что нет полного сокрытия данных.

def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


# def average():
#     values = []
#
#     def inner(value: int) -> float:
#         values.append(value)
#         return sum(values) / len(values)
#
#     return inner

def counter():
    count = 0
    def inner(value:int)-> int:
        nonlocal count
        count+=value
        return count
    return inner

def pow_(base):

    def inner(value):
        return value**base
    return inner

# version lambda
def pow_(base):
    return lambda value: value**base



if __name__ == '__main__':
    p = pow_(2)
    print(p(5))
    # boys = names()
    # # boys('Vasya')
    # boys('Sasya')
    # print(boys.__closure__[0].cell_contents)
    # pow__ = pow_(2)
    # pow_2 = pow_(3)
    # print(pow__(5))
    # print(pow__(6))
    # print(pow__(7))
    # print(pow_2(5))
    # print(pow_2(6))
    # print(pow_2(7))
    # print(pow__.__closure__[0].cell_contents)
    # count = counter()
    # # print(count.__closure__[].cell_contents)
    # print(count(1))
    # print(count(1))
    # print(count(1))
    # print(count(-3))

    # avg = average()
    # print(avg(10))
    # print(avg(20))
    # print(avg(30))
    # boys = names()
    # girls = names()
    # print(boys('Vasya'))
    # print(boys('Petya'))
    # print(boys('Dima'))
    # print(girls('Lena'))
    # print(girls('Sveta'))
    # print(girls('Olga'))
