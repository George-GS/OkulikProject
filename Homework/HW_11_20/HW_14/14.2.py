# Задание 1: Обработка ошибок ввода
#
# python
# Напиши функцию, которая запрашивает число у пользователя
# и обрабатывает ValueError если введен не число
# Используй try-except

def calc():
    try:
        x = int(input('Введите число 1: '))
        y = int(input('Введите число 2: '))
        return x / y
    except ValueError:
        print('Вы ввели не число')
        return None
    except ZeroDivisionError:
        print('Нельзя делить на 0')
        return None

result = calc()  # ← Вызываем calc(), а не met_err()
print(result)