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

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'


def save_log(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):

        result = func(*arg, **kwargs)
        logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.DEBUG, encoding='utf-8')
        logger = logging.getLogger(func.__name__)
        logger.debug({'args': (arg, kwargs), 'result': result})
    return wrapper


@save_log
def get_sum(*arg, **kwargs):
    return sum(arg)

if __name__ == '__main__':
    get_sum(1, 2, 3)