import telebot

main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
main_keyboard.row('👤 Профиль', '😜 Найти собеседника')
main_keyboard.row('❔ Помощь', '🛠 Error')

profile_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
profile_keyboard.row('🔄 Заполнить профиль', '⚙ Настройки')
profile_keyboard.row('🔙 Вернуться назад')

chat_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
chat_keyboard.row('😜 Найти нового собеседника')
chat_keyboard.row('⛔ Прекратить диалоги')

gender_keyboard = telebot.types.InlineKeyboardMarkup()
gender_keyboard.add(telebot.types.InlineKeyboardButton('🚹 Мужской', callback_data='gender.man'))
gender_keyboard.add(telebot.types.InlineKeyboardButton('🚺 Женский', callback_data='gender.woman'))

edit_profile_key = telebot.types.InlineKeyboardMarkup()
edit_profile_key.add(telebot.types.InlineKeyboardButton('✅ Да', callback_data='prof.yes'))
edit_profile_key.add(telebot.types.InlineKeyboardButton('❌ Нет', callback_data='prof.no'))

bog_keyboard = telebot.types.InlineKeyboardMarkup()
bog_keyboard.add(telebot.types.InlineKeyboardButton('Ответить', callback_data='bog'))

set_key = telebot.types.InlineKeyboardMarkup()
set_key.add(telebot.types.InlineKeyboardButton('Показать профиль?', callback_data='sett.show'))
set_key.add(telebot.types.InlineKeyboardButton('Ищу гендер', callback_data='sett.gender'))
set_key.add(telebot.types.InlineKeyboardButton('🔙 Вернуться назад', callback_data='sett.back'))
