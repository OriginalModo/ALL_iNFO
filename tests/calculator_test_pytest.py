import pytest

from Again_2.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_no_signs():
    with pytest.raises(ValueError) as e:
        calculator('abracadabra')
    assert 'Выражение должно осдержать хотя бы один знак +-/*' == e.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as e:
        calculator('2+2+2')
    assert 'Выражение должно содержать 2 целых числа и 1 знак' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
