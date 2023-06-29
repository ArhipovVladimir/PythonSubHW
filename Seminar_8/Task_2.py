"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться
"""
import json
import os


def user_add(file_mame):
    file_mame = f'{file_mame}.json'
    print(os.listdir())
    if file_mame in os.listdir():
        with open(file_mame, 'r') as f1:
            dict_user = json.load(f1)
    else: dict_user = {}

    while True:
        user_name = input('введите имя пользователя')
        if user_name == 'exit':
            break
        user_id = int(input('введите id'))
        if user_id in dict_user.keys():
            print("идентификатор уже имеется")
            continue
        level_access = int(input('введите уровень через'))
        dict_user.setdefault(user_id, [user_name, level_access])

    print(dict_user)
    with open(file_mame, 'a') as f2:
        json.dump(dict_user, f2, sort_keys=True, ensure_ascii=False)

user_add('user_id')