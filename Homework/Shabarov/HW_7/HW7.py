# Напиши функцию, которая:
# 1. Принимает список чисел
# 2. Возвращает словарь с:
#    - "sum": сумма всех чисел
#    - "avg": среднее значение
#    - "max": максимальное число
#    - "min": минимальное число

anal_dict = {}
def analyze_numbers(numbers):
    a = sum(numbers)
    b = sum(numbers) / len(numbers)
    c = max(numbers)
    d = min(numbers)

    return {
        'sum' : a,
        'avg' : b,
        'max' : c,
        'min' : d
    }


result = analyze_numbers([10, 5, 20, 15, 8])
print(result)