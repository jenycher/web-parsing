#Попробуем работать с другим сайтом — randomword.com
#Здесь постоянно выдаются рандомные слова, с которыми мы создадим мини-игру.

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def choose_language():
    print("Выберите язык / Choose the language:")
    print("   1. Русский")
    print("   2. English")

    language = input("Выберите язык / Choose the language: ")

    if language == "1":
        return "русский"
    elif language == "2":
        return "english"
    else:
        print("Неверный выбор. Попробуйте еще раз / Wrong choice. Please try again.")
        return choose_language()

# Создаём функцию, которая будет получать информацию
def get_english_words(language):
    if language.lower() == 'русский':
        url = "https://randomword.com/"
        translator = Translator()
    else:
        url = "https://randomword.com/"
        translator = Translator()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        russian_word = translator.translate(english_word, dest="ru").text

        word_definition = soup.find("div", id="random_word_definition").text.strip()
        word_definition_ru = translator.translate(word_definition, dest="ru").text

        return {
            "english_word": english_word,
            "russian_word": russian_word,
            "word_definition": word_definition,
            "word_definition_ru": word_definition_ru
        }
    except Exception as e:
        print("Произошла ошибка:", e)


# Создаём функцию, которая будет делать саму игру
def word_game():
    language = choose_language()

    print("Добро пожаловать в игру!")

    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words(language)
        word = word_dict.get("russian_word" if language.lower() == 'русский' else "english_word")
        word_definition = word_dict.get("word_definition_ru" if language.lower() == 'русский' else "word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру

        play_again = input("Хотите сыграть еще раз? y/n:")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()