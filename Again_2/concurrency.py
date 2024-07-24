# Конкурентность (concurrency) - запуск на выполнение сразу нескольких задач
# (не обязательно в 1 момент времени выполняется несколько). Зависит от ПО

# Параллельность (parallel) - конкурентность, когда 2+ задачи выполняются одновременно. Зависит от железа


# thread-safe - потокобезопасность, означает что при работе с обьектом не возникают известные проблемы
# при работе с конкурентностью

# GIL (Global Interpreter Lock) - глобальная блокировка интерпретатора

# Задачи могут быть:
# CPU-bound - зависит от мощности процессора # расчеты внутри python
# IO-bound - зависит от системы ввода/вывода # обращение к файлу, обращение к сайту # GIL не трогает


# threading - IO-bound задачи # GIL не помешает
# asyncio - IO-bound задачи
# multiprocessing - любые задачи

import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

def activity():
    # for i in range(100_000):
    #     abs(round(i ** 2 / 122) + i * 3.14)
    requests.get('https://yandex.ru')
    print('OK')


def run(threaded=False):
    start = time.time()
    if not threaded:
        for i in range(10):
            activity()
    else:
        executor = ThreadPoolExecutor()
        for _ in range(10):
            executor.submit(activity)
        # threads = [threading.Thread(target=activity, daemon=True) for _ in range(10)]
        # for i in threads:
        #     i.start()
        # for i in threads:
        #     i.join()
        executor.shutdown(wait=True)
    end = time.time()
    print(f'Time: {end - start} seconds')


if __name__ == '__main__':
    run(threaded=True)
