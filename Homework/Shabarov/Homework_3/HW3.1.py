#Сделал новую ветку

weight = 100    # кг
height = 1.73  # м

imt = weight / height**2

print(f'ИМТ = {imt}')

if imt < 18.5:
    print('У вас недостаточный вес')

if imt > 18.5 and imt < 25:
    print('У вас нормальный вес')

if imt > 25:
    print('У вас избыточный вес')
