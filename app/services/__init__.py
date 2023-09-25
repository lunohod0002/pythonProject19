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

