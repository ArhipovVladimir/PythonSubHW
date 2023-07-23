"""Задание №5
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""

from datetime import datetime
import logging
import argparse


week_day = {'понедельник': 0,
            'вторник': 1,
            'среда': 2,
            'четверг': 3,
            'пятница': 4,
            'суббота': 5,
            'воскресенье': 6}

dict_monat = {'января': 1,
              'февраля': 2,
              'марта': 3,
              'апреля': 4,
              'мая': 5,
              'июня': 6,
              'июля': 7,
              'августа': 8,
              'сентября': 9,
              'октября': 10,
              'ноября': 11,
              'декабря': 12}

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'

logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def get_date(*args):
    try:
        d, w, m, = args
        if d >= 6:
            logger.error('не верный ввод')
    except Exception:
        logger.error('не верный ввод')

    d = int(d.strip("-й"))
    try:
        weekday = week_day[w]
        month_ = dict_monat[m]
    except KeyError:
        logger.error('не верный ввод')
    count = 0
    for day in range(1, 32):
        try:
            data_res = datetime(datetime.now().year, month_, day)
        except UnboundLocalError:
            logger.error('не верный ввод')
        try:
            if data_res.weekday() == weekday and count != d:
                count += 1
            if data_res.weekday() == weekday and count == d:
                return data_res
        except Exception as e:
            logger.error(f'не номер дня недели {e}')
            return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('-d', metavar='day', type=str,
                        help='number day', default=1)
    parser.add_argument('-w', metavar='weekday', type=str,
                        help='week day', default=datetime.now().weekday())
    parser.add_argument('-m', metavar='month', type=str,
                        help='month', default=datetime.now().month)
    args = parser.parse_args()
    print(get_date(args.d, args.w, args.m))

    # print(get_date('5-й четверг марта'))