# Есть список логинов в разных форматах
logins = ["  user123  ", "ADMIN", "  guest_user  "]

# Нужно привести все логины к стандартному формату:
# - убрать лишние пробелы
# - все буквы в нижний регистр
# Результат: ["user123", "admin", "guest_user"]
# Используй map

logins = ["  user123  ", "ADMIN", "  guest_user  "]

# def dfsdf(x):
#     x = " "
#     x.strip().lower()

logins_new = list(map(lambda x: x.strip().lower(), logins))
print(logins_new)