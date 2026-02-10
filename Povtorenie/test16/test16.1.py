import csv
from collections import defaultdict

with open('test.csv') as file:
    reader = csv.DictReader(file)
    data = defaultdict(list)

    for row in reader:
        modul = row['module']
        data[modul].append(row)

    print(dict(data))
    print()

    for module, tests in data.items():
        total = len(tests)
        status_count = {}
        for test in tests:
            status = test['status']
            status_count[status] = status_count.get(status, 0) + 1

        status_parts = []
        for status, count in status_count.items():
            if count > 0:
                status_parts.append(f"{count} {status}")

        status_str = ", ".join(status_parts)
        print(f"Модуль {module}: {total} тест{'а' if total != 1 else ''} ({status_str})")




