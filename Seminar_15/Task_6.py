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
import argparse
from sys import argv

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



def dir_write(dir_=os.getcwd()):
    os.chdir(dir_)
    # print(dir_)
    list_obj = []
    for obj in os.listdir(os.getcwd()):
        # print(obj)
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
    parser = argparse.ArgumentParser(description='dir info')
    parser.add_argument('args', metavar='path', type=str, help='get dir path', default=os.getcwd())
    args = parser.parse_args()
    # print(args)
    # dir_write(args)
    # dir_write()
    # dir_write('C:\\Users\\arhip\\OneDrive\\Документы\\GB\\Python2\\PythonSubHW\\Seminar_9')
    print(args.args)
    # _, args = argv
    dir_write(args.args)

