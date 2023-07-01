"""Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в
функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов."""

from typing import Callable
from random import randint


def verif(funk):
    def wrapper(digit, level):

        if not 1 <= digit <= 100:
            digit = randint(1, 100)
            print('будут использованны случайные числа угадывания')
        if not 1 <= level <= 10:
            level = randint(1, 10)
            print('будут использованны случайные числа попыток')

        return funk(digit, level)

    return wrapper


# @verif
def funk_round(digit, level):
    att = 0
    while att < level:
        print(f'Веедите число между {1} и {100} у Вас {level} попыток')
        num = int(input())
        att += 1
        if num < 1 or num > 100:
            print(f'Число {num} не в границах интервала {1} {100}')

        elif num < digit:
            print(f'Число {num} меньше загаданного')

        elif num > digit:
            print(f'Число {num} больше загаданного')

        else:
            print(f'правильно компьютер загадывал {num}')
            return True

    else:
        print(f' колическо попыток ичерпано - компьютер загадывал {digit}')
        return False


if __name__ == '__main__':
    number = 5
    attc = 9
    print(funk_round.__name__)
    funk_round = verif(funk_round)
    print(funk_round.__name__)
    funk_round(number, attc)



