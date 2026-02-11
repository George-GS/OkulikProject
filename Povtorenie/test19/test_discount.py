import pytest
from func_calc import calculate_discount

@pytest.mark.smoke
def test_base_calc(sample_product):
    '''Базовая проверка калькулятора на готовых данных'''
    assert calculate_discount(sample_product['price'], sample_product['discount']) == 900

@pytest.mark.regression
def test_er1_calc():
    '''проверка цены меньше нуля'''
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        calculate_discount(-1, 50)

@pytest.mark.regression
def test_er2_calc():
    '''проверка скидки меньше нуля'''
    with pytest.raises(ValueError, match="Скидка должна быть от 0 до 100"):
        calculate_discount(100, -5)

@pytest.mark.regression
def test_er3_calc():
    '''проверка скидки меньше нуля'''
    with pytest.raises(ValueError, match="Скидка должна быть от 0 до 100"):
        calculate_discount(100, 101)

@pytest.mark.slow
@pytest.mark.parametrize('price, discount, expected', [
    (100, 90, 10),
    (5555.55, 44.5, 3083.33)
])
def test_calc_param(price, discount, expected):
    '''Регресс тест с различными параметрами'''
    assert calculate_discount(price, discount) == expected
