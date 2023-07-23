"""
Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.

"""
from functools import wraps
import logging

FORMAT = '{asctime} {levelname}: {msg}'
logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger()


def save_log(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):

        result = func(**kwargs)
        logger.info(f'{func.__name__} args: {kwargs}, result {result}')
    return wrapper


@save_log
def get_sqr(**kwargs):
        a, b, c = map(int, kwargs.values())
        if a == 0:
            return 0, 0
        diskrim = b ** 2 - 4 * a * c
        x1 = (- b + (diskrim ** 0.5)) / (2 * a)
        x2 = (- b - (diskrim ** 0.5)) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    get_sqr(a=1, b=2, c=3)
    get_sqr(a=2, b=2, c=3)
    get_sqr(a=0, b=2, c=3)