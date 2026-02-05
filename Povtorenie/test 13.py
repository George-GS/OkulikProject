# Напиши функцию, которая запрашивает число у пользователя
# и обрабатывает ValueError если введен не число
# Используй try-except


# def func_one():
#     while True:
#         try:
#             x = float(input('Введите число 1: '))
#             y = float(input('Введите число 2: '))
#             print(f'Результат деленеи {x} на {y} равен {x / y}')
#
#         except ValueError:
#             print('Вы ввели не число')
#         except ZeroDivisionError:
#             print('На ноль делить нельзя')
#
#         print('Попытка завершена')
#
#         choice = input('Повторить попытку? Пожалуйста введите "да" или "нет": ').lower().strip()
#         if choice != 'да':
#             break
#
# func_one()


# Создай config.txt с настройками:
# timeout=10
# browser=chrome
# headless=false
#
# Прочитай файл и преобразуй в словарь

# def read_file():
#     gs_dict = {}
#     with open('config.txt', 'r') as file:
#         for line in file:
#             line = line.strip()
#             key, value = line.split('=')
#             gs_dict[key] = value
#
#     print(gs_dict)
#
# read_file()

# Задание 3: Генерация тестовых данных с датами
#
# python
# Создай список из 5 дат - сегодня + 1 день, +2 дня, +3 дня...
# Используй datetime и timedelta

import datetime

def gen_date(limit):
    count = 0
    today = datetime.date.today()
    while count < limit:
        yield today.strftime('%d.%m.%Y')
        today += datetime.timedelta(days=1)
        count += 1

date = list(gen_date(5))
print(date)


