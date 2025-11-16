# Задание 1: Класс для тестового пользователя
# Создай класс TestUser с атрибутами: username, email, password
# и методами: login(), logout(), change_password()


class TestUser:

    platform = "web"

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_logged_in = False

    def login(self):
        '''Имитирует вход пользователя'''
        self.is_logged_in = True
        print(f'Пользователь {self.username} вошел в систему')

    def change_password(self, new_password):
        """Имитирут смену пароля"""
        self.password = new_password
        print('Ваш пароль изменен')

    def logout(self):
        """Имитирует выход пользователя"""
        self.is_logged_in = False
        print(f'Пользователь {self.username} вышел из системы')



# Задание 1.2: Создание объектов и работа с атрибутами
# Используя созданный класс TestUser, создай 3 разных пользователя
# Покажи разницу между атрибутами объекта и вызовом методов
# Создай объекты: user1, user2, user3 с разными данными

user1 = TestUser('user1', 'email_1.com', 'pass1')
user2 = TestUser('user2', 'email_2.com', 'pass2')
user3 = TestUser('user3', 'email_3.com', 'pass3')

print(user2.email)

user3.login()
user3.change_password('new_pass3')
user3.logout()
print(user3.password)

# Задание 1.3: Демонстрация наследования
# Создай класс AdminUser который наследует TestUser
# Добавь атрибут is_admin = True
# Добавь метод delete_user()

class AdminUser(TestUser):

    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.is_admin = True

    def delete_user(self, username):
        """"Имитация удаления пользователя"""
        print(f'Пользователь {username} удален администратором {self.username}')

# Демонстрация наследования

admin_user = AdminUser('admin1', 'adm_email.com', 'adm_pass123')

print('')
admin_user.login()
print(admin_user.is_logged_in)
admin_user.logout()
print(admin_user.is_logged_in)
print(admin_user.is_admin)

admin_user.delete_user('user1')

# Задание 1.4: Работа с атрибутами класса
# Добавь в класс TestUser атрибут класса platform = "web"
# Покажи что он доступен всем объектам

#добавил
print('')
print(admin_user.platform)
print(user3.platform)

user2.platform = 'web_2'
print(user2.platform)
