"""
Компоновщик (Composite):

Суть: для компановки обьектов древовидной структуры в последствии позволяет работать с ними как с одним обьектом


В каких случаях рекомендуется использовать:
1) обьект (модель) системы может быть структурирован в виде дерева
2) в клиентском коде необходимо единообразно трактовать как составные, так и индивидуальные обьекты

Плюсы:
--- позволяет определить иерархии классов, в состав которых входит примитивные и составные обьекты
--- упрощает архитектуру клиента и облегчает добавление новых видов компонентов

Минусы:
--- создается слишком общий дизайн классов
"""

from abc import ABC, abstractmethod


class IProduct(ABC):
    """Интерфейс продуктов входящих в пиццу"""

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Product(IProduct):
    """Класс продукта"""

    def __init__(self, name: str, cost: float):
        self.__name = name
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoudProduct(IProduct):
    """Класс компонуемых продуктов"""

    def __init__(self, name: str):
        self.__name = name
        self.products = []

    def cost(self) -> float:
        cost = 0
        for i in self.products:
            cost += i.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product(self, product: IProduct):
        self.products.remove(product)

    def clear(self):
        self.products = []

class Pizza(CompoudProduct):
    """Класс пиццы"""

    def __init__(self, name: str):
        super(Pizza, self).__init__(name)

    def cost(self) -> float:
        cost = 0
        for i in self.products:
            cost_i = i.cost()
            print(f"Стоимость '{i.name()}' = {cost_i} тугриков")
            cost+= cost_i
        print(f"Стоимость пиццы '{self.name()}' = {cost} тугриков")
        return cost

if __name__ == '__main__':
    dough = CompoudProduct('тесто')
    dough.add_product(Product('мука', 3))
    dough.add_product(Product('яйцо', 2.3))
    dough.add_product(Product('соль', 1))
    dough.add_product(Product('сахар', 2.1))
    sauce = Product('Барбекю',12.)
    topping = CompoudProduct('топпинг')
    topping.add_product(Product('Дор блю', 14))
    topping.add_product(Product('Дор блю', 12.3))
    topping.add_product(Product('Дор блю', 9.54))
    topping.add_product(Product('Дор блю', 7.27))
    pizza = Pizza('4 сыра')
    pizza.add_product(dough)
    pizza.add_product(sauce)
    pizza.add_product(topping)
    print(pizza.cost())

