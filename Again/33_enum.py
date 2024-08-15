# Enum(перечисления) -  это класс, который содержит константы и методы для работы с ними

# Enum нужен там, где количество значений ограничено, если у вас есть 2+ констант, связанных по смыслу - это возможно
#  хороший вариант для Enum. CREATED-PROCESSED-FINISHED-CANCELED

# Enum "ограничивает" выбор пользователя, помогает пользователю понять возможные варианты, позволяет легко добавлять или удалять значения
# Позволяет легко добавлять или удалять значения

# 1) Мы не можем ограничить пользователя
# 2) Документация не всегда актуальна
# 3) Изменения в нескольких местах

from enum import Enum, auto

# auto - Заглушка
class TrafficLight(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()


def allowed_action(traffic_light: TrafficLight) -> str:
    if traffic_light == TrafficLight.RED:
        return 'stop'
    elif traffic_light == TrafficLight.GREEN:
        return 'go'
    elif traffic_light == TrafficLight.YELLOW:
        return 'wait'


# if __name__ == '__main__':
    # print(allowed_action(TrafficLight.RED))
    # print(allowed_action(TrafficLight.YELLOW))
    # print(allowed_action(TrafficLight.GREEN))


# value, name
class TrafficLight(Enum):
    RED = 'stop'
    GREEN = 'go'
    YELLOW = 'wait'


def allowed_action(traffic_light: TrafficLight) -> str:
    return traffic_light.value


if __name__ == '__main__':
    print(allowed_action(TrafficLight.RED))      # -> stop
    print(allowed_action(TrafficLight.YELLOW))   # -> wait
    print(allowed_action(TrafficLight.GREEN))    # -> go


















