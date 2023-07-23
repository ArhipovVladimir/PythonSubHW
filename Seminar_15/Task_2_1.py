"""Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging."""


from functools import wraps
import logging

# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
#             'в строке {lineno:03d} функция "{funcName}()" ' \
#             'в {created} секунд записала сообщение: {msg}'

FORMAT = '{asctime} {levelname} {funcName}: {msg}'
logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def save_log(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):

        result = func(**kwargs)
        logger.info({'args': (kwargs), 'result': result})
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