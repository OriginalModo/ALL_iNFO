# __package__ = 'imports_lessons'
from .utils import multi

def calc(a, b):
    multi('=', 10)
    print(f'a+b{a+b}')

if __name__ == '__main__':
    calc(2, 3)