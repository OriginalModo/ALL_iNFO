from unittest import TestCase, main
import doctest
from Again.unit_tests import divisor_new

# Плюсы:
# 1) сразу видно тест, не нужно идти в другие папки, чтобы посмотреть проверки
# 2) виден пример использования функции, что особенно актуально для сложных вариантов
# 3) мотивирует писать и поддерживать документацию к функции
# 4) интегрируется с юниттестом, что позволяет прогонять сразу все тесты проекта, и юниты и доктесты.
#
# Минусы:
# 1) свой синтаксис
# 2) не очень удобно писать сложные тесты, обрабатывать исключения и т.п.
#
# Мой совет - использовать доктест как добавку к юниттесту, то есть писать в сложных функциях примеры использования
# (и документацию, что немаловажно), а сложные кейсы решать уже средствами юниттеста.


# def load_tests(loader, tests, ignore):
#     tests.addTests(doctest.DocTestSuite(divisor_new))
#     return tests


class TestDivisor(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError) as e:
            divisor_new.divide(10, 0)


if __name__ == '__main__':
    main()
