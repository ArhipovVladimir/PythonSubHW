"""
Возьмите любую из задач с прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры
в свойства. Задачи должны решаться через вызов методов экземпляра.

 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку."""

import csv
import pickle

class conv_csv_picle:

    def __init__(self, file_csv):
        self.file_csv = file_csv


    def conv(self):
        with (open(self.file_csv, 'r', encoding='utf-8', newline='') as f_read,
                open(self.file_csv.strip('.csv') + '.pickle', 'wb') as f_picle):
                csv_file = csv.reader(f_read)
                data_csv = [*csv_file]
                key_csv = data_csv[0]
                dict_pickle = {}
                for line_fine in data_csv[1:]:

                    for i, value in enumerate(line_fine):
                        dict_pickle.setdefault(key_csv[i], value)

                   pickle.dump(dict_pickle, f_picle)





if __name__ == '__main__':
    conv2 = conv_csv_picle('user_id_add.csv')
    conv2.conv()