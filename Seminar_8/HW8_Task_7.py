""" Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку."""
import csv
import pickle


def get_kye_from_csv(file_csv):
    with open(file_csv, 'r', encoding='utf-8', newline='') as f_read:
        csv_file = csv.reader(f_read)
        data_csv = [*csv_file]
        key_csv = data_csv[0]
        dict_pickle = {}
        for line_fine in data_csv[1:]:

            for i, value in enumerate(line_fine):
                dict_pickle.setdefault(value, key_csv[i])

    str_pickle = pickle.dumps(dict_pickle)
    print(str_pickle)




if __name__ == '__main__':
    get_kye_from_csv('user_id_add.csv')