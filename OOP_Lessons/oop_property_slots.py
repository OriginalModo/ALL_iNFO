# Используем сег/гет а также проперти ТОЛЬКО при наличии логики в получении или установке атрибута

# Возможность установки/получения атрибутов с логикой
# Зарпетить менять атрибут или добавлять новые атрибуты
# __dict__ - это атрибут обьектов в питоне, который хранит состояние
# __setattr__ вызывается при попытке установить атрибут
# __slots__ - создан для уменьшения памяти, занимаемой обьектами

from pympler import asizeof


class Cat:
    __slots__ = ('_name', '_age')
    # FIELDS = ('name', 'age')

    def __init__(self, name, age):
        if not name:
            raise AttributeError('Name cant be empty!')
        if age < 1 or age > 15:
            raise AttributeError('Age should be in 1-15')
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError('Name cant be empty')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 1 or  value > 15:
            raise AttributeError('Age should be in 1-15')
        self._age = value

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'

    # def __getitem__(self, item):
    #     return self.age[item]

    # def __setattr__(self, key, value):
    #     # print(key)
    #     if key not in self.FIELDS:
    #         raise AttributeError(f'Only allowed {self.FIELDS}')
    #     if key == 'name' and not value:
    #         raise AttributeError('Name cant be empty!')
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError('Age should be in 1-15')
    #     self.__dict__[key] = value


if __name__ == '__main__':
    tom = Cat('Tom', 10)
    print(tom)
    print(asizeof.asizeof(tom))



# Пример работы __dict__
# class Empty:
#     pass
#
#
# if __name__ == '__main__':
#     empty = Empty()
#     empty.abra = 'cadabra'
#     print(empty.__dict__['abra'])
