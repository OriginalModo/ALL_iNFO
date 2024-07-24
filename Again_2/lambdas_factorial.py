# аналог def!!
# можно писать всё что допустимо после retrun в def
# не выполняется до вызова ()!!!
# можно писать код без лямбд


from functools import reduce

print(reduce(lambda x, y: x * y, range(1, 6), 1))  # !5  ->120

fact = lambda x: x * fact(x - 1) if x > 1 else x
print(fact)
