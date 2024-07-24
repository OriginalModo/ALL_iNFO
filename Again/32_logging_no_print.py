# Логирование - фиксация состояния вашей системы(приложения) в какой-то момент времени
# Логирование решает основную функцию - диагностирование проблемы
# - В каком состоянии находится система
# - В каком состоянии находятся данные
# - Что у вас происходит в системе
# Нужно для того чтобы понимать:
# 1) Понимать что всё работает правильно
# 2) Понимать что всё вообще работатет
# 3) Для диагностики проблемы
#
# В самом простом логировании мы используем - функцию print()
# print() - нормальный способ логирования для простых программ (пара функций, 1 класс
# Чем сложнее/больше ваше приложение - тем сильнее растет необходимость использования специальных инструментов для логирования
# Логирования много не бывает :) легче диагностировать проблему когда информации много
#
#
#
#
#
import json
import logging.config
from logging import getLogger, basicConfig, DEBUG, ERROR, INFO, FileHandler, StreamHandler


with open('logging.conf') as file:
    config = json.load(file)


logging.config.dictConfig(config)
logger = getLogger()  # самый главный логер
# FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
# file_handler = FileHandler("data.log")
# file_handler.setLevel(DEBUG)
# console = StreamHandler()
# console.setLevel(INFO)
# basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])

def calculate(exp: str):
    logger.debug("Get expression %s", exp)
    try:
        result = eval(exp)
        logger.debug("Evaluated %s", result)
        return result
    except Exception as e:
        logger.error("Exception %s", e)
        return None


def start():
    while True:
        expression = input('Введите выражения для вычистения: ')
        logger.debug("Exception is %s", expression)
        if not expression:
            logger.info('empty expression, stopping...')
            break
        result = calculate(expression)
        if result is None:
            logger.info('No result back, stopping...')
            break
        print(f"Result is {result}")


if __name__ == '__main__':
    logger.info('start service')
    start()
    logger.info('stop service')

