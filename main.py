from bot.commands import *

while __name__ == '__main__':
    print('Да')
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass
