# Создай генератор, который выдает тестовые email-адреса для регистрации
# Формат: testuser1@test.com, testuser2@test.com, testuser3@test.com...
# Должен работать бесконечно

def email_gen():
    num = 1
    mail = 'testuser1@test.com'
    while True:
        yield mail
        num += 1
        mail = 'testuser' + str(num) + '@test.com'

gen = email_gen()
print(next(gen))
print(next(gen))
print(next(gen))