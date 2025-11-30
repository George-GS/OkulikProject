import datetime
import requests


def time_request(url):
    start_time = datetime.datetime.now()
    response = requests.get(url)
    end_time = datetime.datetime.now()

    return (end_time - start_time).total_seconds()


time = time_request('https://jsonplaceholder.typicode.com/posts')
print(f"Запрос выполнен за {time:.2f} секунд")
