# def typed_int(function):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise ValueError('Тип должен быть int')
#         return function(*args)
#
#     return wrapper
#
# def typed_str(function):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg, str):
#                 raise ValueError('Тип должен быть str')
#         return function(*args)
#
#     return wrapper
#

def typed(type_):
    def real_decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип должен быть {type_}')
            return function(*args)
        return wrapper
    return real_decorator

@typed(int) #@real_decorator
def calculate(a, b, c):
    # Logic
    return a + b + c

@typed(str)
def convert(a, b):
    # Logic
    return a + b


if __name__ == '__main__':
    # calculate = typed_int(calculate)
    # calculate = typed(int)(calculate)
    print(calculate(1, 3, 3))
    print(convert('None', 'hello'))
    # convert = typed(str)(convert)
