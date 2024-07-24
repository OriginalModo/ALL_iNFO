"""
Адаптер (Adapter)(Wrapper)(Обёртка):

Суть: Преобразование интерфейса одного класса в интерфейс другого


В каких случаях рекомендуется использовать:
1) Интерфейс существующего класса, не соответствует потребностям
2) Необходимо использовать уже существующие производные классы, в которых отсутствует некоторая общая функциональность,
которую нельзя реализовать путем расширения их базового класса

Плюсы:
--- позволяет отделить и скрыть от клиентского кода подробности преобразования различных интерфейсов
--- позволяет заместить некоторые операции адаптируемого класса

Минусы:
--- за счет добавляемых классов может усложниться сам код программы
"""

from abc import ABC, abstractmethod


class IOven(ABC):
    """Исходный интерфейс плиты,
    где единица измерения температуры - F"""

    @abstractmethod
    def get_temperature(self) -> float:
        pass

    @abstractmethod
    def set_temperature(self, t: float) -> None:
        pass


class ICelsiusOven(ABC):
    """Интерфейс плиты с которой будем осуществлять
    работу в рамках разрабатываемой системы,
    где единица измерения температуры - С"""

    @abstractmethod
    def get_celsius_temperature(self) -> float:
        pass

    @abstractmethod
    def set_celsius_temperature(self, t: float) -> None:
        pass

    @abstractmethod
    def get_original_temperature(self) -> float:
        pass


class OriginalOven(IOven):
    """Класс кухонной плиты, который будем адаптировать"""

    def __init__(self, t: float):
        assert t >= 32, 'Мы тут не холодильник реализуем'
        self.temperature = t

    def get_temperature(self) -> float:
        return self.temperature

    def set_temperature(self, t: float) -> None:
        assert t >= 32, 'Печь которая может морозить? Хм...' \
                        'интересненько'
        self.temperature = t

class OvenAdapter(ICelsiusOven):
    """Адаптер, позволяющий работать с плитой, где
    единица измерения температуры фаренгейта в
    градусах цельсия"""

    CALSIUS_TO_FAHRENHEIT: float = 9.0/5.0
    FAHRENHEIT_TO_CALSIUS: float = 5.0/9.0
    FAHRENHEIT_ZERO: float = 32.0

    def __init__(self, original_stove: IOven):
        self.stove = original_stove
        self.temperature = self._init_temperature()


    def get_celsius_temperature(self) -> float:
        return self.temperature

    def _init_temperature(self) -> float:
        return (OvenAdapter.FAHRENHEIT_TO_CALSIUS *
                (self.stove.get_temperature() -
                 OvenAdapter.FAHRENHEIT_ZERO))

    def get_original_temperature(self) -> float:
        return self.stove.get_temperature()

    def set_celsius_temperature(self, t: float) -> None:
        new_temperature_stove = (OvenAdapter.CALSIUS_TO_FAHRENHEIT * t +
                                 OvenAdapter.FAHRENHEIT_ZERO)
        self.stove.set_temperature(new_temperature_stove)
        self.temperature = t


if __name__ == '__main__':
    def print_temperature(stove: ICelsiusOven):
        print(f'Original temperature = {stove.get_original_temperature()}'
              f' F')
        print(f'Celsius temperature = {stove.get_celsius_temperature()}')
    fahrenheit_stove = OriginalOven(32)
    celsius_stove = OvenAdapter(fahrenheit_stove)
    print_temperature(celsius_stove)
    celsius_stove.set_celsius_temperature(180)
    print('-'*50)
    print('New temperature')
    print('-'*50)
    print_temperature(celsius_stove)
