import botData
import telebot
import requests
from bs4 import BeautifulSoup as BS


bot = telebot.TeleBot(botData.TOKEN)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ человек')

    #Keyboard
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    item1 = telebot.types.InlineKeyboardButton("Похвали меня!", callback_data='good')
    item2 = telebot.types.InlineKeyboardButton("Обзови меня!", callback_data='bad')
    item3 = telebot.types.InlineKeyboardButton("Расписание", callback_data='photo')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Привет",parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def blabla(message):
    if message.chat.type == 'private':
        if message.text == "Похвали меня!":
            bot.send_message(message.chat.id, "Ты молодец!!!")
        elif message.text == "Обзови меня!":
            bot.send_message(message.chat.id, "Ты ленивый!!!")
        elif message.text == "Расписание":
            p = open("img/schedule.png", 'rb')
            bot.send_photo(message.chat.id, p)
        else:
            bot.send_message(message.chat.id, "Я не знаю что отвевить(")

@bot.callback_query_handlers(func=lambda callFunc: True)
def callback_query(callFunc):
    try:
        if callFunc.data == 'good':
            bot.send_message(callFunc.message.chat.id, "Ты красавчик!!!")
        elif callFunc.data == 'callFunc':
            bot.send_message(callFunc.message.chat.id, "Ты дурак!!!")

        bot.edit_message_text(chat_id=callFunc.message.chat.id, reply_markup=None)
    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    bot.polling(none_stop=True)