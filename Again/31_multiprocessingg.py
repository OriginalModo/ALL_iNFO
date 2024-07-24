import time
from multiprocessing import Process, Pool
import requests

# --- Multiprocessing выдуман чтобы побороть GIL! Как его побороть сделать много GIL каждый из которых независимый ---
# --- Multiprocessing работает только с обьектами которые поддерживают сериализацию через pickle
# В других ЯП: параллельность вычислений достигается с помощью 2-х средств ПОТОКИ или asyncio. Потому что у них нет GIL
# Multiprocessing - позволяет решать любые задачи (IO-bound или CPU-bound)
# Ускорение любые задачи, распараллеливая их на ядра процессора (лишь до определенного предела, закон Амдала)
# закон Амдала - с какого-то момента бессмысленно добавлять дополнительных рабочих(ЦПУ, доп.ядра) быстрее не станет
# Ускорение не идеально и возможно только до определенного предела, смотрим закон Амдала.
# Создает несколько процессов, у каждого из которых своя память и свой GIL, каждый выполняет свою задачу, взаимодействие
# между ними требует pickle(сериализация, превращение обьектов python в байты и наоборот байтов в обьекты python)
# API принципиально похоже на многопоточность, выгодно использовать Pool, а для взаимодействия между процессами Queue и Pipe
# Pipe - когда нужно 2 процесса между собой подружить чтобы они передавали друг другу данные

# Плюсы:
# + реальная параллельность любых задач
# + не умирает из-за одного(!)
# + процессы не зависят друг от друга(у каждого процесса своя память и GIL)
# Минусы:
# - потребление ресурсов (памяти, процессора, времени)
# - необходимость сериализации в pickle
# - проблемы синхронизации (взаимодействие между процессами)

def activity():
    result = 0
    for i in range(1000_000):
        result += abs(round(i ** 2 / 122) + i * 3.14)
    print(result)
    # requests.get('https://ya.ru')
    # print('OK')

def run(parallel=False):
    start = time.time()
    if not parallel:
        for i in range(10):
            activity()
    else:
        processes = [Process(target=lambda :activity, daemon=True) for _ in range(10)]
        for i in processes:
            i.start()
        for i in processes:
            i.join()
    end = time.time()
    print(f'Time: {end - start} seconds')


def work():
    arr = list(range(1000_000))
    step = len(arr) // 10
    position = 0
    processes = []
    for _ in range(10):
        split = arr[position:position+step]
        processes.append(Process(target=calc_sum_print, args=(split,), daemon=True))
        position += step
    start = time.time()
    for i in processes:
        i.start()
    for i in processes:
        i.join()
    end = time.time()
    print(f'Time: {end - start} seconds')

def work_pool():
    arr = list(range(1000_000))
    step = len(arr) // 10
    start = time.time()
    with Pool(10) as pool:
        result = pool.map(calc_sum, [arr[position:position + step] for position in range(0, len(arr), step)])
        print(result)
    end = time.time()
    print(f'Time: {end - start} seconds')



def calc_sum(a_list: list):
    return sum(a_list)


def calc_sum_print(a_list: list):
    print(sum(a_list))

if __name__ == '__main__':
    # run(parallel=True)
    # work()
    work_pool()
