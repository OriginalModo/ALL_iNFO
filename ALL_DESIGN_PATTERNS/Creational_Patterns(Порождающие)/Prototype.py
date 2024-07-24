"""
Прототип (Prototype):

Суть: Позволяет копировать обьекты не обращая внимания на детали их реализации


В каких случаях рекомендуется использовать:
1) код не должен зависить от классов копируемых обьектов
2) необходимо избежать использование иерархий классов или фабрик, а также параллельных иерархий классов продуктов
3) необходимо избежать множества производных классов, которые отличаются друг от друга только начальным значением их атрибута

Плюсы:
--- клонирование обьектов без привязки к их конкретным классам
--- ускорение создание обьектов и уменьшение повторяющегося кода при инициализации обьектов

Минусы:
--- Сложно осуществить процесс клонирования составных обьектов, имеющих ссылки на другие обьекты
"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple
from typing import List
import copy

# from .Builder import (PizzaSauceType,
#                       PizzaBase,
#                       PizzaDoughDepth,
#                       PizzaDoughType,
#                       PizzaTopLevelType,
#                       )


class IPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass



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


class Pizza(IPrototype):
    def __init__(self,
                 name,
                 dough: PizzaBase = PizzaBase(PizzaDoughDepth.THICK,
                                              PizzaDoughType.WHEAT),
                 sauce: PizzaSauceType = PizzaSauceType.TOMATO,
                 topping: List[PizzaTopLevelType] = None,
                 cooking_time: int = 10,
                 ):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.cooking_time = cooking_time  # in minute

    def __str__(self):
        info: str = f'Pizza name: {self.name} \n' \
                    f'dough type: {self.dough.DoughDepth.name} & ' \
                    f'{self.dough.DoughDepth.name} \n' \
                    f'sauce type: {self.sauce} \n' \
                    f'topping: {[it.name for it in self.topping]} \n' \
                    f'cooking time: {self.cooking_time} minutes '
        return info

    def clone(self):
        topping = self.topping.copy() if self.topping is not None else None
        return type(self)(
            self.name,
            self.dough,
            self.sauce,
            topping,
            self.cooking_time
        )


if __name__ == '__main__':
    pizza = Pizza('Margarita', topping=[PizzaTopLevelType.MOZZARELLA,
                                        PizzaTopLevelType.MOZZARELLA,
                                        PizzaTopLevelType.BACON
                                        ])
    print(pizza)
    new_pizza = pizza.clone() # клонируем обьект
    new_pizza.name = 'New Margarita'
    print('-'*50)
    print(new_pizza)
    salami_pizza = copy.deepcopy(new_pizza)
    salami_pizza.name = 'Salami'
    salami_pizza.sauce = PizzaSauceType.BARBEQUE
    salami_pizza.topping.append(PizzaTopLevelType.SALAMI)
    print('-' * 50)
    print(salami_pizza)