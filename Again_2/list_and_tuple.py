# list = список, изменяемый упорядоченный, обычно хранит значения одного типа, O(1) доступ к элементу
# tuple = кортеж, неизменяемый упорядоченный, обычно хранит разных типов, O(1) доступ к элементу
# tuple хранит ссылки на элементы

# скорость(время) доступа к элементам одинаковая, скорость не зависит от количества элементов

# используй кортежи везде, где это возможно и обоснованно
# 1) используй [] для создание пустого списка ({} для словаря)
# 2) если заранее известен размер, то не используй append (для 8000 добавлений выделяется 8600 ячеек памяти)
# 3) используй листкомпс
# 4) не пытайся заменять список кортежом, там где идет изменение размера


from timeit import timeit
from terminaltables import AsciiTable
from pympler import asizeof
import dis

# a_list = list(range(100_000))
# a_list = tuple(range(100_000))

a_list = list(range(100))
b_list = list(range(100_000))
x = timeit('a_list.append(100)', 'from __main__ import a_list', number=1)
y = timeit('b_list.append(100)', 'from __main__ import b_list', number=1)

print(f'{x:.6f}')
print(f'{y:.6f}')


# print(timeit('a_list[0]', 'from __main__ import a_list'))
# print(timeit('a_list[50]', 'from __main__ import a_list'))
# print(timeit('a_list[-1]', 'from __main__ import a_list'))


# print(timeit('list()'))
# print(timeit('[]'))

# print(timeit('list()'))
# print(timeit('tuple()'))
# print(asizeof.asizeof(list()))
# print(asizeof.asizeof(tuple()))


# table = AsciiTable([list(range(10))]).table
# print(table)
# print(id(table))

# new_list = []
# a_tuple = (new_list, 1, 'A')
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

# dis.dis('list()')
# dis.dis('[]')

