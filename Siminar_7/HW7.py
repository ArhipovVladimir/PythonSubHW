"""
Дорабатываем функции из предыдущих задач.
* Генерируйте файлы в указанную директорию — отдельный параметр функции.

* Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).

* Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.

* При переименовании в конце имени добавляется порядковый номер.

* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.

* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

import os

def grour_rename(dir_, original_exten, new_name):
    os.chdir(dir_)
    print(os.getcwd())
    files = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file)\
             and file.split('.')[1] == original_exten]
    print(files)
    new_name_file, new_exten = new_name.split('.')
    count = 1
    for file in files:
        os.rename(file, f'{file}_{new_name_file}_{count}.{new_exten}')
        count += 1

if __name__ == '__main__':
    grour_rename('C:\\Users\\arhip\\OneDrive\\Документы\\GB\\Python2\\PythonSubHW\\Siminar_7\\текст', "bin", "bin_file.bin")