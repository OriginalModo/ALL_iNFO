# Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если содержит только цифры, только строчные, только заглавные то вернуть Weak
# - если содержит символы любых 2 наборов вернуть Good
# - если содержит символы любых 3 наборов вернуть Very Good
import string


def check_password(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(value) < 8:
        return 'Too Weak'

    if all(i in digits for i in value) or all(i in lowers for i in value) or all(i in uppers for i in value):
        return 'Weak'
    if any(i in digits for i in value) or any(i in lowers for i in value) or any(i in uppers for i in value):
        return 'Very Good'
    if (any(i in digits for i in value) and any(i in lowers for i in value)) or (
            any(i in digits for i in value) and any(i in uppers for i in value)) or (
            any(i in lowers for i in value) and any(i in uppers for i in value)):
        return 'Good'


if __name__ == '__main__':
    assert check_password('') == 'Too Weak'
    assert check_password('1234567') == 'Too Weak'
    assert check_password('qweerra') == 'Too Weak'
    assert check_password('QWEERRA') == 'Too Weak'
    assert check_password('QAaa1') == 'Too Weak'
    assert check_password('12345678') == 'Weak'
    assert check_password('12345678990') == 'Weak'
    assert check_password('qweerrad') == 'Weak'
    assert check_password('QWEERRAD') == 'Weak'
    assert check_password('QWEERRADDRF') == 'Weak'
    # assert check_password('1234qazw') == 'Good'
    # assert check_password('1234QARD') == 'Good'
    # assert check_password('1234qards') == 'Good'
    # assert check_password('QARDqard') == 'Good'
    assert check_password('221QARDqard') == 'Very Good'
    assert check_password('221QARDqard') == 'Very Good'
    assert check_password('221QARDqardAa') == 'Very Good'
    assert check_password('221QARDqard') == 'Very Good'
