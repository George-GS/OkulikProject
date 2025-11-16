# Создай генератор, который выдает случайные имена пользователей
# Используй модуль random и список: ["alex", "mike", "anna", "olga"]
# Должен бесконечно выдавать случайные имена из списка

import random

user_list = ["alex", "mike", "anna", "olga"]

def gen_user():
    while True:
        yield random.choice(user_list)


gen = gen_user()
print(next(gen))
print(next(gen))
print(next(gen))
