#Мы попробовали парсинг ссылок, теперь перейдём к парсингу цитат.

#На сайте https://quotes.toscrape.com/ мы видим цитаты, их авторов и теги.

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

#Создадим отдельную переменную text, куда будут сохраняться все цитаты
#text = soup.find("span", class_="text")
#print(text)

text = soup.find_all("span", class_="text")
#print(text)

#Создадим отдельную переменную author, куда будут сохраняться все авторы
author = soup.find_all("small", class_="author")
#print(author)

for i in range(len(text)):
    print(f"Цитата номер - {i + 1}")
    print(text[i].text)
    print(f"Автор цитаты - {author[i].text}\n")