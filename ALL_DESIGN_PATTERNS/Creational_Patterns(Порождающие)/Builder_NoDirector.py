"""
Строитель (Builder):

Суть: Используется для пошагового создания сложных обьектов


В каких случаях рекомендуется использовать:
1) Процесс(алгоритм) создание сложного обьекта не должен зависеть от того, из каких частей он состоит и как
эти части стыкуются между собой
2) Процесс создания (конструирования) обьекта должен обеспечивать его различные представления

Плюсы:
--- позволяет создавать продукты пошагово
--- избавляет клиентский код от привязки к конкретным классам продуктов и упрощает добавление новых
--- инкапсулирует сложный код сборки продукта от его основной бизнес-логики

Минусы:
--- Усложнение кода программы, так как добавляются  дополнительные классы
--- Привязка клиентского кода к конкретным классам строителей
"""

# from .Builder import (PizzaSauceType,
#                       PizzaBase,
#                       PizzaDoughDepth,
#                       PizzaDoughType,
#                       PizzaTopLevelType,
#                       )
from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple


PizzaBase = namedtuple('PizzaBase', ['DoughDepth', 'DoughType'])


class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


class PizzaSauceType(Enum):
    PESTO = auto()
    WHITE_GARLIC = auto()
    BARBEQUE = auto()
    TOMATO = auto()


class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()


"""
Класс компонуемого продукта
"""


class Pizza:
    def __init__(self, builder):
        self.name = builder.name
        self.dough = builder.dough
        self.sauce = builder.sauce
        self.topping = builder.topping
        self.cooking_time = builder.cooking_time  # in minute

    def __str__(self):
        info: str = f'Pizza name: {self.name} \n' \
                    f'dough type: {self.dough.DoughDepth.name} & ' \
                    f'{self.dough.DoughDepth.name} \n' \
                    f'sauce type: {self.sauce} \n' \
                    f'topping: {[it.name for it in self.topping]} \n' \
                    f'cooking time: {self.cooking_time} minutes '
        return info


    @staticmethod
    def getBuilder():
        return _Builder()


"""
Абстрактный класс, задающий интерфейс строителя
"""


class _Builder:

    def set_name(self, name: str):
        self.name = name

    def set_dough(self, pizza_base: PizzaBase):
        self.dough = pizza_base

    def set_sauce(self, sauce: PizzaSauceType):
        self.sauce = sauce

    def set_topping(self, topping: list):
        self.topping = topping

    def set_cooking_time(self, time: int):
        self.cooking_time = time

    def build(self):
        return Pizza(self)


if __name__ == '__main__':
    # Готовим пиццу маргарита
    pizza_base = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)
    builder = Pizza.getBuilder()
    builder.set_name('Margarita')
    builder.set_dough(pizza_base)
    builder.set_sauce(PizzaSauceType.TOMATO)
    builder.set_topping(
        [
            i for i in (PizzaTopLevelType.MOZZARELLA,
                        PizzaTopLevelType.MOZZARELLA,
                        PizzaTopLevelType.BACON
                        )
        ]
    )
    builder.set_cooking_time(10)
    pizza = builder.build()
    print(pizza)
