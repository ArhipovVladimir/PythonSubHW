"""
Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.

"""


def get_dict(dict_use, key, defalt):
    try:
        return dict_use[key]
    except KeyError:
        return defalt


if __name__ == '__main__':
    dct = {
        1: 'a',
        2: 'a',
        3: 'c',
        4: 'd'
    }

    get_dict(dct, 5, 'e')
    print(get_dict(dct, 4, 'f'))
    print(dct)
