'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

'''


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


if __name__ == '--main__':

    while True:
        dd, mm, yyyy = map(int, input('введите дату в формае DD.MM.YYYY в диапазоне [1, 9999]: ').split('.'))
        if 1 < yyyy <= 9999:
            break

    if check_date(dd, mm, yyyy):
        print('дата может существовать')
    print('дата не возможна')

