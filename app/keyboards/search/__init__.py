from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import json


def search_info(name):
    with open('app/services/equipment.json', 'r',
              encoding='utf-8') as f:
        data = json.load(f)
    for item in data["equipment"]:
        if item["name"] == name:
            s = str(item['settings'])
            s = s.replace(', ', '\n').replace('"', '').replace(" {", "\n").replace("{'", '').replace('}', "\n").replace(
                "'",
                "").replace(
                "Power", "\nPower")
            s = f"{name}\n{s}"
            return s


def gen_search_keyboard(lis) -> InlineKeyboardMarkup:
    main_keyboard = InlineKeyboardMarkup(row_width=1)
    for key in lis:
        button = InlineKeyboardButton(text=key, callback_data=key)
        main_keyboard.add(button)
    main_keyboard.add(InlineKeyboardButton(text="Меню", callback_data="menu"))

    return main_keyboard
