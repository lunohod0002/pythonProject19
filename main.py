import telebot
from app.config import token,admin_id
bot = telebot.TeleBot(token)
from app.handlers import *
if __name__ == '__main__':
    bot.set_chat_menu_button()
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Запуск бота"),
    ])

    bot.polling(none_stop=True)
