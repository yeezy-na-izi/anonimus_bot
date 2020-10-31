import telebot

callback_bot = telebot.TeleBot('1385232383:AAEiIL7rGofcHw8vehkgakxYyMKe3miBhnQ')
admins = [380907452, 441567171]


def send_analytic(message, from_bot):
    for i in admins:
        callback_bot.send_message(i, f'Username: @{message.from_user.username}\n'
                                     f'Текст: {message.text}\n'
                                     f'Id: {message.chat.id}\n'
                                     f'Имя: {message.from_user.first_name}\n'
                                     f'Фамилия: {message.from_user.last_name}\n'
                                     f'Бот: @{from_bot}')
