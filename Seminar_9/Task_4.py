"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.

"""

def param(count):
    def deco(func):
        res_list = []
        def wrapper(*args):
            for _ in range(count):
                res_list.append(func(args))
            return res_list
        return wrapper
    return deco

@param(5)
def my_func(*args):
    return args



if __name__ == '__main__':

    print(my_func('привет'))

