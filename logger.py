import datetime
from datetime import datetime
import telebot.types


def loogger_do(msg: telebot.types.Message):
    current_time = datetime.now()
    data = str(current_time)
    with open("log.txt", "a", encoding='utf-8') as file_data:
        file_data.write(f'{data} {": "} Пользователь ({msg.from_user.id}) прислал сообщение: {msg.text}\n')


def logger(msg, command, res):
    current_time = datetime.now()
    data = str(current_time)
    with open("log.txt", "a", encoding='utf-8') as file_data:
        file_data.write(f'{data} {", "} {msg} {", "} {command} {", "} {res}\n')