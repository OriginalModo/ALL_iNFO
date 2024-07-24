# Closure Замыкание
# Замыкание(Closure) - Внутренняя функция которая возвращается из внешней и при этом
# использует переменные из внешнего Scope(Область видимости)
# каждое замыкание хранит своё состояние, они не пересекаются
# хранит состояние(данные), предоставляет интерфейс для работы с ними, "скрывает" данные и помогает избегать global


def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    values = []
    def inner(value: int)-> float:
        values.append(value)
        return sum(values) / len(values)
    return inner


if __name__ == '__main__':
    boys = names()
    girls = names()
    print(boys('Vasya'))
    print(boys('Petya'))
    print(boys('Dima'))
    print(girls('Lena'))
    print(girls('Olya'))
    print(girls('Sveta'))

    avg = average()
    print(avg(10))
    print(avg(20))
    print(avg(30))

