# - *- coding: utf- 8 - *-
import time
from datetime import datetime


# Очистка текста от HTML тэгов
def clear_html(get_text):
    if "<" in get_text: get_text = get_text.replace("<", "*")
    if ">" in get_text: get_text = get_text.replace(">", "*")

    return get_text


# Получение текущего unix времени
def get_unix():
    return int(time.time())


# Получение текущей даты
def get_date():
    this_date = datetime.now().replace(microsecond=0)
    this_date = this_date.strftime("%d.%m.%Y %H:%M:%S")

    return this_date


# Разбив списка по количеству переданных значений
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Очистка мусорных символов из списка
def clear_list(get_list: list):
    while "" in get_list:
        get_list.remove("")

    while " " in get_list:
        get_list.remove(" ")

    while "," in get_list:
        get_list.remove(",")

    while "\r" in get_list:
        get_list.remove("\r")

    return get_list


# Удаление отступов у текста
def ded(get_text: str):
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)

    return get_text



# Конвертация дней
def convert_day(day):
    day = int(day)
    days = ['день', 'дня', 'дней']

    if day % 10 == 1 and day % 100 != 11:
        count = 0
    elif 2 <= day % 10 <= 4 and (day % 100 < 10 or day % 100 >= 20):
        count = 1
    else:
        count = 2

    return f"{day} {days[count]}"
