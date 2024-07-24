# def typed_int(func):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise ValueError('Need int')
#         return func(*args)
#
#     return wrapper
#
# def typed_str(func):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg, str):
#                 raise ValueError('Need str')
#         return func(*args)
#
#     return wrapper


def typed(type_):
    def real_decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Need INT{type_}')
            return func(*args)
        return wrapper
    return real_decorator




@typed(int) # @real_decorator
def calculate(a, b, c):
    return a + b + c

@typed(str)
def convert(a, b):
    return a + b


if __name__ == '__main__':
    # print(typed_int(calculate)(1, 2, 3))
    # calculate = typed_int(calculate)
    # print(calculate(1,2,3))
    # print(typed(int)(calculate)(1, 2, 3))
    # calculate = typed()(calculate)(1,2,3)
    # print(calculate)
    print(calculate(1, 2, 3))
    print(convert('1', 'hello'))
