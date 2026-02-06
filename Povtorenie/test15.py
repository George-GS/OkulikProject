# Задание 1
# import mysql.connector
#
# db = mysql.connector.connect(
#     host='db4free.net',
#     port=3306,
#     user='gs_user',
#     password='gs_test_pass123!',
#     database='gs_test_base'
# )
#
# print('✅ Подключение успешно')
#
# cursor = db.cursor(dictionary=True)
# cursor.execute("""
#     CREATE TABLE test_results (
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         test_name VARCHAR(30),
#         status VARCHAR(10),
#         execution_time DECIMAL(5, 2),
#         timestamp DATETIME
#         )
# """)
#
# insert_query = """
#     INSERT INTO test_results (test_name, status, execution_time, timestamp)
#     VALUES (%s, %s, %s, %s)
#     """
#
# test_data = [
#     ('test_login', 'passed', 1.23, '2024-02-04 14:30:45'),
#     ('test_checkout', 'failed', 2.15, '2024-02-04 14:31:00'),
#     ('test_search', 'skipped', 0.1, '2024-02-04 14:32:10'),
#     ('test_registration', 'passed', 3.5, '2024-02-04 14:33:20'),
#     ('test_payment', 'passed', 1.8, '2024-02-04 14:34:00')
# ]
#
# cursor.executemany(insert_query, test_data)
# db.commit()
#
# cursor.execute("SELECT * FROM test_results")
# result = cursor.fetchall()
# print(result)
#
#
# db.close()

# # Задание 2
# import mysql.connector
#
# class TestDBUtils:
#
#     def __init__(self):
#         self.db = mysql.connector.connect(
#         host='db4free.net',
#         port=3306,
#         user='gs_user',
#         password='gs_test_pass123!',
#         database='gs_test_base'
#     )
#         self.cursor = self.db.cursor(dictionary=True)
#
#     def count_passed_tests(self):
#         '''Возвращает количество пройденных тестов'''
#         self.cursor.execute('SELECT COUNT(*) as count FROM test_result WHERE status = "passed"')
#         result = self.cursor.fetchone()
#         return result['count']
#
#     def close(self):
#         """Закрывает соединение с БД."""
#         self.cursor.close()
#         self.db.close()
#
# # Создаем объект
# tester = TestDBUtils()
#
# # Вызываем метод
# passed_count = tester.count_passed_tests()
# print(f"Пройдено тестов: {passed_count}")
#
# # Закрываем соединение
# tester.close()

# Задание 3
#
# result = {
#     "url": "/api/users",
#     "status_code": 201,
#     "response_time": 150,
#     "data": {"id": 123}
# }
#
# def test01(result):
#     match result:
#         case 'passed':
#             return 'Тест пройден'
#         case 'failed':
#             return 'Тест упал'
#         case 'skipped':
#             return 'Тест пропущен'
#         case _:
#             return 'Неизвестный статус'

# Задание 4

config_lines = [
    "browser = chrome",
    "timeout = 30",
    "headless = true",
    "retry_count = 3"
]

for line in config_lines:
    key, value = line.split(' = ')
    if '=' in line and key == 'timeout':
        print(f"Найден timeout: {int(value)}")
        break

# с моржовым операторм
for line in config_lines:
    if '=' in line and (key_value := line.split('=')):
        key = key_value[0].strip()
        value = key_value[1].strip()
        if key == 'timeout':
            timeout = int(value)
            print(f"Найден timeout: {timeout}")
            break