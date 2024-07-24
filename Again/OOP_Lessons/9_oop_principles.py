# DRY - don't repeat yourself - не повторяйся
# YAGNI - You aren't gonna need it - это не понадобится
# KISS - Keep it simple, stupid - будь проще
# POLA - Principle Of Least Astonishment - не удивляй пользователя
# EAFP - Easier to Ask for Forgiveness than Permission - проще извиниться, чем просить разрешения (сначала действуй) # PythonWAY
# LBYL - Look Before You Leap - смотри, прежде чем прыгнуть (сначала спроси)
from pathlib import Path


def func():
    # some code
    try:
        return read_from_file_eafp('test.txt')
    except FileNotFoundError:
        print('')



def two():
    # some code
    return read_from_file_lbyl('test2.txt')


def read_from_file_eafp(name):
    try:
        with open(f'folder/{name}') as file:
            result = file.readlines()
        return result
    except:
        print('Sorry')


def read_from_file_lbyl(name):
    if Path(f'folder/{name}').exists():
        with open(f'folder/{name}') as file:
            result = file.readlines()
        return result
    else:
        print('Sorry')


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says: Meow!')
