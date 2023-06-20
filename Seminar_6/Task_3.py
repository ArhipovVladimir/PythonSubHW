'''Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.'''

import random
from sys import argv

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

# argv = ['task.py', '1', '10', '5']

# использую срез [1:] списка argv так как в первый аргумент попадает имя модуля
min_lim, max_lim, level = map(int, argv[1:])
# print(min_lim, max_lim, level)
funk_round(min_lim, max_lim, level)

