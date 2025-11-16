# Задание 1
# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary. А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

def rand_bon():
    salary = int(input('Введите цену '))
    bonus = [True, False]
    if random.choice(bonus) is True:
        salary += random.randrange(1,10000)
    else:
        print("😔 Бонус не начислен")
    return salary

print(rand_bon())

