# Результаты тестирования функциональности
test_results = [45, 89, 0, 76, -3, 92, 100, None, 68]

# Отфильтруй валидные результаты (только числа от 0 до 100)
# и преобразуй их в строки с добавлением "%"
# Используй filter и map вместе


test_filter = list(filter(lambda x:  x is not None and 0 <= x <= 100, test_results))
print(list(map(lambda x: str(x)+'%', test_filter)))





