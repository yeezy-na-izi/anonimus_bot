from main import *
from .keyboards import *
import telebot
from .connect_with_users import *
from .DataBases import *

bot = telebot.TeleBot('1467056746:AAEGEMZV_XJpJAZjM0mffj3DdeG4RBpJe3I')

set_profile = dict()
error_sl = dict()
bog_mes = dict()


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


@bot.message_handler(regexp='🛠 Error')
def error_mes(message):
    bot.send_message(message.chat.id, 'Что вы хотите отправить богу (админу)?')
    error_sl[message.chat.id] = True


@bot.message_handler(regexp='🔙 Вернуться назад')
def go_back(message):
    bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=main_keyboard)


# profile commands
@bot.message_handler(regexp='👤 Профиль')
def profile_message(message):
    bot.send_message(message.chat.id, 'Ну, твой профиль', reply_markup=profile_keyboard)


@bot.message_handler(regexp='🔄 Заново заполнить профиль')
def save_profile(message):
    bot.send_message(message.chat.id, 'Напиши свое имя')
    set_profile[message.chat.id] = [False, True, True, True]


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


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.chat.id in set_profile:
        if not set_profile[message.chat.id][0]:
            set_profile[message.chat.id][0] = message.text
            set_profile[message.chat.id][1] = False
            bot.send_message(message.chat.id, 'Напишите фамилию')
        elif not set_profile[message.chat.id][1]:
            set_profile[message.chat.id][1] = message.text
            set_profile[message.chat.id][2] = False
            bot.send_message(message.chat.id, 'Напишите небольшую информацию о себе')
        elif not set_profile[message.chat.id][2]:
            set_profile[message.chat.id][2] = message.text
            set_profile[message.chat.id][3] = False
            bot.send_message(message.chat.id, 'Ваш пол', reply_markup=gender_keyboard)
    if message.chat.id in error_sl:
        if error_sl[message.chat.id]:
            send_analytic(message, 'anonimus_chat_bot')
            bot.send_message(message.chat.id, 'Успешно отправлено', reply_markup=main_keyboard)
            error_sl[message.chat.id] = False
    if message.chat.id in bog_mes:
        if bog_mes[message.chat.id][0]:
            try:
                bot.send_message(bog_mes[message.chat.id][1], message.text)
                bog_mes[message.chat.id] = [False, False]
                bot.send_message(message.chat.id, 'Успешно')
            except:
                bot.send_message(message.chat.id, 'Сорян, я слишокм слаб чтобы это сделать')


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if 'gender' in call.data:
        if call.data == 'gender.man':
            set_profile[call.message.chat.id][3] = True
        else:
            set_profile[call.message.chat.id][3] = False
        bot.send_message(call.message.chat.id, f'Сохранить?\n'
                                               f'Ваше имя: {set_profile[call.message.chat.id][0]}\n'
                                               f'Ваша фамилия: {set_profile[call.message.chat.id][1]}\n'
                                               f'Информация о себе: {set_profile[call.message.chat.id][2]}\n'
                                               f'Ваш пол: '
                                               f'{"Мужской" if set_profile[call.message.chat.id][3] else "Женский"}',
                         reply_markup=edit_profile_key)
    elif call.data == 'bog':
        bog_mes[call.message.chat.id] = [True, int(call.message.text.split('\n')[2][3:])]
        bot.send_message(call.message.chat.id, 'Напиши твое сообщение')
    elif 'prof' in call.data:
        if 'yes' in call.data:
            data_add_users(set_profile[call.message.chat.id], call.message.chat.id)
            bot.send_message(call.message.chat.id, "Сохранено...")
        else:
            bot.send_message(call.message.chat.id, 'Вы хотите перезаполнить форму?')
    bot.answer_callback_query(call.id)


# main def
def helper(message):
    bot.send_message(message.chat.id, 'Тут какой-то помошник', reply_markup=main_keyboard)


def find_people(message):
    bot.send_message(message.chat.id, 'Медленно ищу', reply_markup=chat_keyboard)
