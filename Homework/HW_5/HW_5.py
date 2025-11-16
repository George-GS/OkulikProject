# Задание 1
#coordinates = (45, 78, 12)
# Задача: Распаковать координаты в переменные x, y, z и вывести их в формате: "X: 45, Y: 78, Z: 12"

x, y, z = coordinates
print(f'X: {x}, Y: {y}, Z: {z}')

# Задание 2.
# text = "Python Programming"
#
print(text[0:6])
print(text[7:])
print(text[2:10])
print(text[-1: :-1])

# Задание 3. Задача: Преобразовать строку чтобы получилось: "Hello world! Today is a great day."
# sentence = "  hello WORLD! today is a GREAT day.  "
#
sentence = sentence.strip().capitalize().replace('today', 'Today')
print(sentence)

#Задание 4/ Задача: Распаковать первые два элемента в first_name, last_name, а остальные в список details

data = ["John", "Smith", 30, "programmer", "New York"]

first_name, last_name, *details = data

print(f"first_name: {first_name}")
print(f"last_name: {last_name}")
print(f"details: {details}")

# Задание 5. Разделить строку по ;, затем каждую часть очистить от лишних пробелов и вывести в формате:
# Email: user@example.com
# Phone: +123456789

text = "Email: user@example.com; Phone: +123456789"
a, b = text.split(';')
a = a.strip()
b = b.strip()

print(a)
print(b)
