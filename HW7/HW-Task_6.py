"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
from Task_5 import create_dif_files
import os
def create_her_files(*args, **kwargs):
    os.chdir(args[0])
    if args[1] not in os.listdir():
        os.mkdir(args[1])
    os.chdir(args[1])
    create_dif_files(**kwargs)

if __name__ == '__main__':
    create_her_files('C:\\Users\\arhip\\OneDrive\\Документы\\GB\\Python2\\PythonSubHW\\Siminar_7\\Тест создания', 'тест4', txt=20, bin=3, jpg=3)