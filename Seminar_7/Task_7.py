"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os
from pathlib import Path

DICT = {'видео': ('mvk', 'avi', 'mp4'),
        'изображеие':('pnd', 'jpg', 'jpeg'),
        'текст': ('txt', 'bon')}

def group(dir_):

   for i in DICT:
       os.mkdir(f'{dir_}/{i}')


   for *_, files in os.walk(dir_):
        for file in files:
            *_, exten = file.split('.')
            for i in DICT:
                if exten in DICT[i]:
                    os.replace(file, os.path.join(os.getcwd(), i, file))
        break



print(os.getcwd())
group(os.getcwd())