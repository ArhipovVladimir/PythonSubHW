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
    # print(os.listdir())
    if file_mame in os.listdir():
        with open(file_mame, 'r', encoding='utf-8') as f1:
            dict_user = json.load(f1)
    else: dict_user = {}

    while True:

        user_name = input('введите имя пользователя')
        if not user_name:
                 break
        if not user_name.isalpha():
            print(f'в строке должны быть только буквы {user_name}')
            continue
        if not user_name.istitle():
            print(f' ФИО не с большой буквы {user_name}')
            continue

        try:
            user_id = int(input('введите id'))
        except ValueError as e:
            print(f'не число ошибка {e}')
            continue
        if user_id in dict_user.keys():
            print("идентификатор уже имеется")
            continue
        try:
            level_access = int(input('введите уровень через'))
        except ValueError as e:
            print(f'не число ошибка {e}')
            continue

        dict_user.setdefault(level_access, {user_id: user_name})[user_id] = user_name
        # dict_user.setdefault(level_access, [user_id, user_name])

    print(dict_user)
    with open(file_mame, 'w', encoding='utf-8') as f2:
        json.dump(dict_user, f2, ensure_ascii=False)

user_add('user_id_v1')