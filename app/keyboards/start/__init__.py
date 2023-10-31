from telebot.types import  InlineKeyboardMarkup,InlineKeyboardButton


def user_start_keyboard() -> InlineKeyboardMarkup:
    main_keyboard = InlineKeyboardMarkup(row_width=3)
    search_button = InlineKeyboardButton(text='\U0001F50E Поиск', callback_data="search")
    types_button = InlineKeyboardButton(text='\U0001F4D6 Каталог', callback_data="catalog_types")
    brand_button = InlineKeyboardButton(text='\U0001F4D6 Каталог по брендам', callback_data="catalog_brands")

    main_keyboard.add(types_button)
    main_keyboard.add(brand_button)
    main_keyboard.add(search_button)

    return main_keyboard


def admin_start_keybooard() -> InlineKeyboardMarkup:
    main_keyboard = InlineKeyboardMarkup(row_width=3)
    search_button = InlineKeyboardButton(text='\U0001F50E Поиск', callback_data="search")
    types_button = InlineKeyboardButton(text='\U0001F4D6Каталог', callback_data="catalog_types")
    brand_button = InlineKeyboardButton(text='\U0001F4D6 Каталог по брендам ', callback_data="catalog_brands")
    mail_button = InlineKeyboardButton(text='\U0001F4E7 Отправить рассылку ', callback_data="mail")

    main_keyboard.add(types_button)
    main_keyboard.add(brand_button)
    main_keyboard.add(search_button)
    main_keyboard.add(mail_button)

    return main_keyboard

