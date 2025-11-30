# Напиши программу, которая:
# 1. Просит вводить числа пока не введут 0
# 2. Считает сумму всех введенных чисел
# 3. Выводит максимальное введенное число

total = 0
max_num = 0

max_lst = []
number = int(input('введите число: '))

while number != 0:
    total += number
    max_lst.append(number)
    number = int(input('Введите другое число: '))

print(f'общая сумма: {total}')
print(f'максимальное число: {max(max_lst)}')