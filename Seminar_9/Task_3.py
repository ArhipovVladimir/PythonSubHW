"""Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции."""
import json
import os
from typing import Callable
from functools import wraps

def save_json(func):
    @wraps(func)
    def wrapper(num, *arg, **kwargs):
        filemame = f'{func.__name__}.json'
        print(filemame)
        if filemame in os.listdir():
            with open(filemame, 'r', encoding='utf-8') as f_json:
                list_file = json.load(f_json)
        else:
            list_file = []

        result = func(num, *arg, **kwargs)
        list_file.append({'args': (num, arg, kwargs), 'result': result})

        with open(filemame, 'w', encoding='utf-8') as f_json:
              json.dump(list_file, f_json, indent=1)

    return wrapper


@save_json
def get_sum(num, *arg, **kwargs):
    return num

if __name__ == '__main__':
    get_sum(1, 1, 1)

