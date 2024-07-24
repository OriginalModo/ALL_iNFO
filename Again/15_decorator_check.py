from functools import wraps

def check_values(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        # print(args)
        for i in args:
            if type(i) != int:
                raise ValueError('I need INT')
        # print(args)
        result = func(*args)
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@check_values
def unknown_values(*args, **kwargs):
    return args

if __name__ == '__main__':
    # unknown_values = check_values(unknown_values)
    #
    # print(unknown_values(1,2,3))
    # print(check_values(unknown_values)(1,2,3))
    # print(unknown_values(1, 2, '3', 4))
    print(unknown_values(1, 2, 3, 4))
    print(unknown_values.__name__)
