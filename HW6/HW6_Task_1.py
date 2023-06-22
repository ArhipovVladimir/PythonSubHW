'''
Решить задачи, которые не успели решить на семинаре.

В модуль с проверкой даты добавьте возможность запуска в
терминале с передачей даты на проверку.
'''

from sys import argv

def check_day(day, month, yare):
    list_monat = [1, 3, 5, 7, 8, 10, 12]
    if day > 31:
        return False
    elif day == 31 and month not in list_monat:
        return False
    elif day == 30 and month == 2:
        return False
    elif day == 29 and month == 2:
        if _check_yare(yare):
            return True
        return False
    return True


def check_monht(mm):
    if mm > 12:
        return False
    return True


def _check_yare(yare):
    return yare % 4 != 0 or yare % 100 == 0 and yare % 400 != 0

    # if yare % 4 != 0:
    #     return False
    # elif yare % 100 == 0:
    #     if yare % 400 == 0:
    #         return True
    #     return False
    # else:
    #     return True


def check_date(day, month, yare):
    return all([check_day(day, month, yare), check_monht(month)])


if __name__ == '__main__':
    _, *params = argv
    day, month, yare = map(int, str(params[0]).split('.'))
    print(day, month, yare)

    while True:
        if 1 < yare <= 9999:
             break
        day, month, yare = map(int, input('введите дату в формате DD.MM.YYYY в диапазоне [1, 9999]: ').split('.'))


    if check_date(day, month, yare):
        print('дата может существовать')
    else:
        print('дата не возможна')

