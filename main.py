import telebot
from config import TOKEN
from logic import gen_pass, command_list, flip, fox
import os
import random
import requests

    
bot = telebot.TeleBot(TOKEN)
memes = os.listdir("./img")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['password'])
def send_pass(message):
    words = message.text.split()
    if len(words) > 1:
        try:
            password = gen_pass(int(words[1]))
            bot.reply_to(message, f"Ваш пароль: {password}")
        except (ValueError,SyntaxError,NameError,TypeError):
            bot.reply_to(message, "Введите число после команды")
    else:
        password = gen_pass(8)
        bot.reply_to(message, password)
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, command_list())
    
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(commands=['calc'])
def send_calc(message):
    to_calc = message.text.split()
    if len(to_calc) > 1:
        try:
            bot.reply_to(message, eval(to_calc[1]))
        except (SyntaxError, NameError, TypeError):
            bot.reply_to(message, "Неккоректный пример")
    
@bot.message_handler(commands=['newnickname'])
def send_nickname(message):
    username = message.from_user.username
    words = message.text.split()
    if len(words) > 1:
        try:
            password = gen_pass(int(words[1]))
            bot.reply_to(message, f"Ваш новый ник: {username + password}")
        except(SyntaxError, TypeError, NameError, ValueError):
            bot.reply_to(message, "Введите число")
    else:
        bot.reply_to(message, "Введите число после команды")
    
@bot.message_handler(commands=['flip'])
def send_flip(message):
    coin = flip()
    if coin == 1:
        bot.reply_to(message, "Выпала решка")
    elif coin == 2:
        bot.reply_to(message, "Выпал орёл")
    elif coin == 3:
        bot.reply_to(message, "Выпало ребро")
        
@bot.message_handler(commands=['meme'])
def send_meme(message):
    words = message.text.split()
    if len(words) == 2:
        num_mem = int(words[1])
        if 0 < num_mem <= len(memes):
            with open(f"./img/{memes[num_mem -1]}", "rb") as f:
                bot.send_photo(message.chat.id, f)
            return
    with open(f"./img/{random.choice(memes)}", "rb") as f:
        bot.send_photo(message.chat.id, f)
        
@bot.message_handler(commands=['fox'])
def send_fox(message):
    image_url = fox()
    bot.send_photo(message.chat.id, image_url)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()
