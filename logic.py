import random
import requests


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def command_list():
    commands = """
/start - Бот отвечает вам "Привет! Я твой Telegram бот. Напиши что-нибудь!"

/hello - Бот отвечает вам "Привет! Как дела?"

/bye - Бот отвечает вам "Пока! Удачи!"

/password - Бот генерирует вам пароль из количества символов ( /password <число> ) 

/help - Команда которая выводит весь список команд

/heh - Выводит столько he сколько вы хотите ( /heh <число> )

/calc - Считает пример за вас ( /calc <пример> )

/newnickname - Добавляет к вашему username символы ( /newnickname <число> )

/flip - Подбрасывает монету

Если вы ввели команду которой не существует то бот ответит вам тем же что вы написали ему
    """
    return commands

def flip():
    coin = random.randint(1,3)
    return coin

def fox():
    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    return data['image']
