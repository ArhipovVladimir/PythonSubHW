'''
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

'''
import random


def funk_round(min_lim, max_lim, level):
    digit = random.randint(min_lim, max_lim)
    while level > 0:
        print(f'Веедите число между {min_lim} и {max_lim} у Вас {level} попыток')
        num = int(input())
        if num < min_lim or num > max_lim:
            print(f'Число {num} не в границах интервала {min_lim} {max_lim}')
            level -= 1
        elif num < digit:
            print(f'Число {num} меньше загаданного')
            level -= 1
        elif num > digit:
            print(f'Число {num} больше загаданного')
            level -= 1
        else:
            print(f'правильно компьютер загадывал {num}')
            return True

    else:
        print(f' колическо попыток ичерпано - компьютер загадывал {digit}')
        return False


min_lim, max_lim, level = map(int, input('Enter min_lim, max_lim, level: ').split())
funk_round(min_lim, max_lim, level)

