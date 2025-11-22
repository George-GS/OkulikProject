# ЗАДАНИЕ 2: Чтение тестовых данных из файла
# В файле test_users.csv:
# username,password,expected_result
# user1,pass123,success
# user2,wrongpass,error
# Задача: прочитать файл и подготовить данные для тестов

import csv

with open('data.csv', newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for item in file_data:
        data.append(item)

print(data)

# def login(username, password):
#     print(f"Приняты данные: логин={username}, пароль={password}")
#     print('Успешный вход')
#     return True
#
# login(data[1]['username'], data[1]['password'])

#выше мое решение, ниде улучшение

def login(username, password, expected_result):
    print(f"Тест: логин={username}, пароль={password}, ожидаем: {expected_result}")

    # Симуляция проверки логина
    if password == "wrongpass" or password == 'short':
        actual_result = "error"
        print("❌ Ошибка входа - неверный пароль")
    else:
        actual_result = "success"
        print("✅ Успешный вход")

    # Проверяем соответствие ожиданий и результата
    if actual_result == expected_result:
        print("✅ ТЕСТ ПРОЙДЕН")
        return True
    else:
        print("❌ ТЕСТ НЕ ПРОЙДЕН")
        return False

count = 0
# Запускаем все тесты из файла
for test_case in data:
    count += 1
    print()
    print(f'Тест №{count}🎉')
    login(test_case['username'], test_case['password'], test_case['expected_result'])
