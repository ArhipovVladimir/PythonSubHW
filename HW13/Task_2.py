
"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.

"""
import csv
import json


def create_json_csv(file_json, file_csv):

    try:
        with (open(file_json, 'r', encoding='utf-8') as f_read,
              open(file_csv, 'w', encoding='utf-8', newline='')as f_write):
            dict_json = json.load(f_read)
            csv_write = csv.DictWriter(f_write, fieldnames=["level", "user_id", "user_name"])
            csv_write.writeheader()
            all_data = []
            for level in dict_json:
                for user_id, user in dict_json.items():
                    all_data.append({'level': level, 'user_id': user_id, 'user_name': user})

            print(all_data)
            csv_write.writerows(all_data)
    except FileNotFoundError as e:
           print(f' файл не найден {e}')



    # print(dict_user)

if __name__ == '__main__':
    create_json_csv('user_id_v1.json', 'user_id.csv')