"""
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный
 случайные  варианты и выведите 4 успешных расстановки."""

from random import randint
__all__ = ['get_pozis']


def get_pozis(size=8):
    list_posis = []
    for i in range(size):
        list_posis.append([randint(1, size), randint(1, size)])
    return list_posis


if __name__ == '__main__':
    print(get_pozis())
