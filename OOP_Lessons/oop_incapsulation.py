# Инкапсуляция заключается в сборе в одно место (класс) данных и методов для работы с ними и
# предоставлении пользовател. публичного интерфейса(API(Публичный интерфейс))
# _ - (protected) знак того, что этот атрибут не предназначен для прямого использования. Работа обьекта не гарантируется,
# при использовании таких атрибутов
# __ - (private) под капотом преобразуется в object._Class__attribute (только для случаев когда начинается с __) Name MangLing
# Явное лучше неявного!!!

# Публичный АПИ(интерфейс) - это контракт, все методы будут работать, внутренняя же реализация не гарантируется.
# Совет - делать одно _ для врутренних атрибутов и реализаций, не перебарщивать с __ и сеттерами/геттерами

class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.__age = age
        self.__one__ = 1

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError(f'Age must be in range 1-120')
        self.__age = age

    def describe(self):
        print(f'I am {self._first_name} {self._last_name}, Im {self.__age} years old')


if __name__ == '__main__':
    ivan = Person('Ivan', 'Ivanov', 20)
    ivan._Person__age = 100
    # ivan.set_age(200)
    ivan.describe()
    # print(ivan._last_name)
    print(dir(ivan))
    # print(ivan._Person__age)

# import collections
# text = collections
# # text = '1213'
# print(dir(text))
# print([i for i in dir(text) if not i.startswith('_')])
