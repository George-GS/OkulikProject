numbers = [15, 7, 23, 4, 18, 9, 12, 6, 21]

# Напиши цикл for, который:
# 1. Выводит все четные числа
# 2. Считает сумму чисел больше 10
# 3. Находит количество чисел, делящихся на 3

a_lst = []
x_sum = 0
num_3 = 0

for numb in numbers:
    if numb % 2 == 0:
        a_lst.append(numb)
    if numb > 10:
        x_sum += numb
    if numb % 3 == 0:
        num_3 += 1


print(a_lst)
print(x_sum)
print(num_3)