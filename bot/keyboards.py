import telebot

main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
main_keyboard.row('👤 Профиль', '😜 Найти собеседника')
main_keyboard.row('❔ Помощь')

profile_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
profile_keyboard.row('✏ Изменить профиль', '🔄 Заново заполнить профиль')
profile_keyboard.row('🔙 Вернуться назад')

chat_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
chat_keyboard.row('😜 Найти нового собеседника')
chat_keyboard.row('⛔ Прекратить диалоги')

gender_keyboard = telebot.types.InlineKeyboardMarkup()
gender_keyboard.add(telebot.types.InlineKeyboardButton('🚹 Мужской', callback_data='gender.man'))
gender_keyboard.add(telebot.types.InlineKeyboardButton('🚺 Женский', callback_data='gender.woman'))

edit_profile_key = telebot.types.InlineKeyboardMarkup()
edit_profile_key.add(telebot.types.InlineKeyboardButton('Да', callback_data='google.com'))
edit_profile_key.add(telebot.types.InlineKeyboardButton('Нет', callback_data='google.com'))
