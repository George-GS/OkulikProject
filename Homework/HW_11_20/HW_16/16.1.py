# ЗАДАНИЕ 1: Простой подсчет результатов тестов
#
# python
# test_results = ["passed", "failed", "passed", "passed", "failed"]
# # Задача: посчитать сколько тестов прошло, а сколько упало

from collections import defaultdict

# Результаты автотестов за неделю
test_results = [
    "passed", "failed", "passed", "passed", "failed",
    "passed", "passed", "passed", "failed", "skipped",
    "passed", "passed", "failed", "passed", "passed",
    "skipped", "passed", "passed", "passed", "passed"
]

data = defaultdict(int)

for item in test_results:
    data[item] += 1

print(dict(data))