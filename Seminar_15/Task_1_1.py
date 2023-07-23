import logging

# FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
#             'в строке {lineno:03d} функция "{funcName}()" ' \
#             'в {created} секунд записала сообщение: {msg}'

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'

logging.basicConfig(filename='log/log.txt', format=FORMAT, style='{', level=logging.ERROR, encoding='utf-8')
logger = logging.getLogger(__name__)


def div_(a, b):
    try:
       return a / b
    except ZeroDivisionError:
        logger.error('деление на 0')
        return 'inf'


if __name__ == '__main__':
    a, b = map(int, input("введите число").split(' '))
    print(div_(a, b))
