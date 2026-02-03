# Часть 2: Обработка данных пользователей
# python
# # Дан список словарей с пользователями:
users = [
    {"id": 1, "name": "Анна", "age": 25, "active": True, "score": 85},
    {"id": 2, "name": "Иван", "age": 17, "active": False, "score": 42},
    {"id": 3, "name": "Мария", "age": 30, "active": True, "score": 93},
    {"id": 4, "name": "Петр", "age": 22, "active": True, "score": 67},
    {"id": 5, "name": "Ольга", "age": 16, "active": False, "score": 51}
]

# Задания (создай функции для каждой задачи):
# 1. get_active_users(users) - возвращает список имён активных пользователей
# 2. get_average_score(users) - возвращает средний балл всех пользователей
# 3. get_adults(users) - возвращает список пользователей старше 18 лет
# 4. find_top_student(users) - возвращает имя пользователя с наивысшим баллом
# 5. update_scores(users, bonus=5) - добавляет bonus баллов всем активным пользователям
#    (функция должна изменить исходный список!)

def get_active_users(users):
    '''Возвращает список имён активных пользователей'''

    active_users = []
    for item in users:
        if item['active'] == True: # Можно просто if item['active']:
            active_users.append(item['name'])
    return active_users

def get_average_score(users):
    '''Возвращает средний балл всех пользователей'''

    sum_score = 0
    count = 0
    for item in users:
        sum_score += item['score']
        count += 1
    avg_score = sum_score / count # лучше округлить  round(sum_score / count, 2)
    return avg_score

def get_adults(users):
    '''Возвращает список пользователей старше 18 лет'''

    users_18 = []
    for item in users:
        if item['age'] >= 18:
            users_18.append(item['name'])
    return users_18

def find_top_student(users):
    '''Возвращает имя пользователя с наивысшим баллом'''

    top_score = 0
    top_student = ''
    for item in users:
        if item['score'] > top_score:
            top_score = item['score']
            top_student = item['name']
    return top_student

def update_scores(users, bonus=5):
    '''добавляет bonus баллов всем активным пользователям'''

    for item in users:
        if item['active'] == True: # Можно просто if item['active']:
            item['score'] += bonus
    return users

print(get_active_users(users))
print(get_average_score(users))
print(get_adults(users))
print(find_top_student(users))
print(update_scores(users))