'''
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

'''


def rebus_todo(rebus_use, variant, level):
    print(f'загадка {rebus_use}')
    # print(f'варианты {variant}')
    count = 1
    while level > 0:

        resalt = input('введите ответ ')
        if resalt in variant:
            return count
        level -= 1
        count += 1
    return 0
