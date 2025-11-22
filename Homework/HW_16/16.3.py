# ЗАДАНИЕ: Генератор тестовых данных для автотестов
# Задача:
# 1. Создай .env файл с настройками:
#    - USERS_COUNT=5
#    - LOCALE=ru_RU
#    - OUTPUT_FORMAT=console
#
# 2. Напиши код который:
#    - Читает настройки из .env
#    - Генерирует указанное количество тестовых пользователей
#    - Каждый пользователь: имя, email, телефон, город
#    - Выводит результат в консоль в удобном формате
#
# Пример вывода:
# === ТЕСТОВЫЕ ПОЛЬЗОВАТЕЛИ (5) ===
# 1. Иван Петров - ivan@mail.ru - +7-123-456-7890 - Москва
# 2. Мария Сидорова - maria@yandex.ru - +7-987-654-3210 - СПб

from faker import Faker
import os
import dotenv

dotenv.load_dotenv()
fake = Faker(os.getenv('LOCALE'))

def gen_user(num):
    print(f'=== ТЕСТОВЫЕ ПОЛЬЗОВАТЕЛИ ({num} шт.) ===')
    count = 1
    for i in range(num):
        print(f'{count}. {fake.name()} - {fake.email()} - {fake.phone_number()} - {fake.city_name()}')
        count += 1

gen_user(int(os.getenv('USERS_COUNT')))


