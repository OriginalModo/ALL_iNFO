if __name__ == '__main__':
    first = {1: 1, 2: 2}
    second = {3: 3, 4: 4}
    third = {5: 5, 4: 100}
    first.update(second)
    # first |= second

    # print({**first, **second})
    print(first | second | third)
