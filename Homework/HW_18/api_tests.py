# чтоб скачать pip3 install requests

import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

# ЗАДАНИЕ 1: Тест получения пользователей
def test_get_users():
    """
    - Сделай GET запрос к /users
    - Проверь что статус код 200
    - Проверь что в ответе 10 пользователей
    - Проверь что у каждого пользователя есть поля: id, name, email
    """
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200, 'Статус код не 200'
    assert len(response.json()) == 10, 'Количество пользователей не 10'
    for item in response.json():
        assert 'id' in item, 'Нет поля id'
        assert 'name' in item, 'Нет поля name'
        assert 'email' in item, 'Нет поля email'

    print(response.json())

# test_get_users()

# ЗАДАНИЕ 2: Тест создания поста
def test_create_post():
    """
    - Создай POST запрос к /posts
    - Тело запроса: title, body, userId
    - Проверь статус код 201
    - Проверь что в ответе есть id
    - Проверь что title совпадает с отправленным
    """

    body = {
        "title": "Gsgsgsgsgsgsgsggsg0709",
        "body": "Gsgsgsgsgsgsgsggsg0709",
        "userId": 1

    }
    headers = {'Content-Type': 'application/json'}

    respons = requests.post(f'{BASE_URL}/posts', json=body, headers=headers)

    assert respons.status_code == 201, 'Статус код не 201'
    assert 'id' in respons.json(), 'Нет поля id'
    assert respons.json()['title'] == 'Gsgsgsgsgsgsgsggsg0709'

    print(respons.json())


test_create_post()

# ЗАДАНИЕ 3: Тест обновления поста
def test_update_post():
    """
    - Сначала создай пост (POST /posts)
    - Затем обнови его (PUT /posts/{id})
    - Проверь что данные обновились
    """
    pass

# ЗАДАНИЕ 4: Тест удаления
def test_delete_post():
    """
    - Создай пост
    - Удали его (DELETE /posts/{id})
    - Проверь статус код 200
    """
    pass

# ЗАДАНИЕ 5*: Тест с query параметрами
def test_posts_filter():
    """
    - Сделай GET /posts?userId=1
    - Проверь что все посты принадлежат пользователю с userId=1
    """
    pass