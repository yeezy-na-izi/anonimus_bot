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
