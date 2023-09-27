from app.services.types import equipment_catalog
import telebot
from app.services.names import equipment
from app.services import storage
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from app.services import get_all_brands, get_all_types, get_brand_current_names, \
    get_current_brands, get_current_names, get_manual_link
import json

keys = []
for key in equipment_catalog.keys():
    keys.append(key)
keys2 = []
for key in equipment.keys():
    keys2.append(key)
kol = 0


def all_types_keyboard() -> ReplyKeyboardMarkup:
    main_keyboard = ReplyKeyboardMarkup()
    types = get_all_types()
    for key in types:
        button = InlineKeyboardButton(text=type, callback_data=type)
        main_keyboard.row(button)
    main_keyboard.row("Меню")

    return main_keyboard


def all_brands_keyboard() -> ReplyKeyboardMarkup:
    main_keyboard = ReplyKeyboardMarkup()
    brands = get_all_brands()
    for brand in brands:
        button = InlineKeyboardButton(text=brand, callback_data=brand)
        main_keyboard.row(button)
    main_keyboard.row("Меню")

    return main_keyboard


def all_names_keyboard() -> ReplyKeyboardMarkup:
    main_keyboard = ReplyKeyboardMarkup()
    names = get_all_types()
    for name in names:
        button = InlineKeyboardButton(text=name, callback_data=name)
        main_keyboard.row(button)
    main_keyboard.row("Меню")

    return main_keyboard


def get_brands_keyboard() -> ReplyKeyboardMarkup:
    main_keyboard = telebot.types.ReplyKeyboardMarkup()
    brands = get_all_brands()
    for key in brands:
        button = telebot.types.InlineKeyboardButton(text=key)
        main_keyboard.row(button)
    main_keyboard.row("Меню")
    return main_keyboard


def get_second_brand_keybord(message) -> ReplyKeyboardMarkup:
    main_keyboard = telebot.types.ReplyKeyboardMarkup()
    names = get_brand_current_names(message)
    for key in names:
        button = telebot.types.InlineKeyboardButton(text=key)
        main_keyboard.row(button)
    main_keyboard.row("\U0001F519Назад")
    return main_keyboard


def gen_main_keyboard() -> ReplyKeyboardMarkup:
    main_keyboard = ReplyKeyboardMarkup()
    types = get_all_types()
    for type in types:
        button = telebot.types.InlineKeyboardButton(text=type, callback_data=type)
        main_keyboard.row(button)
    main_keyboard.row("Меню")

    return main_keyboard


def gen_search_keyboard(lis) -> InlineKeyboardMarkup:
    main_keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    for key in lis:
        button = telebot.types.InlineKeyboardButton(text=key, callback_data=key)
        main_keyboard.add(button)
    main_keyboard.add(telebot.types.InlineKeyboardButton(text="Меню", callback_data="menu"))

    return main_keyboard


def gen_second_keyboard(type) -> ReplyKeyboardMarkup:
    second_keyboard = telebot.types.ReplyKeyboardMarkup()
    brands = get_current_brands(type)
    with open('C:/Users/Георгий/PycharmProjects/pythonProject19/app/services/equipment.json', 'r',
              encoding='utf-8') as f:
        data = json.load(f)

    for brand in brands:
        button = telebot.types.InlineKeyboardButton(text=brand, callback_data=brand)
        second_keyboard.row(button)

    second_keyboard.row("\U0001F519Назад")

    return second_keyboard


def gen_third_keyboard(tg_id) -> ReplyKeyboardMarkup:
    costorage = storage.get_data(chat_id=tg_id, user_id=tg_id)
    type = costorage['type']
    brand = costorage['brand']
    names = get_current_names(type, brand)
    third_keyboard = telebot.types.ReplyKeyboardMarkup()

    for name in names:
        button = telebot.types.InlineKeyboardButton(text=name, callback_data=name)
        third_keyboard.row(button)

    third_keyboard.row("Новый запрос")
    third_keyboard.row("\U0001F519Назад")

    return third_keyboard


def get_info(tg_id):
    costorage = storage.get_data(chat_id=tg_id, user_id=tg_id)
    type = costorage['type']
    brand = costorage['brand']
    name = costorage['name']
    with open('C:/Users/Георгий/PycharmProjects/pythonProject19/app/services/equipment.json', 'r',
              encoding='utf-8') as f:
        data = json.load(f)
    for item in data["equipment"]:
        if item["type"] == type and item["brand"] == brand and item["name"] == name:
            s = str(item['settings'])
            s = s.replace(', ', '\n').replace('"', '').replace(" {", "\n").replace("{'", '').replace('}', "\n").replace(
                "'",
                "").replace(
                "Power", "\nPower")
            s = f"{name}\n{s}"
            return s.strip()


def get_info_brand(tg_id):
    costorage = storage.get_data(chat_id=tg_id, user_id=tg_id)
    brand = costorage['brand_type']
    name = costorage['brand_name']
    with open('C:/Users/Георгий/PycharmProjects/pythonProject19/app/services/equipment.json', 'r',
              encoding='utf-8') as f:
        data = json.load(f)
    for item in data["equipment"]:
        if item["brand"] == brand and item["name"] == name:
            s = str(item['settings'])
            s = s.replace(', ', '\n').replace('"', '').replace(" {", "\n").replace("{'", '').replace('}', "\n").replace(
                "'",
                "").replace(
                "Power", "\nPower")
            s = f"{name}\n{s}"
            return s.strip()


def get_manual_keyboard(name) -> InlineKeyboardMarkup | None:
    keyboard = InlineKeyboardMarkup()
    if get_manual_link(name) != None:
        button = InlineKeyboardButton("Мануал", url=get_manual_link(name))
        keyboard.add(button)
        return keyboard
    return None


def get_mail_keyboard() -> InlineKeyboardMarkup:
    main_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    send_button = telebot.types.InlineKeyboardButton(text='Отправить', callback_data="send")
    cancel_button = telebot.types.InlineKeyboardButton(text='Отменить', callback_data="cancel")
    change_button = telebot.types.InlineKeyboardButton(text='Изменить',
                                                       callback_data="change")

    main_keyboard.add(send_button)
    main_keyboard.add(cancel_button)
    main_keyboard.add(change_button)

    return main_keyboard
