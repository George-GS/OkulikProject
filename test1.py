name = input('Введите ваше имя: ')
demo = f'Привет, {name}!'
print(demo)

age = input(f"{name}, введите ваш возраст: ")
print(f'Ваш возраст: {age}')

age = int(age)

if age > 28:
    print(f'{name}, Вы милениал')

else:
    print('Ты школьник')
