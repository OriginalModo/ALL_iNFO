# Обьект - сущность, обьединяющая данные и методы для работы с ними (состояние и поведение)
# Чертеж-класс, обьект это дом
# Класс - это новый тип данных, обьект - его конкретный представитель
# у любого обьекта есть id (адресс в памяти), значение и тип
# первая потребность для классов - когда не хватает встроенных типов, вторая - разное состояние
# метод - это функция которая принадлежит классу
# self - ссылка на экземпляр класса
# dunder(double under) дандер(двойное нижнее подчеркивание), магический метод

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        # print(self)
        print(f'{self.name} says: Meow!')

    def __add__(self, other):  # +
        if isinstance(other, Cat):
            return Cat('Ginger', 0)


# from cat import Cat, meow

if __name__ == '__main__':
    # tom = Cat('Tom', 2)
    # print(tom)
    # print(tom.name)
    # meow()

    # cats = [('Tom', 2), ('Angela', 1)]
    # tom = cats[0]
    # print(tom)
    # print(tom[0])

    tom = Cat('Tom', 2)
    angela = Cat('Angela', 1)
    print(tom)
    print(angela)
    tom.meow()
    angela.meow()
    print(tom.name)
    print(tom.age)
    Cat.meow(tom)  # !!!

    ginger = tom + angela
    ginger.meow()
