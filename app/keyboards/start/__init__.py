from app.services.types import equipment_catalog
from app.services.names import equipment
from telebot.types import  InlineKeyboardMarkup,InlineKeyboardButton

keys = []
for key in equipment_catalog.keys():
    keys.append(key)
keys2 = []
for key in equipment.keys():
    keys2.append(key)
kol = 0
def user_start_keyboard() -> InlineKeyboardMarkup:
    main_keyboard = InlineKeyboardMarkup(row_width=3)
    search_button = InlineKeyboardButton(text='Поиск \U0001F50E', callback_data="search")
    types_button = InlineKeyboardButton(text='Каталог \U0001F4D6', callback_data="catalog_types")
    brand_button = InlineKeyboardButton(text='Каталог брендов \U0001F4D6', callback_data="catalog_brands")

    main_keyboard.add(types_button)
    main_keyboard.add(brand_button)
    main_keyboard.add(search_button)

    return main_keyboard


def admin_start_keybooard() -> InlineKeyboardMarkup:
    main_keyboard = InlineKeyboardMarkup(row_width=3)
    search_button = InlineKeyboardButton(text='Поиск \U0001F50E', callback_data="search")
    types_button = InlineKeyboardButton(text='Каталог \U0001F4D6', callback_data="catalog_types")
    brand_button = InlineKeyboardButton(text='Каталог брендов \U0001F4D6', callback_data="catalog_brands")
    mail_button = InlineKeyboardButton(text='Отправить рассылку \U0001F4E7', callback_data="mail")

    main_keyboard.add(types_button)
    main_keyboard.add(brand_button)
    main_keyboard.add(search_button)
    main_keyboard.add(mail_button)

    return main_keyboard

