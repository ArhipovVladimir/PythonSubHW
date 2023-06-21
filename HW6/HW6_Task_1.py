'''
Решить задачи, которые не успели решить на семинаре.

В модуль с проверкой даты добавьте возможность запуска в
терминале с передачей даты на проверку.
'''

from sys import argv

def check_day(dd, mm, yyyy):
    list_monat = [1, 3, 5, 7, 8, 10, 12]
    if dd > 31:
        return False
    elif dd == 31 and mm not in list_monat:
        return False
    elif dd == 29 and mm == 2:
        if _check_yare(yyyy):
            return True
        return False
    return True


def check_monat(mm):
    if mm > 12:
        return False
    return True


def _check_yare(yyyy):
    if yyyy % 4 != 0:
        return False
    elif yyyy % 100 == 0:
        if yyyy % 400 == 0:
            return True
        return False
    else:
        return True


def check_date(dd, mm, yyyy):
    return all([check_day(dd, mm, yyyy), check_monat(mm)])


if __name__ == '__main__':

    while True:
        # argv = ['dddcs', '23.01.2023']
        # print(argv)
        # min_lim, max_lim, level = map(int, map(str, argv[1:]))

        dd, mm, yyyy = (map(int, argv[1:]))
        print(dd, mm, yyyy)
        if 1 < yyyy <= 9999:
            break

    if check_date(dd, mm, yyyy):
        print('дата может существовать')
    else:
        print('дата не возможна')

