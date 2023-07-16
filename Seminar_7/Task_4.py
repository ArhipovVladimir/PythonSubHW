"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

"""
import os
from random import randint, choices
from string import ascii_letters, digits

START_INDEX_CHR = 97
END_INDEX_CHR = 122

def ctreate_file(type_file, min_name=6, max_name=8, min_byte=256, max_byte=4096, count_file=0):

    for _ in range(count_file):
        len_name_file = randint(min_name, max_name)
        file_mame = ''.join(choices(ascii_letters + digits, k=len_name_file)) +'.'+ type_file
        file_size = randint(min_byte, max_byte)
        # random_bytres = os.urandom(file_size)
        random_bytres = ''.join(choices(ascii_letters + digits, k=file_size)).encode('UTF-8')

        with open(file_mame, 'wb') as f:
            f.write(random_bytres)

ctreate_file('bin')





