"""
Возьмите любую из задач с прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры
в свойства. Задачи должны решаться через вызов методов экземпляра.

Напишите функцию, которая преобразует pickle файл
 хранящий список словарей в табличный csv файл.
 Для тестированию возьмите pickle версию файла из предыдущей задачи."""

import pickle
import csv

class conv_pickle_csv:

    def __init__(self, file_pickle):
        self.file_pickle=file_pickle

    def conv(self):

        with(open(self.file_pickle, 'rb') as f_pickle,
             open(self.file_pickle.strip('.pickle') + '.csv', 'w', encoding='utf-8', newline='') as f_csv):

            dict_pickle = pickle.load(f_pickle)
            csv_write = csv.DictWriter(f_csv, fieldnames=list(dict_pickle[0].keys()))
            csv_write.writeheader()
            all_data = []
            for line in dict_pickle:
                str_data = {}
                for key, value in line.items():
                    str_data.setdefault(key, value)
                all_data.append(str_data)
            # print(all_data)
            csv_write.writerows(all_data)


if __name__ == '__main__':
    conv1 = conv_pickle_csv('user_id_add.pickle')
    conv1.conv()
