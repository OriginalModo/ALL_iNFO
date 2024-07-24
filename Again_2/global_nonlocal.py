# global и nonlocal нужны только для изменения значений
# global может создать переменную, nonlocal не может!
# nonlocal ищет только во внешнмх скоупах, но не в глобальном

counter = 100


def increment():

    def inner1():
        def inner():
            nonlocal counter
            counter = 1
            print(counter)

        return inner()

    return inner1()


if __name__ == '__main__':
    increment()
