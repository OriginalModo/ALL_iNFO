# 1) Именование! Называем вещи своими именами, коллекции во множественном числе, функции -что делает
# 2) Всегда используйте f - строки, НИКОГДА не складываем строки
# 3) не делаем то, что происходит по-умолчанию (str(input))
# 4) используем листкомпс и генэксп только если есть преобразование И/ИЛИ фильтрация
# 5) предпочитаем листкомпс, генэксп  map/filter
# 6) используем while True для вечных циклов
# 7) если список не нужен, используем генэксп
# 8) не используем range(len(list)), если нужен индекс используем enumerate
# 9) используем if collection чтобы проверить что не пустая
# 10) используем встроенные функции
# 11) ловим конкретное исключение, пишем информацию в ветке except

# 11)

try:
    int('a')
except ValueError as e:
    print(e)
    print('Error')

# 10)
integers_3 = [1, 2, 3, -1]

print(all(i > 0 for i in integers_3))


# 9)
integers_2 = [1, 2, 3]
if bool(integers_2):
    pass

# 8)
integers = [1, 2, 3]
for index, element in enumerate(integers):  # (0, 1)
    print(f'{index}--{element}')

integers_1 = [1, 2, 3]
for integer in integers_1:
    print(integer)

# 7)
print(sum(i for i in range(10) if i % 2 == 0))
print(''.join(str(i) for i in range(10) if i % 2 == 0))

# 6)
while True:
    break

# 5)
integers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
integers2 = (i ** 2 for i in range(10) if i % 2 == 0)
print(integers, integers2, sep='\n')

# 4)
# integers = [i for i in range(10)]
integers = list(range(10))
print(integers)

# 3)
a_dict = {1: 1, 2: 2}
value = a_dict.get(3)
print(value, a_dict)

# 3)
# value = input()
print(value)
print(type(value))

# 2)
first = 'Hello'
second = 'World'

print(f'{first} {second}')

# 1)
value = 1
test = 'text'
integers = [1, 2, 3, 4, 5]
student = ['Петя', 'Иванов', 22]


def get_positives(integers: list) -> list:
    return [i for i in integers if i > 0]
