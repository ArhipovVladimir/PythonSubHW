"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import os
import json
import pickle


def find_json(dir_):

    files = [file for file in os.listdir(dir_) if file.endswith('.json')]

    for file in files:
        with(open(os.path.join(dir_, file), 'r', encoding='utf-8') as f,
             open(os.path.join(dir_, file.strip('.json') + '.picke'), 'wb') as f1
        ):
            pickle.dump(json.load(f), f1)


if __name__ == '__main__':
    find_json(os.getcwd())

