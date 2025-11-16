# Создай файл test_config.py с настройками для тестов
# Внутри должны быть переменные:
# - BASE_URL = "https://example.com"
# - TIMEOUT = 10
# - BROWSER = "chrome"
#
# Затем импортируй их в основном файле и используй

import test_config

print(test_config.TIMEOUT)

from Lesson.lesson_8 import test_config2

print(test_config2.BASE_URL)

