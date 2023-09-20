from app.services.dict import equipment_catalog
import telebot
from telebot.types import ReplyKeyboardRemove,Message
from app.services.dict2 import equipment
from app.services import storage
from app.services.keys import keys3
from app.configs import token
from app.keyboards import gen_main_keyboard,gen_search_keyboard,gen_first_keyboard,\
    gen_second_keyboard,gen_third_keyboard,get_info,search_info
bot = telebot.TeleBot(token)
from app.handlers import *
if __name__ == '__main__':
    bot.set_chat_menu_button()
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Запуск бота")
    ])

    bot.polling(none_stop=True)
