"""Функция получает на вход список чисел.

Отсортируйте список по убыванию суммы цифр"""


def get_sum(num: int):
    return sum(map(int, str(num)))


lst = [75, 41, 80, 19, 16,1]


print(sorted(lst, key=get_sum, reverse=True))

# print(sorted(lst, key=(lambda x: sum(int, str(x)), [75, 41, 80, 19, 16,1]), reverse=True))