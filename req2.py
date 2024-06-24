import requests


img="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Redhead_Cat_%28%D0%A0%D1%8B%D0%B6%D0%B8%D0%B9_%D0%9A%D0%BE%D1%82%29.jpg/1200px-Redhead_Cat_%28%D0%A0%D1%8B%D0%B6%D0%B8%D0%B9_%D0%9A%D0%BE%D1%82%29.jpg"
response = requests.get(img)
with open("test.jpg", "wb") as file:
    file.write(response.content)