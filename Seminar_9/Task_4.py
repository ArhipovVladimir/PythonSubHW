"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.

"""
COUNT = 3

def count_statr(count):
    def deco(func):
        res_list = []
        def wrapper(*args):
            for _ in range(count):
                res_list.append(func(*args))

        return wrapper
    return deco


@count_statr(3)
def my_func(*args):
    return args



if __name__ == '__main__':
    my_func('пот')

