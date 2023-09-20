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
keys=[]
for key in equipment_catalog.keys():
    keys.append(key)
keys2=[]
for key in equipment.keys():
    keys2.append(key)
kol=0


@bot.message_handler(commands=['start'])
def start(message:Message):
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать",  reply_markup=gen_first_keyboard())

    storage.reset_data(chat_id=message.chat.id, user_id=message.from_user.id)
    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                      state='choose_button')
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Запуск бота")
    ])
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
        if call.data== 'catalog':
            bot.send_message(call.from_user.id, "Выберите тип прибора",
                             reply_markup=gen_main_keyboard())
            storage.reset_data(chat_id=call.message.chat.id, user_id=call.from_user.id)

            storage.set_state(chat_id=call.message.chat.id, user_id=call.from_user.id, state='choose_type')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        elif call.data== 'search':
            bot.send_message(call.from_user.id, "Введите название прибора",
                             reply_markup=ReplyKeyboardRemove())
            storage.reset_data(chat_id=call.message.chat.id, user_id=call.from_user.id)

            storage.set_state(chat_id=call.message.chat.id, user_id=call.from_user.id, state='search')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        elif call.data in keys2:
            (call.data)
            bot.send_message(call.from_user.id, search_info(call.data))
            storage.reset_data(chat_id=call.message.chat.id, user_id=call.from_user.id)

            storage.set_state(chat_id=call.message.chat.id, user_id=call.from_user.id, state='search')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        elif call.data =="menu":
            (storage.get_data(chat_id=call.message.chat.id, user_id=call.from_user.id).keys())

            bot.send_message(call.from_user.id, "Привет! Нажми на кнопку, чтобы начать",  reply_markup=gen_first_keyboard())
            storage.reset_data(chat_id=call.message.chat.id, user_id=call.from_user.id)

            storage.set_state(chat_id=call.message.chat.id, user_id=call.from_user.id, state='choose_button')
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
@bot.message_handler(content_types=['text'])
def booking(message):
    try:
        match storage.get_state(chat_id=message.chat.id, user_id=message.from_user.id) :
            case 'search':
                if (len(message.text)> 2):
                    lis=list()
                    s=message.text.lower
                    main_keyboard = telebot.types.ReplyKeyboardMarkup()
                    for i in range(0,len(keys3)):
                        if message.text.lower() in keys3[i].lower():
                            lis.append(keys2[i])
                    if len(lis)==0:
                        bot.send_message(message.chat.id, "Название не найдено", reply_markup=gen_search_keyboard(lis))
                    else:
                        bot.send_message(message.chat.id,text= f"Найдено {len(lis)} совпадений",reply_markup=gen_search_keyboard(lis))
                        storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                              state='search')

                else :
                    bot.send_message(message.chat.id, "Название должно быть длинее 2 символов")

            case 'search_info':
                for item in keys2:
                    if message.text.lower() in item.lower():
                        bot.send_message(message.chat.id, search_info(message.text))
                        storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                  state='search')
                        storage.reset_data(chat_id=message.chat.id, user_id=message.from_user.id)

            case 'choose_type':
                if (message.text in equipment_catalog.keys()) :
                    bot.send_message(message.chat.id, "Выбери бренд прибора", reply_markup=gen_second_keyboard(message.text))
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_brand')
                    storage.set_data(chat_id=message.chat.id, user_id=message.from_user.id,
                                      key='type',value=message.text)
                else:
                    bot.send_message(message.chat.id, "Ошибка. Поробуй еще раз")
            case 'choose_brand':
                if (message.text in equipment_catalog[storage.get_data(chat_id=message.chat.id, user_id=message.from_user.id)['type']]):
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_name')
                    storage.set_data(chat_id=message.chat.id, user_id=message.from_user.id,
                                     key='brand', value=message.text)
                    bot.send_message(message.chat.id, "Выбери название прибора", reply_markup=gen_third_keyboard(message.from_user.id))
                elif (message.text=='\U0001F519Назад'):
                    bot.send_message(message.chat.id, "Выбери тип прибора",
                                     reply_markup=gen_main_keyboard())

                    storage.reset_data(chat_id=message.chat.id, user_id=message.from_user.id)
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_type')
                else :
                    bot.send_message(message.chat.id, "Бренд не найден. Попробуй еще раз")
            case 'choose_name':
                if (message.text in equipment_catalog[storage.get_data(chat_id=message.chat.id, user_id=message.from_user.id)['type']]
                [storage.get_data(chat_id=message.chat.id, user_id=message.from_user.id)['brand']]):
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_name')
                    storage.set_data(chat_id=message.chat.id, user_id=message.from_user.id,
                                     key='name', value=message.text)
                    bot.send_message(message.chat.id, get_info(message.from_user.id))
                elif (message.text=='Новый запрос'):
                    bot.send_message(message.chat.id, "Выбери тип прибора",
                                     reply_markup=gen_main_keyboard())
                    storage.reset_data(chat_id=message.chat.id, user_id=message.from_user.id)
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_type')
                elif (message.text=='\U0001F519Назад'):
                    bot.send_message(message.chat.id, "Выбери бренд прибора",
                                     reply_markup=gen_second_keyboard(storage.get_data(chat_id=message.chat.id, user_id=message.from_user.id)['type']))
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_brand')
                else:
                    bot.send_message(message.chat.id, "Название не найдено. Поробуй еще раз")
            case 'complete':
                if (message.text=='Новый запрос'):
                    bot.send_message(message.chat.id, "Выбери тип прибора",
                                     reply_markup=gen_main_keyboard())
                    storage.reset_data(chat_id=message.chat.id, user_id=message.from_user.id)
                    storage.set_state(chat_id=message.chat.id, user_id=message.from_user.id,
                                      state='choose_type')

    except Exception as e:
        (e)
        bot.send_message(message.chat.id, "Попробуй ещё раз")
bot.set_chat_menu_button()

bot.polling(none_stop=True)