"""
Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_num(text):

    while True:
        data = input(text)
        try:
            return int(data)
        except ValueError as e:
            try:
                return float(data)
            except ValueError as e:
                print(f'не число ошибка {e}')


if __name__ == '__main__':
    number = get_num('введите число ')
    print(number)

