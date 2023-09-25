import telebot
bot = telebot.TeleBot('5956975897:AAG9deyfFYO03yv8eWqrW9wubdWJdKLAE9E')
from app.handlers import *
if __name__ == '__main__':
    bot.set_chat_menu_button()
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Запуск бота"),
    ])

    bot.polling(none_stop=True)
