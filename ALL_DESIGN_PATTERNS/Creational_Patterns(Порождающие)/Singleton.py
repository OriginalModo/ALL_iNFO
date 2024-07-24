"""
Одиночка (Singleton):

Суть: Класс будет представлен в системе в ЕДИНСТВЕННОМ ЭКЗЕМПЛЯРЕ и предоставляет к нему глобальную точку доступа

Для того чтобы использовать паттерн Одиночка (Singleton): нужно использовать МЕТАПРОГРАММИРОВАНИЕ

В каких случаях рекомендуется использовать:
1) В системе должен существовать только один экземпляр класса, доступ к которому легко получить из любой точки клиентского кода

Плюсы:
--- Singleton позволяет с любой точки клиентского кода обратиться к его единственному экземпляру
--- создание экземпляра осуществляется по принцыпу отложенной инициализации

Минусы:
--- Бездумное использование паттерна Singleton может привести к плохому дизайну архитектуры
"""

# 1 Вариант
class SingletonBaseClass(type):
    _instances = {}


    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]


class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = 'Singleton'
        self.value_a = 3
        self.value_b = 5

# # 1 Вариант
# class MySingleton:
#     _instances = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instances is None:
#             cls._instances = super().__new__(cls)
#         return cls._instances
#
#
#     def __init__(self):
#         self.name = 'Singleton'
#         self.value_a = 3
#         self.value_b = 5


    def add_a_b(self) -> int:
        return self.value_a+self.value_b

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


if __name__ == '__main__':
    my_singleton1 = MySingleton()
    my_singleton2 = MySingleton()
    print('Singleton1 name: '+my_singleton1.get_name())
    my_singleton1.set_name('New Singleton')
    print('Singleton2 name: '+my_singleton2.get_name())
    print(my_singleton1)
    print(my_singleton2)
    print(id(my_singleton1) == id(my_singleton2))

