import telebot

storage = telebot.StateMemoryStorage()
auth_storage = telebot.StateMemoryStorage()


def get_all_id():
    with open("info.log", "r") as log_file:
        data = log_file.readlines()
        users_id = []
        for user_id in data:
            # Извлекаем ID пользователя из строки лога
            user_id = user_id.strip().split("]:")[1].strip().split(" ")[1]
            users_id.append(user_id)
    return (set(users_id))


# Для отправки рассылки вызовите функцию send_message_to_all_users()
import json


def get_all_types():
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    types = []

    for item in data["equipment"]:
        current_type = item["type"]

        types.append(current_type)
    new_list = []

    for el in types:
        if el not in new_list:
            new_list.append(el)
    return new_list


def get_all_brands():
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    brands = []

    for item in data["equipment"]:
        current_brand = item["brand"]

        brands.append(current_brand)
    new_list = []

    for el in brands:
        if el not in new_list:
            new_list.append(el)
    return new_list


def get_current_brands(type):
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    brands = []

    for item in data["equipment"]:
        if type == item["type"]:
            brand = item["brand"]
            brands.append(brand)
            new_list = []

    for el in brands:
        if el not in new_list:
            new_list.append(el)
    return new_list


def get_current_names(type, brand):
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    names = []

    for item in data["equipment"]:
        if type == item["type"] and brand == item["brand"]:
            name = item["name"]

            names.append(name.strip())


    new_list = []

    for el in names:
        if el not in new_list:
            new_list.append(el)
    return new_list
def get_brand_current_names(brand):
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    names = []

    for item in data["equipment"]:
        if brand == item["brand"]:
            name = item["name"]

            names.append(name.strip())
    new_list = []

    for el in names:
        if el not in new_list:
            new_list.append(el)
    return new_list



def get_all_names():
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    names = []

    for item in data["equipment"]:
        current_name = item["name"]
        names.append(current_name)
    new_list = []

    for el in names:
        if el not in new_list:
            new_list.append(el)
    return new_list

def get_manual_link(name):
    with open('equipment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data["equipment"]:
        if name == item["name"]:
            if "*" != item["manual"]:
                return item["manual"]
            else :
                return None
    return None

