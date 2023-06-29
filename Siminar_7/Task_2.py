"""
Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint
MIN_LEN = 4
MAX_LEN = 7
START_INDEX_CHR = 97
END_INDEX_CHR = 122

def get_name_file(count_name, name):
    # map(lambda x: x = chr(randint(97, 122)) for _ in range(len_name_file))
    for _ in range(count_name):
        len_name_file = randint(MIN_LEN, MAX_LEN)
        str_name = ''
        for _ in range(len_name_file):
            str_name += chr(randint(START_INDEX_CHR, END_INDEX_CHR))
        str_name = str_name.capitalize()

        with open(f'{name}', 'a') as f:
            f.writelines(f'{str_name}\n')


if __name__ == '__main__':
    get_name_file(20, 'file_name.txt')