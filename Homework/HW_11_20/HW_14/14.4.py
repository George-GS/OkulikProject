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


# now = datetime.datetime.now()
# now1 = now + datetime.timedelta(days=1)
# print(now)
# print(now1)