"""Задание №1
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль."""

import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
            'в строке {lineno:03d} функция "{funcName}()" ' \
            'в {created} секунд записала сообщение: {msg}'

# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'

logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.DEBUG, encoding='utf-8')
logger = logging.getLogger('main')
logger.debug("ошибка")

def div_(a, b):
    return a / b


if __name__ == '__main__':
    a, b = map(int, input("введите число").split(' '))
    print(a)
    print(b)
    print(div_(a, b))
