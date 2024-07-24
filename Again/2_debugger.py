# 1) Прочитать и желательно понять ошибку (!)
# 2) перейти по ссылке в место, где она падает и снова подумать
# 3) поставить брекпоинт и отлаживать

def get(value):
    if value > 0:
        return 'Positive'
    if value < 0:
        return 'Negative'
    return 'Zero'

if __name__ == '__main__':
    k = 0
    for i in range(10):
        k += i
    value = int(input())
    print(get(value).upper())
