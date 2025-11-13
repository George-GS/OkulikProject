#Задание 2: Фильтрация пользователей
# Есть список пользователей с возрастом
users = [
    {"name": "John", "age": 17},
    {"name": "Anna", "age": 25},
    {"name": "Mike", "age": 16},
    {"name": "Sarah", "age": 30}
]
# Оставить только совершеннолетних (18+)
# Используй filter


# age_plus = []
# def scan_age(age):
#     for x in age:
#         if x['age'] >= 18:
#             age_plus.append(x)
#     return age_plus

adult_users = list(filter(lambda x: x['age'] >= 18, users))

print(adult_users)

