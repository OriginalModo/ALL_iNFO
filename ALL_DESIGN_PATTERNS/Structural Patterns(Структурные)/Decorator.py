"""
Декоратор (Decorator):

Суть: для динамического добавления обьекту новой функциональности путем оборачивания его в некоторый класс обёртку


В каких случаях рекомендуется использовать:
1) имеется необходимость динамически и незаметно для клиентского кода добавлять обязаности существующим обьектам
2) нет возможности использовать наследование для расширения функциональности обьекта
3) обязаности, накладываемые на обьект, могут быть с него сняты

Плюсы:
--- Позволяет динамически добавлять как одну, так и несколько обязанностей обьекту
--- предоставляет больше гибкости, по сравнению с наследованием

Минусы:
--- разрастается кодовая база проекта из-за наличия большого числа маленьких классов
--- появляются трудности с конфигурированием многократно оборачиваемых обьектов
"""

from abc import ABC, abstractmethod


class IPizzaBase(ABC):
    """Интерфейс декорируемого обьекта"""

    @abstractmethod
    def cost(self) -> float:
        pass


class PizzaBase(IPizzaBase):
    """Класс декорируемого обьекта"""

    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost



class IDecorator(IPizzaBase):
    """Интерфейс декоратора"""

    @abstractmethod
    def name(self) -> str:
        pass


class PizzaMargarita(IDecorator):
    """На основе PizzaBase получаем пиццу Маргарита"""

    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = 'Маргарита'

    def cost(self) -> float:
        return self.__cost+self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


class PizzaSalami(IDecorator):
    """На основе PizzaBase получаем пиццу Салями"""

    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = 'Салями'

    def cost(self) -> float:
        return (self.__cost + self.__wrapped.cost())*2

    def name(self) -> str:
        return self.__name

if __name__ == '__main__':
    def print_pizza(pizza: IDecorator) -> None:
        print(f'Стоимость основы пиццы = {pizza.cost()}')

    pizza_base = PizzaBase(3.4)
    print(f'Стоимость основы пиццы = {pizza_base.cost()}')
    margarita = PizzaMargarita(pizza_base, 10)
    print_pizza(margarita)
    salami = PizzaSalami(pizza_base, 7)
    print_pizza(salami)