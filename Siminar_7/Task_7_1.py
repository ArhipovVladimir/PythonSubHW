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
        'текст': ('txt', 'bin')}

def group(dir_):

   files = [file for file in os.listdir(dir_) if os.path.isfile(file)]
   for file in files:
       *_, exten = file.split('.')
       for fold in DICT:
           if fold not in os.listdir():
                os.mkdir(fold)
           if exten in DICT[fold]:
               os.replace(file, os.path.join(os.getcwd(), fold, file))


if __name__ == '__main__':
    group(os.getcwd())