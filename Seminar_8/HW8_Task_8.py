"""Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
ля файлов сохраните его размер в байтах, а для директорий размер файлов
в ней с учётом всех вложенных файлов и директорий.

Соберите из созданных на уроке и в рамках домашнего задания функций пакет
для работы с файлами разных форматов."""
import json
import os
import pickle
import sys


def walk_write(dir_):
    res_list = []
    for patch_, dir_names, file_names in os.walk(dir_):
        # print(patch_, dir_names, file_names )
        dict_dir_file = {}
        if len(dir_names) != 0:

            for dir_name in dir_names:
                dict_dir_file.setdefault("dir", {dir_name}).add(dir_name)
                dict_dir_file.setdefault("patch", {patch_}).add(patch_)

        if len(file_names) != 0:
            for file_name in file_names:
                dict_dir_file.setdefault("File", {file_name}).add(file_name)
                dict_dir_file.setdefault("size", {os.path.getsize(os.path.join(patch_, file_name))})\
                    .add(os.path.getsize(os.path.join(patch_, file_name)))
                dict_dir_file.setdefault("patch", {patch_}).add(patch_)

        # print(dict_dir_file)

    with(
        open('dict_dir_file.json', 'w', encoding='utf-8') as f_json,
        open('dict_dir_file.pickle', 'wb') as f_pic,
    ):
        # json.dump(dict_dir_file, f_json)
        pickle.dump(dict_dir_file, f_pic)


if __name__ == '__main__':
    walk_write('C:\\Users\\arhip\\OneDrive\\Документы\\GB\\Python2\\PythonSubHW\\Siminar_7')