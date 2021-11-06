import PyPDF2
import random
import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
quote = "Protect your own good in all that you do, and as concerns everything else take what is given as far as you can make reasoned use of it. If you don’t, you’ll be unlucky, prone to failure, hindered and stymied.     -Epictetus"
#number = int(random.uniform(0, 5))
pdfObj = open('quotes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)
#pageObj = pdfReader.getPage(number)

@bot.message_handler(commands=['Hi', 'hi', 'hello', 'hey', 'hola'])
def greet(message):
    bot.send_message(message.chat.id,quote)
bot.polling()

