"""
Цепочка обязанностей (Chain of Responsibility):

Суть: организовает последовательную передачу запроса по цепочке обьектов обработчиков каждый из которых проверяет
может он обработать запрос или передать его следующему обработчику цепочки.
Можно по-разному организовывать поведение:
--- Запрос может передаватся всем обработчикам и они проверяют могут ли что-то с ним сделать
--- Запрос может предназначатся только одному обработчику после которого он не передается по цепочке

В каких случаях рекомендуется использовать:
1) существует более одного обьекта обработки запроса,но заранее не известно,какие запросы будут приходить и
какие обьекты их будут обрабатывать
2) необходимо отправить запрос одному из ряда обьектов, при этом явно не указывая какому именно
3) обработчики запросов должны задваться динамически
4) обработка запроса должна производиться в строго определнной последовательности

Плюсы:
--- ослабляет связаность между обьектами системы
--- уменьшает зависимость между обьектами клиентского кода и обработчиками запросов

Минусы:
--- запрос может не обработаться: нет конкретного получателя и соответственно какой-либо гарантии на его обработку
--- усложнение кода
"""
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod
from enum import Enum
# from __future__ import annotations
from typing import List, Optional, TypeVar

T = TypeVar("T")


class EnumOrder(Enum):
    """Тип Заказа"""
    VEGAN = 1
    NOT_VEGAN = 2
    BINGE = 3
    NOT_ORDER = 3


class RequestOrder:
    """Класс запроса на обслуживание от клиента"""

    def __init__(self, description: List[str], order_type: EnumOrder):
        self.__description = description
        self.__order_type = order_type

    @property
    def order_type(self):
        return self.__order_type

    @property
    def order_list(self):
        return self.__description


class Handler(ABC):
    """Базовый класс для обработчиков запросов"""

    def __init__(self, successor: Optional[T] = None):
        self.__successor = successor

    def handle(self, request: RequestOrder) -> None:
        res = self._check_request(request.order_type)
        if not res and self.__successor:
            self.__successor.handle(request)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, successor: Optional[T]):
        self.__successor = successor

    @abstractmethod
    def _check_request(self, request_type: EnumOrder) -> bool:
        pass


class WaiterHandler(Handler):
    """Класс для обработки запроса официантом"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type in (EnumOrder.BINGE,
                                 EnumOrder.VEGAN,
                                 EnumOrder.NOT_VEGAN,
                                 )
        if check:
            print('Официант передает заказ дальше')
        else:
            print('Официант отклоняет запрос клиента')
        return not check


class KitchenHandler(Handler):
    """Класс обработки запроса кухней пицерии"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type in (EnumOrder.VEGAN,
                                 EnumOrder.NOT_VEGAN,
                                 )
        if check:
            print('Шеф-повар приступил к готовке заказа на кухне')
        else:
            print('Шеф-повар воротит нос от поступившего запроса')
        return check


class BarmanHandler(Handler):
    """Класс обработки запроса на стойке бара"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: EnumOrder) -> bool:
        check = request_type is EnumOrder.BINGE
        if check:
            print('Бармен наливает заказанный напиток клиентом')
        else:
            print('Бармен разводит руками и может только восхититься'
                  'гурманским вкусам клиента')
        return check


if __name__ == '__main__':
    # Настраиваем цепочку обработки запросов
    kitchen = KitchenHandler()
    bar = BarmanHandler(kitchen)
    waiter = WaiterHandler()
    # запрос всегда первым поступает официанту
    waiter.successor = bar


    def request_handler(request: RequestOrder):
        print(' ' * 20 + 'Обработка запроса' + '' * 20)
        print(f'Запрос от клиента: {request.order_list}')
        waiter.handle(request)


    req_list = ['Борщ', 'Макарошки по-флотски']
    request = RequestOrder(req_list, EnumOrder.NOT_VEGAN)
    request_handler(request)

    req_list = ['Кровавая Мерри', 'Коньяк', 'Виски']
    request = RequestOrder(req_list, EnumOrder.BINGE)
    request_handler(request)

    req_list = ['Мир на блюдечке!!!']
    request = RequestOrder(req_list, EnumOrder.NOT_ORDER)
    request_handler(request)
