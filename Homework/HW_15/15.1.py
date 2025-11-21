# Задание 1: Проверка регистрации пользователя в БД
#
# python
# # Напиши код который проверяет что после добавления пользователя в таблицу через sql запрос пользователь появился в таблице users

import mysql.connector as mysql
import os

bd = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st4'

)

cursor = bd.cursor(dictionary=True)
cursor.execute("INSERT INTO users (name, age) VALUES ('Oleg', 15)")
values = cursor.lastrowid
bd.commit()

query = ('SELECT id, name FROM users WHERE id = %s')
cursor.execute(query, (values,))
user1 = cursor.fetchone()

match user1['name']:
    case 'Oleg':
        print('Status - OK')
    case _:
        print('status - failed')

bd.close()