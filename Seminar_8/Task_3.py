"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.

"""
import csv
import json


def create_csv(file_json, file_csv):

    with (open(file_json, 'r', encoding='utf-8') as f_read,
          open(file_csv, 'w', encoding='utf-8', newline='')as f_write):

        dict_json = json.load(f_read)
        csv_write = csv.DictWriter(f_write, fieldnames=["level", "user_id", "user_name"])
        csv_write.writeheader()
        all_data = []
        for level in dict_json:
            for user_id, in dict_json[level]:
                    all_data.append({'level': level, 'user_id': user_id, 'user_name': dict_json[level][user_id]})

        print(all_data)
        csv_write.writerows(all_data)

    # print(dict_user)













if __name__ == '__main__':
    create_csv('user_id.json', 'user_id.csv')