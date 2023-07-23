"""Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import os
import logging
from collections import namedtuple

# class Project:
#
#     def __init__(self, list_user):
#         self.list_user = list_user
#
#
#
#     @classmethod
#     def load_json (cls, json_file):
#             list_user = []
#             with open(json_file, 'r', encoding='utf-8') as f_read:
#                 user_dict = json.load(f_read)
#
#             for level, in user_dict:
#                 for user_id in user_dict[level]:
#                     list_user.append(User(user_dict[level][user_id], user_id, level))
#
#             return Project(list_user)

FORMAT = '{msg}'

logging.basicConfig(filename='log/log1.txt', format=FORMAT, style='{', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)
Object_dir = namedtuple('Object', ['name', 'exemp', 'is_dir', 'path'])



def dir_write(dir_list=os.listdir()):
    list_obj = []
    for obj in dir_list:
        if os.path.isdir(obj):
            logger.info(f'{obj} {None} {os.path.isdir(obj)} {os.getcwd()}')
            list_obj.append(Object_dir(obj, None, os.path.isdir(obj), os.getcwd()))
        if os.path.isfile(obj):
            obj, exem = obj.split('.')
            logger.info(f'{obj} {exem} {os.path.isdir(obj)} {os.getcwd()}')
            list_obj.append(Object_dir(obj, exem, os.path.isdir(obj), os.getcwd()))

    print(list_obj)
        # print(f'{os.path.isdir(obj) = }', end='\t')
        # print(f'{os.path.isfile(obj) = }', end='\t')
        # print(f'{os.path.islink(obj) = }', end='\t')
        # print(f'{obj = }')


if __name__ == '__main__':
    dir_write()