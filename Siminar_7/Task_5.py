"""Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи."""

from Task_4 import ctreate_file

def create_dif_files(**kwargs):

    for ext, count in kwargs.items():
        ctreate_file(ext, count_file=count)

if __name__ == '__main__':
    create_dif_files(txt=20, bin=3, jpg=3)
