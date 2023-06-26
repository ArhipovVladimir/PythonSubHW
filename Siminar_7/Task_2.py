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

def get_name_file():
    len_name_file = randint(MIN_LEN, MAX_LEN + 1)
    str_name = ''
    # map(lambda x: x = chr(randint(97, 122)) for _ in range(len_name_file))
    for _ in range(len_name_file):
        str_name += chr(randint(97, 122))

    str_name=str_name.capitalize()

    with open('file_name.txt', 'a') as f:
        f.write(f'{str_name}\n')






get_name_file()