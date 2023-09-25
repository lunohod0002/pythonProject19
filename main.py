import telebot
bot = telebot.TeleBot('6396475143:AAENCBa4wUJ4eUJ-tkE0R2T-vWQYPljx6kI')
from app.handlers import *
if __name__ == '__main__':
    bot.set_chat_menu_button()
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Запуск бота"),
    ])

    bot.polling(none_stop=True)
