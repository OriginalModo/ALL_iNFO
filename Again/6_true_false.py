# True, False

#    and ломается на ЛЖИ
# Как только and встретить ложь проверки дальше не выполняются
# and проверяет все условия

#    or ломается на правде
# Как только or встретить правда проверки дальше не выполняются
# and проверяет все условия

# Примеры
# def check(x) -> bool:
#     print(f'{x}>0 is {bool(x > 0)}')
#     return x > 0
#
# if check(-1) or check(5) or check(-2) or check(-3):
#     print('YES')
# if check(-1) and check(5) and check(-2) and check(-3):
#     print('YES')

# def is_even(x) -> bool:
#     return x % 2 == 0

falsy = [None, False, 0, 0.0, [], {}, set(), tuple(), range(0), '']

def check(x) -> bool:
    print(f'{x}>0 is {bool(x > 0)}')
    return x > 0

