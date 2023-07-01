"""
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.

Задание №6
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.

"""

from Task_2 import funk_round
from Task_2 import verif
from Task_3 import save_json
from Task_4 import count_statr


@count_statr(2)
@save_json
@verif
def funk_start(*args):
    return funk_round(*args)

if __name__ == '__main__':
    funk_start(10, 3)

