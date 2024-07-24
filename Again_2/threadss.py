# multithreading - многопоточность, подходит для IO-bound задач, использует ОС, страдает от GIL
# Полезно для ускорения выполнения задач для того, чтобы текущий поток занялся другой задачей
# Любая программа это минимум один процесс и один поток

# Полезно использовать daemon=True, очереди, pool executor, НО в любом случае все зависит от программиста!

# Плюсы:
# + просто(сравнительно)
# + быстро
# + не умирает из-за одного(!)

# Минусы:
# - потребление ресурсов
# - неуправляемость
# - проблема потоков

import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk
from queue import Queue


def waiting(timeout):
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print('OK')


def thread_wait(timeout):
    thread = Thread(target=waiting, args=(timeout,), daemon=True)
    thread.start()
    return thread


counter = [0]
queue = Queue()
queue.put(0)
# lock = threading.Lock()


# def inc():
#     lock.acquire()
#     c = counter[0]
#     time.sleep(0.1)
#     counter[0] = c + 1
#     lock.release()


def inc_queue():
    c = queue.get()
    time.sleep(0.1)
    queue.put(c+1)


def info():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f'Process {pid}, name {name}')


if __name__ == '__main__':
    # tk = Tk()
    # button1 = ttk.Button(tk, text='WAIT', command=lambda: waiting(3))
    # button1.pack(side=LEFT)
    # button2 = ttk.Button(tk, text='THREAD', command=lambda: thread_wait(3))
    # button2.pack(side=LEFT)
    # tk.mainloop()
    # threads = [Thread(target=info, daemon=True) for _ in range(10)]
    # threads = [Thread(target=lambda: waiting(5), daemon=True) for _ in range(3)]
    threads = [Thread(target=inc_queue, daemon=True) for _ in range(10)]
    for t in threads:
        t.start()
    for y in threads:
        t.join()
    # print(counter)
    print(queue.qsize())
    print(queue.get_nowait())
    # info()
