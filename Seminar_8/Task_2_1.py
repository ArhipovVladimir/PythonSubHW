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


def user_add_json(file_mame):
    file_mame = f'{file_mame}.json'
    print(os.listdir())
    if file_mame in os.listdir():
        with open(file_mame, 'r', encoding='utf-8') as f1:
            dict_user = json.load(f1)
    else: dict_user = {str(i): {} for i in range(1, 8)}

    while True:
        data = input('введите имя пользователя')
        if not data:
            break

        user_name, user_id, access = data.split()

        if user_id in dict_user[access]:
            print("id дублируется")
            continue

        dict_user.setdefault(access, {user_id: user_name})[user_id] = user_name

    with open(file_mame, 'w', encoding='utf-8') as f2:
        json.dump(dict_user, f2, ensure_ascii=False)


if __name__ == '__main__':
    user_add_json('user_id')