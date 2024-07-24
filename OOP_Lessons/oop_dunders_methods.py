# Магические методы - dunder методы, методы которые начинаются и заканчиваются __
# init по умолчанию не ждет аргументов
# repr - для програмистов, возвращает строку, по которой видно (и можно воссоздать) состояние обьекта
# str - для людей, возвращает строку
# если не реализован репр и стр, то будет возвращать адрес в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип
# если методы сравнения не реализованы то падает ошибка
# contains для реализации проверки IN
# bool для самодеельных обьектов всегда вернет True, для изменения поведения нужно написать __bool__
# len вернет ошибку если не переопределить метод __len__
# чтобы обьект стал вызываемым (callable) нужно реализовать __call__, иначе ошибка
# __iter__ возвращает обьект итератор, тот кто реализует итер = Итерабл
# __next__ должен вернуть следующий обьект из контейнера, кто его реализует = Итератор, for работает до StorIteration
# __getitem__ нужен для функционала [] (аналог списка и словаря)
# __setitem__ для присовоения через [], если не реализовать = ошибка
# если в обьекте не реализован __iter__ то для цикла фор будет использован __getitem__ там ожидается падение IndexError




class Banknote:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'

    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


class Iterator:

    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        # while 0 <= self.index < len(self.container):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __str__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0
        # return bool(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        return f'{sum(i.value for i in self.container)} рублей'

    # def __iter__(self):
    #     return self

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item: int):
        print('!!!')
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key, value):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == '__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred)
    wallet[0] = Banknote(500)
    for money in wallet:
        print(money)

    # print(wallet[1])
    # for money in wallet:
    #     print(money)

    # print(wallet())
    # print(len(wallet))
    # print(Banknote(500) in wallet)
    # if wallet:
    #     print('!')

    # banknote = Banknote(50)
    # fifty = Banknote(50)
    # hundred = Banknote(100)
    # # other = eval(repr(banknote))
    # # print(f'{banknote!r}') # __repr__
    # # print(banknote) # __str__
    # print(banknote >= hundred)
