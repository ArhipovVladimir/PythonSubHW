"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.

"""
import csv
import json


def create_csv(file_json, file_csv):

    with (open(file_json, 'r', encoding='utf-8') as f_read,
          open(file_csv, 'w', encoding='utf-8')as f_write):

        dict_json = json.load(f_read)
        csv_write = csv.DictWriter(f_write, 'excel_tab', fieldnames=["level", "user_id", "user_name"],
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        all_data = []
        for i, level in enumerate(dict_json):
            for j, user_id, in enumerate(dict_json[level]):
                if i != 0 and j != 0:
                    all_data.append(level, user_id, dict_json[level][user_id])

        csv_write.writerows(all_data)

    # print(dict_user)













if __name__ == '__main__':
    create_csv('user_id.json', 'user_id.csv')