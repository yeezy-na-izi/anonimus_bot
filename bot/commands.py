from main import *
from .keyboards import *
import telebot

bot = telebot.TeleBot('1467056746:AAEGEMZV_XJpJAZjM0mffj3DdeG4RBpJe3I')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Это лучший анонимный чат бот в мире!\n'
                                      'Напиши /help что бы узнать полный список возможностей бота!',
                     reply_markup=main_keyboard)


@bot.message_handler(commands=['help'])
def help_commands(message):
    helper(message)


@bot.message_handler(regexp='❔ Помощь')
def help_message(message):
    helper(message)


@bot.message_handler(regexp='🔙 Вернуться назад')
def go_back(message):
    bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=main_keyboard)


# profile commands
@bot.message_handler(regexp='👤 Профиль')
def profile_message(message):
    bot.send_message(message.chat.id, 'Ну, твой профиль', reply_markup=profile_keyboard)


# chat commands
@bot.message_handler(regexp='😜 Найти нового собеседника')
def re_find_people_message(message):
    find_people(message)


@bot.message_handler(regexp='😜 Найти собеседника')
def find_people_message(message):
    find_people(message)


@bot.message_handler(regexp='⛔ Прекратить диалоги')
def stop_chat(message):
    bot.send_message(message.chat.id, 'Вы прекратили диалоги', reply_markup=main_keyboard)


# main def
def helper(message):
    bot.send_message(message.chat.id, 'Тут какой-то помошник', reply_markup=main_keyboard)


def find_people(message):
    bot.send_message(message.chat.id, 'Медленно ищу', reply_markup=chat_keyboard)
