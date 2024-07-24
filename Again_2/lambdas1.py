# аналог def!!
# можно писать всё что допустимо после retrun в def
# не выполняется до вызова ()!!!
# можно писать код без лямбд

def square(x):
    return x ** 2


# square2 = lambda x: x ** 2
# even_odd = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'

any_ = lambda: abracadabra
any2 = lambda: square(use(it))

if __name__ == '__main__':
    x = 2
    result = lambda n=x: n ** 2
    x = 3
    result2 = lambda n=x: n ** 2
    print(result())
    print(result2())
