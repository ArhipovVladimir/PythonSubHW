'''
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

'''
__all__ = ['_dict_resalt']

_dict_resalt = {}


def save_resalt(rebus_use, resalt_round):
    _dict_resalt[rebus_use] = resalt_round


def output_resalt():
    for item in _dict_resalt.items():
        print(f'загадка {item[0]} отгадана с {item[1]} попытки')


