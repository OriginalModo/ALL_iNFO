# LEGB-rule действует для атрибутов без приставок (self)
# для self атрибутов поиск идет сначала в обьекте, потом в классе, затем у предков OCP(object-class-parent)
# если через self пытаться поменять неизменяемый атрибут (строка), то будет создана локальная копия
# если менять через self изменяемый атрибут то он изменится для всех обьектов класса
# cls - это ссылка на класс (не обьект!), питон передает его под капотом
# @classmethod используется для работы с атрибутами класса и с другими методами класса
# @staticmethod не получает ссылок под капотом, это просто функция связанная  контекстом с классом
# cls = BlueCat

class BlueCat:
    breed = 'Russian Blue'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # BlueCat.breed = 'Other'
        # self.increment_count()
        BlueCat.increment_count()
        self.names.append(name)

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        # print(cls)
        if name == 'Tom':
            return cls('Tom', 2)
        elif name == 'Angela':
            return cls('Angela', 1)
        return cls('Ginger', 1)


    @staticmethod
    def get_human_age(age):
        return age * 8


if __name__ == '__main__':
    tom = BlueCat.make_cat('Tom')
    angela = BlueCat.make_cat('Tom')
    tom.meow()
    angela.meow()
    print(BlueCat.get_human_age(angela.age))


    # # tom = BlueCat('Tom', 2)
    # tom = BlueCat.make_cat('Tom')
    # angela = BlueCat('Angela', 1)
    # tom.meow()
    # angela.meow()
    # print(BlueCat.count)


    # tom = BlueCat('Tom', 2)
    # angela = BlueCat('Angela', 1)
    # tom.breed = 'Other'
    # tom.meow()
    # tom.names.append('Ginger')
    # angela.meow()
    # print(tom.names)
    # print(angela.names)
    # print(tom.count)
