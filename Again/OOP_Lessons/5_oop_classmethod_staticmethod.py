# LEGB-rule действует для атрибутов без приставок (self)
# для self атрибутов поиск идет сначала в обьекте, потом в классе, затем у предков OCP(object-class-parent)
# если через self пытаться поменять неизменяемый атрибут (строка), то будет создана локальная копия
# если менять через self изменяемый атрибут то он изменится для всех обьектов класса
# cls - это ссылка на класс (не обьект!), питон передает его под капотом
# @classmethod используется для работы с атрибутами класса и с другими методами класса
# @staticmethod не получает ссылок под капотом, это просто функция связанная  контекстом с классом
# cls = BlueCat
# если есть метод где self, cls передаются но нигде не используются это @staticmethod

# 1) LEGB - правило продолжает действовать для простых имен переменных и их поиска
# 2) для self атрибутов поиск идет сначала в объекте, потом в классе, затем у предков OCP(object-class-parent).
# То есть через селф можно достучаться как к обычным методам/атрибутам, так и к классовым, статичным
# 3) если через self пытаться поменять неизменяемый атрибут (строка) класса, то будет создана локальная копия,
# ее не увидят другие объекты класса
# 4) если менять через self изменямый атрибут класса (список), то он изменится для всех объектов класса
# 5) cls - это ссылка на класс (не объект!), питон передает его под капотом. cls = Class
# 6) @classmethod используется для работы с атрибутами класса и с другими методами класса.
# Часто используется для конструирования готовых объектов
# 7) @staticmethod не получает ссылок под капотом, это просто функция связанная контекстом с классом.
# Используется редко и часто завуалированно
# 8) если есть метод где self, cls передаются но нигде не используются это @staticmethod

class BlueCat:
    breed = 'Russian Blue'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # BlueCat.breed = 'Other'
        self.increment_count()
        self.names.append(name)

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_count(cls):
        cls.count += 1

    # конструктор (фабрика) конструирование обьектов
    # чтобы легко осздать обьект
    @classmethod
    def make_cat(cls, name):
        if name == 'Tom':
            return cls('Tom', 2)
        elif name == 'Angela':
            return cls('Angela', 2)
        return cls('Ginger', 2)

    # @staticmethod
    # def get_human_age(age):
    #     return age * 8

    def get_human_age(self, age):
        return age * 8


if __name__ == '__main__':
    tom = BlueCat.make_cat('Tom')
    angela = BlueCat.make_cat('Angela')
    tom.meow()
    angela.meow()
    print(angela.get_human_age(angela.age))
