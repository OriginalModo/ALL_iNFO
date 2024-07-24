from time import time, sleep, perf_counter, perf_counter_ns
from functools import wraps


def timer(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        finish = time()
        print(f'Work Time {finish - start} sec')
        return result
        # return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@timer
def summa(a, b):
    sleep(1)
    return f'GOOD, {a + b}'


if __name__ == '__main__':
    # print(timer(summa)())
    # summa = timer(summa)
    # print(summa())
    print(summa(2, 2))
    print(summa.__name__)
