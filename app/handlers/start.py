import telebot
import datetime
from datetime import datetime
from telebot.types import ReplyKeyboardRemove, Message
from app.services import storage, auth_storage
from app.keyboards import gen_main_keyboard, gen_search_keyboard, user_start_keyboard, admin_start_keybooard
from main import bot


@bot.message_handler(commands=['start'])
def start(message: Message):

        if message.chat.id == 153559013:
            bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать",
                             reply_markup=admin_start_keybooard())
        else:
            bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать",
                             reply_markup=admin_start_keybooard())


        log_file = open("info.log", "a")
        log_file.write(
            f"\n[INFO {datetime.now()}]: {message.from_user.username} {message.chat.id}")
        log_file.close()
        storage.reset_data(chat_id=message.chat.id, user_id=message.from_user.id)
        storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                          state='choose_button')
        bot.set_my_commands([
            telebot.types.BotCommand("/start", "Запуск бота")
        ])
