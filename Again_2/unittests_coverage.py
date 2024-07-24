# написать функцию calculator, которая принимает на вход строку, содержащую два целых числа и один знак арифметический
# операции + - / * и возвращает результат этой операции. Если числа не целые или нет знака операции то
# бросать исключение ValueError

def calculator(expression):
    allowed = '+-/*'
    if not any(sing in expression for sing in allowed):
        raise ValueError(f'Выражение должно осдержать хотя бы один знак {allowed}')
    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                if sing == '+':
                    return left + right
                elif sing == '-':
                    return left - right
                elif sing == '*':
                    return left * right
                elif sing == '/':
                    return left / right

            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')


if __name__ == '__main__':
    print(calculator('10/2'))
