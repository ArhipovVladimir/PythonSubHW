"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def create_json(patch_file):
    with open(patch_file, 'r', encoding='utf-8') as f1:
        result_json_list = []
        for str_file in f1:
            file_mame, num_res = str_file.split()
            file_mame = str(file_mame).title()
            result_json_list.append({'file_mame': file_mame, 'num_res': num_res})

    with open('result2_json', 'w') as f2:
        json.dump(result_json_list, f2)

    print(result_json_list)


if __name__ == '__main__':
    create_json('/Seminar_7\\result.txt')