import dotenv
import os


dotenv.load_dotenv()

login  = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

def auth(log, passw):
    print(f'Пользователь {log} успешно авторизован')

auth(login, password)

