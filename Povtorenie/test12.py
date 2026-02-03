class MyClass:
    @property  # Декоратор свойства
    def my_word(self):  # Геттер свойства
        return 'hello'  # Возвращаем значение

    def act(self):  # Обычный метод
        return 'hello'  # Выводим сообщение


qqq = MyClass()  # Создаем объект

print(qqq.act())
print(qqq.my_word)