"""Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging."""

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
import logging

# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
#             'в строке {lineno:03d} функция "{funcName}()" ' \
#             'в {created} секунд записала сообщение: {msg}'

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'

logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.DEBUG, encoding='utf-8')
logger = logging.getLogger('main')
logger.debug("ошибка")

def save_log(func):
    @wraps(func)
    def wrapper(num, *arg, **kwargs):

        result = func(num, *arg, **kwargs)
        logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.DEBUG, encoding='utf-8')
        logger = logging.getLogger('main')
        logger.debug({'args': (num, arg, kwargs), 'result': result})


    return wrapper


@save_log
def get_sum(num, *arg, **kwargs):
    return num

if __name__ == '__main__':
    get_sum(1, 2, 3)

