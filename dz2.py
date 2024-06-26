#Задание 2: Параметры запроса
#Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#Отправьте GET-запрос с параметром userId, равным 1.
#Распечатайте полученные записи.

import requests
import pprint

params = {
    'userId' : 1
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)


print(f"Статус-код= {response.status_code}")
posts = response.json()
for post in posts:
    print(post)


