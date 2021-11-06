import random
import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Hi', 'hi', 'hello', 'hey', 'hola'])
def greet(message):
    number = str(int(random.uniform(-1, 10)))
    print(number)
    path = "pics/"
    img = open(path + number + ".png", 'rb')
    bot.send_photo(message.chat.id, img)

bot.polling()
