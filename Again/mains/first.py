print(f'Start module {__name__}')

def calc(a, b):
    print('Run function calc in first')
    return a + b

if __name__ == '__main__':
    print('abracadabra')
    print(calc(2, 2))
