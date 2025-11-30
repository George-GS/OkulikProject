# Задание 1: Обработка ошибок в тестах
# Напиши функцию теста с обработкой исключений:
# - ElementNotVisibleException
# - TimeoutException
# - NoSuchElementException


from selenium.common.exceptions import ElementNotVisibleException, TimeoutException, NoSuchElementException

def met_err(x, y):
    try:
        x = int(input('Введите число 1: '))
        y = int(input('Введите число 2: '))
        return x / y
    except NoSuchElementException:
        print('элемент не найден на странице')
    except ElementNotVisibleException:
        print('элемент есть, но не виден')
    except TimeoutException:
        print('время ожидания истекло')
    except ZeroDivisionError:
        print('Не делим на 0')

print(met_err())