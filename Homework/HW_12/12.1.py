# Задание 1: Класс с инкапсуляцией
# Создай класс TestUser с приватными атрибутами __password, __email
# Добавь свойства (property) для безопасного доступа
# Добавь сеттер с валидацией для email

import json

class TestUser:

    def __init__(self, username, email, password):
        sself.username = username
        self.__email = email
        self.__password = password



    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            self.__email = new_email
        else:
            print("Warning: Invalid email format")


user1 = TestUser('pas123', 'em123@pam.ru')
print(user1.email)
print(user1.password)
user1.email = 'em555@dfs.com'
print(user1.email)
user1.email = 'edddasdas'
print(user1.email)

#