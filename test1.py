api_response = {
    "status": "success",
    "data": {
        "user_id": 12345,
        "name": "John Doe", 
        "orders": [101, 102, 103]
    },
    "message": "User found successfully"
}

# Задания:
# 1. Получи имя пользователя из ответа
# 2. Проверь равен ли статус "success" 
# 3. Выведи количество заказов пользователя
# 4. Выведи сообщение от API

print(api_response['data']["name"])
