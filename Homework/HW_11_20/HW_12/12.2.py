# Создай класс UserFromFile
# Конструктор принимает filename (название файла)
# Файл содержит ТОЛЬКО словарь с логином и паролем:
# {
#     "username": "test_user",
#     "password": "test123"
# }
# Класс создает объект с атрибутами username и password из файла
# Используй json для чтения файла


import json

class UserFromFile:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__username = self.__data['username']
        self.__password = self.__data['password']

    @property
    def data(self):
        return self.__data

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    def __read_file(self):
        file_data = open(self.__filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

user1 = UserFromFile('users.txt')
print(user1.password)