# ХОРОШАЯ ФУНКЦИЯ:
# - имеет читаемое название, нужную информацию получает в аргументах
# - короткая/читаемая
# - возвращает результат (NO PRINT!)
# - независима (NO GLOBAL!!!), и не меняет ничего вне себя
# - умеет делать что-то одно, но умеет это хорошо и знает все для этого
# - если меняет пришедщий аргумент, то возвращает None
# - Тестируема!

import random


def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9) for _ in range(length)))


def replace_fives(a_list: list, value: str) -> list[str]:
    return [element.replace('5', value) for element in a_list]


def replace_fives_inplace(a_list: list, value: str):
    for index in range(len(a_list)):
        a_list[index] = a_list[index].replace('5', value)


def write_file(filename, data: str):
    with open(filename, 'w') as file:
        file.write(data)


# Первый вариант (лучше)
if __name__ == '__main__':
    pins = [generate_pin(8) for _ in range(5)]
    replace_fives_inplace(pins, '6')
    str_list = '\n'.join(pins)
    print(pins)
    write_file('test1.txt', str_list)

# Второй вариант
# if __name__ == '__main__':
#     pins = [generate_pin(8) for _ in range(5)]
#     pins_without_fives = replace_fives(pins, '6')
#     str_list = '\n'.join(pins_without_fives)
#     print(pins)
#     write_file('test1.txt', str_list)
