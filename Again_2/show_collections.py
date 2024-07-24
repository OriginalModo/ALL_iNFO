from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple
import csv

# OrderedDict нужен для действий со словарем где необходим порядок элементов, например
# сравнение с учетом порядка, перестановки элементов с сохранением порядка. Платим памятью!!!

# ChainMap нужен для логического обьединения словарей для поиска информации, но при изменениях меняется первый словарь

# Counter нужен для подсчета элементов в последовательности, работает только с hashable

# defaultdict нужен для создания словаря по умолчанию. Значение подставляется при обращении к несуществующему ключу

# deque потокобезопасна, быстро оперирует с обеими сторонами

# namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописными классом.
# Неизменяемый, позволяет обращаться по имени атрибута, позволяет использовать индексы.


Point = namedtuple('Point', 'x y')


# tom = ('Tom', 4, 'yellow')
Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)
print(tom.name)

# 7)
# a_deque = deque([1, 2, 3], maxlen=3)
# print(a_deque)
# a_deque.append(4)
# print(a_deque)

# 6)
# a_deaue = deque()
# a_deaue.append(1)
# # a_deaue.pop(1)
# print(a_deaue)
# a_deaue.appendleft(2)
# # a_deaue.popleft(2)
# print(a_deaue)

# 5)
# a_dict = defaultdict(list)
# for char in 'hello':
#     a_dict[char].append(char)
#
# print(a_dict)
#


# 4)
# a_dict = defaultdict(int)
# for char in 'hello':
#     a_dict[char]+=1
#
# print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))

# 3)
# counter = Counter('hello')
# print(counter)
# counter.update('world')
# print(counter.most_common(3))


# 2)
# first = {1: 1, 2: 2, 3: 3}
# second = {4: 4, 5: 5}
#
#
# chain = ChainMap(first, second)
#
# print(chain)
# chain[1] = 200
# print(chain)

# 1)
# first = {1: 1, 2: 2, 3: 3}
# second = {2: 2, 1: 1}

# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
# # print(order1==order2)
# # print(order1.popitem(last=False))
# print(order1.move_to_end(3, last=False))
# print(order1)
