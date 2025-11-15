# Задание 3: Декоратор для повторения теста

# Напиши декоратор @repeat(n), который запускает тест n раз
# Выводи "Попытка 1/X", "Попытка 2/X"...
# Примени его к тестовой функции с 3 повторениями

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = 1
            while count <= n:
                print(f'Попытка {count}/{n}')
                result = func(*args, **kwargs)
                count += 1
            return result
        return wrapper
    return decorator

@repeat(3)
def simple1():
    print('simple 1')

simple1()