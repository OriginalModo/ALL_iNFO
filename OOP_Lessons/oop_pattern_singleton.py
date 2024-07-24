# Паттерны или шаблоны разработки - это общие способы решения частых задач и проблем
# Singleton Одиночка - это шаблон предоставления глобального доступа к состоянию, обьект всегда один
# Monostate - это шаблон предоставления глобального доступа к состоянию, обьекты могут быть разными
# нужен для одной точки доступа к ресурсам/данным и для того чтобы ресурсоемкие задачи сделать 1 раз
# плюсы: 1 раз выполняем тяжелые задачи, имеет 1 вход для всей системы
# минусы: общесистемная глобальная переменная
# модуль в python - это синглтон

class Singleton:
    instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #     return cls.instance


    def __new__(cls, *args, **kwargs):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do some hard work')
        # parse, db, work with data/resources etc...
        self.data = 101


class Monostate:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('do some hard work')
            # parse, db, work with data/resources etc...
            self.data = 101


if __name__ == '__main__':
    first = Singleton()
    # first._do_work()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 102
    print(second.data)
    print(Singleton())


# if __name__ == '__main__':
#     first = Monostate()
#     # first._do_work()
#     print(first)
#     second = Monostate()
#     print(second)
#     print(first is second)
#     print(first.data)
#     first.data = 102
#     print(second.data)
#     print(Monostate())

# class Singleton:
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
# class Monostate:
#
#     _shared_attrs = {}
#
#     def __init__(self):
#         self.__dict__ = self._shared_attrs

