from time import time, sleep


def print_n_times(value: str, n: int = 10):
    for _ in range(n):
        print(value)

def some_function():
    print('some_function called')
    return 1

def calc(time_=None):
    if time_ is None:
        time_ = []
    time_.append(1)
    return time_


if __name__ == '__main__':
    print(calc())
    print(calc())
    print(calc([]))
    print(calc([]))

