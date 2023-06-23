'''
Задание
✔ Решить задачи, которые не успели решить на семинаре.

✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''

user_patch = "C:\PycharmProjects\PythonSubHW\HW5\HW_5_Task_1.py"

*only_patch, name_type_file = user_patch.split('\\')
name_file, type_file = name_type_file.split('.')
path_file = "\\".join(only_patch)
print(path_file, name_file, type_file, sep='\n')

