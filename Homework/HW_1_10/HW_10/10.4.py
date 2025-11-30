# List Comprehension
# Задача 1: Создай список имен только активных пользователей
# Задача 2: Создай список словарей с username и status_text где status_text = "активен" если active=True, иначе "неактивен"
# Используй list comprehension

users = [
    {"username": "user1", "active": True},
    {"username": "user2", "active": False},
    {"username": "user3", "active": True},
    {"username": "user4", "active": False},
    {"username": "user5", "active": True}
]

list_active = [user['username'] for user in users if user['active'] is True]
print(list_active)

list_status =  [
    {'username' : user['username'],
    'text_status': 'активен' if user['active'] is True else 'не активен'
    }
    for user in users
]

print(list_status)