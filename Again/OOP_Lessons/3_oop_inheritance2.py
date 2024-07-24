# Наследование - позволяет расширять, менять поведение классов
# и получать к данным поведения своего предка доступ


class First:
    def __init__(self):
        self._login = 'login'
        self.__password = 'passwords'


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = 'My_login'
        self.__password = 'My_pass'


if __name__ == '__main__':
    first = First()
    second = Second()
    print(dir(second))
    print(second._login)
    print(second._Second__password)
    print(second._First__password)


