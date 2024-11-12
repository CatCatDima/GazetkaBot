import telebot
from telebot import types
import ads, designs, resources, users

with open("./key.txt") as f:
    key=f.read()
    if key=="":
        TOKEN=input("Введите API токен: ")
    else:
        TOKEN=key
        print('API токен загружен из файла "./key.txt"')
    f.close()
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(['start','главное_меню'])
def mainmenu(message):
    markup=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    search=types.KeyboardButton('/поиск')
    recommendations=types.KeyboardButton('/рекомендации')
    my_ads=types.KeyboardButton('/мои_объявления')
    channels=types.KeyboardButton('/каналы')
    settings=types.KeyboardButton('/Настройки')

    markup.add(search,recommendations,my_ads,channels,settings)

    bot.send_message(message.chat.id,'главное меню',reply_markup=markup)

@bot.message_handler(['мои_объявления'])
def myads(message):
    markup=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)

    markup.add(types.KeyboardButton('/главное_меню'))

    for ad in ads.search({"user":message.from_user.id}):
        markup.add(ad.header)

    markup.add(types.KeyboardButton('/+новое_объявление+'))

    bot.send_message(message.chat.id,'главное меню',reply_markup=markup)

print("Бот запущен успешно!")
bot.polling(True)
