from typing import List

def calc(a: int | float, b: int | float) -> int | float:
    return a + b

def to_int(a_list: list[str]) -> list[int]:
    return [int(i) for i in a_list]


if __name__ == '__main__':
    print(calc(1.2, 3.3))
