from calculator import Calculator
import pytest

# Напиши тесты ниже используя pytest
# Задачи:
# Протестируй все методы калькулятора
# Добавь тест для проверки деления на ноль (используй pytest.raises)
# Создай фикстуру которая возвращает экземпляр калькулятора

# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             raise ValueError("Cannot divide by zero")
#         return a / b

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.regres
@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (-1, 1, 0),
    (-2.5, 5.5, 3)
])
def test_sum(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.regres
@pytest.mark.parametrize('a, b, expected', [
    (3, 2, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (-1, 1, -2),
    (-2.5, 5.5, -8)
])
def test_minus(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.regres
@pytest.mark.parametrize('a, b, expected', [
    (3, 2, 6),
    (0, 0, 0),
    (-1, -1, 1),
    (-1, 1, -1)
])
def test_umnoz(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.regres
@pytest.mark.parametrize('a, b, expected', [
    (2, 2, 1),
    (3, 2, 1.5),
    (2, -1, -2),
    (0, 5, 0)
])
def test_delenie(calc, a, b, expected):
    assert calc.divide(a, b) == expected

@pytest.mark.smoke
@pytest.mark.parametrize('a, b', [
    (2, 0),
    (5, 0),
])
def test_del_na_zero(calc, a, b):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(a, b)

