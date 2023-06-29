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
        lst = []
        file = [*csv_file]
        header_id, header_name, header_acces = file[0]
        for assecc, id, name in file[1:]:
            # добавдение нолей
            id = f'{"0" * (10 - len(id))}{id}'
            # для больших первых букв
            name = name.title()
            lst.append({header_id: id, header_name:name, header_acces:assecc, 'hash': hash(name+id)})



        json.dump(lst, f_json_wrt, ensure_ascii=False, indent=1)


# f'{"0" * (10 - len(id))}{id}'


if __name__ == '__main__':
    create_csv_json('user_id.csv', 'user_id_add.json')
