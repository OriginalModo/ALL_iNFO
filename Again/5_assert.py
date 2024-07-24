# Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если содержит только цифры, только строчные, только заглавные то вернуть Weak
# - если содержит символы любых 2 наборов вернуть Good
# - если содержит символы любых 3 наборов вернуть Very Good
import string


def password_strength(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    if len(value) < 8:
        return 'Too Weak'
    if all(i in digits for i in value) or all(i in lowers for i in value) or all(i in uppers for i in value):
        return 'Weak'
    if any(i in digits for i in value) and any(i in lowers for i in value) and any(i in uppers for i in value):
        return 'Very Good'
    if (any(i in digits for i in value) and any(i in lowers for i in value)) or (
            any(i in digits for i in value) and any(i in uppers for i in value)) or (
            any(i in lowers for i in value) and any(i in uppers for i in value)):
        return 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('asdfghj') == 'Too Weak'
    assert password_strength('ASDFGHJ') == 'Too Weak'
    assert password_strength('ASdfg1') == 'Too Weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('12345678990') == 'Weak'
    assert password_strength('asdfghjk') == 'Weak'
    assert password_strength('asdfghjkass') == 'Weak'
    assert password_strength('ASDFGHJK') == 'Weak'
    assert password_strength('ASDFGHJKSDD') == 'Weak'
    assert password_strength('1234asdf') == 'Good'
    assert password_strength('1234asdaf') == 'Good'
    assert password_strength('1234ASDF') == 'Good'
    assert password_strength('1234ASDAF') == 'Good'
    assert password_strength('asdfaaASDF') == 'Good'
    assert password_strength('123QWEqwe') == 'Very Good'
    assert password_strength('1234567Ee') == 'Very Good'
    assert password_strength('qqqqqQQ1') == 'Very Good'
    assert password_strength('QQQQQQ1a') == 'Very Good'
