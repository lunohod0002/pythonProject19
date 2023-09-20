from app.services.dict import equipment_catalog
import telebot
from app.services.dict2 import equipment
from app.services import storage
from telebot.types import ReplyKeyboardRemove,ReplyKeyboardMarkup,InlineKeyboardMarkup
keys=[]
for key in equipment_catalog.keys():
    keys.append(key)
keys2=[]
for key in equipment.keys():
    keys2.append(key)
kol=0
def gen_first_keyboard()->InlineKeyboardMarkup:
    main_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2,)
    second=telebot.types.InlineKeyboardButton(text='Поиск \U0001F50E',callback_data="search")
    firt=telebot.types.InlineKeyboardButton(text='Каталог \U0001F4D6',callback_data="catalog")
    main_keyboard.add(firt)
    main_keyboard.add(second)
    return main_keyboard
def gen_main_keyboard()->ReplyKeyboardMarkup:
    main_keyboard = telebot.types.ReplyKeyboardMarkup()
    for key in equipment_catalog.keys():
        button = telebot.types.InlineKeyboardButton(text=key, callback_data=key, state=key)
        main_keyboard.row(button)
    return main_keyboard
def gen_search_keyboard(lis)->InlineKeyboardMarkup:
    main_keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    for key in lis:

        button = telebot.types.InlineKeyboardButton(text=key, callback_data=key)
        main_keyboard.add(button)
    main_keyboard.add(telebot.types.InlineKeyboardButton(text="Меню", callback_data="menu"))

    return main_keyboard

def gen_second_keyboard(message)->ReplyKeyboardMarkup:
    dic1=equipment_catalog[message]
    second_keyboard = telebot.types.ReplyKeyboardMarkup()
    for key in dic1.keys():
        button = telebot.types.InlineKeyboardButton(text=key, callback_data=message+";"+key, state=message+";"+key)
        second_keyboard.row(button)
    second_keyboard.row("\U0001F519Назад")

    return second_keyboard

def gen_third_keyboard(tg_id) ->ReplyKeyboardMarkup:
    costorage=storage.get_data(chat_id=tg_id,user_id=tg_id)
    dic1=equipment_catalog[costorage['type']][costorage['brand']]
    second_keyboard = telebot.types.ReplyKeyboardMarkup()
    for key in dic1.keys():
        button = telebot.types.InlineKeyboardButton(text=key, callback_data=key)
        second_keyboard.row(button)
    second_keyboard.row("Новый запрос")
    second_keyboard.row("\U0001F519Назад")

    return second_keyboard

def get_info(tg_id):
    costorage=storage.get_data(chat_id=tg_id,user_id=tg_id)
    dic1=equipment_catalog[costorage['type']][costorage['brand']][costorage['name']]
    s = str(dic1)
    s = s.replace(', ', '\n').replace('"', '').replace(" {","\n").replace("{'", '').replace('}', "\n").replace("'", "").replace("Power","\nPower")
    s=" "+s
    return s
def search_info(s):
    dic1=equipment[s]
    s = str(dic1)
    s = s.replace(', ', '\n').replace('"', '').replace(" {","\n").replace("{'", '').replace('}', "\n").replace("'", "")
    s=" "+s
    return s