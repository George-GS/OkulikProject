# Задание 1
# Сделай:
# 1. Добавь "Diana" с номером "456-7890"
# 2. Измени номер Bob на "999-9999"
# 3. Удали Charlie
# 4. Проверь есть ли "Eve" в телефонной книге
# 5. Выведи все имена из телефонной книги


phonebook = {
    "Alice": "123-4567",
    "Bob": "234-5678",
    "Charlie": "345-6789"
}
phonebook['Diana'] = '456-7890'
print(phonebook)
phonebook.update({'Bob' : "999-9999"})
print(phonebook)
phonebook.pop('Charlie')
print(phonebook)
print('Eve' in phonebook)
for name in phonebook:
    print(name)

# Задание 2
# Напиши код, который:
# 1. Выводит все продукты дороже 1.50
# 2. Считает общую стоимость всех продуктов
# 3. Находит самый дорогой и самый дешевый продукт
# 4. Увеличивает цены всех продуктов на 10%
products = {
    "apple": 1.20,
    "banana": 0.80,
    "orange": 1.50,
    "kiwi": 2.00,
    "grape": 3.50
}
tot_sum = 0
max_price = max(products.values())
min_price = min(products.values())

for prod, price in products.items():
    if price > 1.50:
        print(prod)

    tot_sum += price

    if price == max_price:
        print(f'самый дорогой фрукт {prod}')

    if price == min_price:
        print(f'самый дешевый фрукт {prod}')


print(f'Сумма всех продуктов {tot_sum}')
print(list(products.items()))

for prod in products:
    products[prod] = round(products[prod] * 1.1, 2)

print(f'Новые цены {products}')
