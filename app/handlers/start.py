import telebot
import datetime
from datetime import datetime
from telebot.types import Message
from app.services import storage
from app.keyboards.start import admin_start_keybooard,user_start_keyboard
from main import bot,admin_id


@bot.message_handler(commands=['start'])
def start(message: Message):
    if message.chat.id == int(admin_id):
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать",
                         reply_markup=admin_start_keybooard())
    else:
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать",
                         reply_markup=user_start_keyboard())

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
