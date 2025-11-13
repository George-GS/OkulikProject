#Задание 3: Генерация тестовых дат

# Создай дату: 15 марта 2024 года
# Преобразуй её в формат "15.03.2024"
# Используй datetime

import datetime

gs_date = datetime.datetime(2024, 3, 15)
print(gs_date)

form_gs_date = gs_date.strftime('%d.%m.%Y')
print(form_gs_date)

print(gs_date.year)