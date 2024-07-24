# all() проверяет что все элементы коллекции при проверке вернут True
# any() проверяет что хотя бы 1 элемент вернет True
# all() для пустого списка вернет True
# filter(None, a_list) при None будет возвращать только True элементы

a_list1 = ['aaa', 'bb', 'cc','d']

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat({self.name=}, {self.age=}'

if __name__ == '__main__':
    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Bob', 5)]
    print(max(cats, key=lambda x: x.age))
    print(max(a_list1, key=len))
    # for line in iter(input, 'end'):
    #     print(line.upper())
    ints = [int(i) for i in iter(input, '')]
    print(ints)





# a_list = [0, 0, 1,0, True, 'sd']

# if any(a_list):
#     print(list(filter(None, a_list))) # при None будет возвращать только True элементы
#     print([i for i in a_list if i])

# TRY THIS
# a_list = []
# if __name__ == '__main__':
#     print(bool(a_list))
#     print(all(a_list))
#     print(any(a_list))








