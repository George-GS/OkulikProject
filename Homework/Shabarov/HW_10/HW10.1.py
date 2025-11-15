# Задание 1: Декоратор для измерения времени теста

# Напиши декоратор @timeit, который измеряет время выполнения теста
# и выводит "Тест выполнялся: X.XX секунд"
# Примени его к тестовой функции

import datetime
import time  #чтобы добавить задержку

def timeit(func):
    def wrapper(*args, **kwargs):
        now1 = datetime.datetime.now()
        print(f'Время начала теста {now1}')
        result = func(*args, **kwargs)
        now2 = datetime.datetime.now()
        print(f'Время окончания теста {now2}')
        dif_sec = now2 - now1
        print(f'Тест выполнялся: {round(dif_sec.total_seconds(), 2)} секунд')
        # print(f'выполнялся: {round(dif_sec.seconds, 2)} секунд') - можно и так было, но тогда бы дробной части не было

        return result


    return wrapper

@timeit
def simple1():
    print('simple 1')
    time.sleep(2.535) #чтобы добавить задержку

simple1()




