"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.

Дополните id до 10 цифр незначащими нулями.

В именах первую букву сделайте прописной.

Добавьте поле хеш на основе имени и идентификатора.

Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.

Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
import json


def create_csv_json(file_csv, new_json_file):
    with(open(file_csv, 'r', encoding='utf-8', newline='') as f_cvs_red,
         open(new_json_file, 'w', encoding='utf-8') as f_json_wrt
    ):
        csv_file = csv.reader(f_cvs_red)
        dict_res = {}
        # print(*csv_file)
        for i, row in enumerate(csv_file):
            if i != 0:
                user_id = f'{"0" * (10 - len(row[1]))}{row[1]}'
                hash_id = str(hash(user_id)) + str(hash(row[2]))
                dict_res.setdefault(row[0], {user_id: [hash_id, row[1]]})[user_id] = [hash_id, row[2]]
        print(dict_res)

        json.dump(dict_res, f_json_wrt, ensure_ascii=False, indent=1)





if __name__ == '__main__':
    create_csv_json('user_id.csv', 'user_id_add.json')
