'''
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''


from random import randint, uniform
MIN_NUM = -1000
MAX_NUM = 1000


def get_file(count_str, name_file):
    with open(name_file, 'w') as f:
        for _ in range(count_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)}|'
                         f'{uniform(MIN_NUM ,MAX_NUM)}\n')



if __name__ == '__main__':
    get_file(20, 'file_num.txt')