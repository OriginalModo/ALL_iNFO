# Используем сег/гет а также проперти ТОЛЬКО при наличии логики в получении или установке атрибута

# Возможность установки/получения атрибутов с логикой
# Зарпетить менять атрибут или добавлять новые атрибуты
# __dict__ - это атрибут обьектов в питоне, который хранит состояние
# __setattr__ вызывается при попытке установить атрибут
# @property - это удобный механизм создания геттеров и сеттеров
# __slots__ - создан для уменьшения памяти, занимаемой обьектами,
# но как побочное свойство -не даст добавить объекту новый атрибут
# в __init__ нужно вызывать setter
# как можно сделать чтобы нельзя было поменять атрибут?
# можно сделать при помощи @property или переопределение __setattr__ просто прописывает условия

from pympler import asizeof


class Cat:
    # FIELDS = ('name', 'age')
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'

    # def __setattr__(self, key, value):
    #     if key not in self.FIELDS:
    #         raise AttributeError(f'Only allowed {self.FIELDS}')
    #     if key == 'name' and not value:
    #         raise AttributeError('Name cant be empty')
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError('Age should be in 1-15')
    #     self.__dict__[key] = value

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
        if value < 1 or value > 15:
            raise AttributeError('Age should be in 1-15')
        self._age = value


class Empty:
    pass


if __name__ == '__main__':
    tom = Cat('Tom', 10)
    emptye = Empty()
    print(tom)
    print(asizeof.asizeof(tom))
