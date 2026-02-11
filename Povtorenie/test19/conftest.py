import pytest

@pytest.fixture
def sample_product():
    '''Возвращает тестовые товар для smoke теста'''
    yield {
        'name': 'Тестовый товар 1',
        'price': 1000,
        'discount': 10
    }