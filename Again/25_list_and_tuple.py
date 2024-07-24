# list = список, изменяемый упорядоченный, обычно хранит значения одного типа, O(1) доступ к элементу
# tuple = кортеж, неизменяемый упорядоченный, обычно хранит разных типов, O(1) доступ к элементу
# tuple хранит ссылки на элементы

# скорость(время) доступа к элементам одинаковая, скорость не зависит от количества элементов

# используй кортежи везде, где это возможно и обоснованно
# 1) используй [] для создание пустого списка ({} для словаря)
# 2) если заранее известен размер, то не используй append (для 8000 добавлений выделяется 8600 ячеек памяти)
# 3) используй листкомпс
# 4) не пытайся заменять список кортежом, там где идет изменение размера


from terminaltables import AsciiTable
from timeit import timeit     # библиотека замера скорости
from pympler import asizeof   # библиотека замера размера структур
import dis                    # библиотека работы с байт кодом

a_list = list(range(100))

# print(timeit('a_list[0]', 'from __main__ import a_list'))
# print(timeit('a_list[50]', 'from __main__ import a_list'))
# print(timeit('a_list[-1]', 'from __main__ import a_list'))

print(timeit('tuple()'))
print(timeit('()'))


print(timeit('dict()'))
print(timeit('{}'))


# table = AsciiTable([list(range(10))]).table
# print(table)
# print(id(table))


# new_list = []
# a_tuple = (new_list, 1, 'A')
# print(a_tuple)

# # Run only this code first
# a_tuple[0] += ['oops']


# # Run only this code second
# print(a_tuple)
# try:
#     a_tuple[0]+=['oops']
# except:
#     pass
# print(a_tuple)


# print([id(i) for i in a_tuple])
# new_list.append(1000)
# print(a_tuple)
# print([id(i) for i in a_tuple])


# dis.dis('[]')