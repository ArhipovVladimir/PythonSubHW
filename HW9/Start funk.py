import csv
from functools import wraps
import json
import os

def statr_funk(file_csv):
    def deco(func):

        @wraps(func)
        def wrapper():
            with open(file_csv, 'r', encoding='utf-8', newline='') as f_csv:
                csv_read = csv.DictReader(f_csv, fieldnames=['a', 'b', 'c'])
                for i, kwargs in enumerate(csv_read):
                    if i != 0:
                        yield kwargs, func(**kwargs)

        return wrapper
    return deco


def save_json(func):
    file = f'{func.__name__}.json'
    print(file)
    if file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f_json:
            json_file = json.load(f_json)
    else:
        json_file = []
    @wraps(func)
    def wrapper(**kwargs):
        for arg, result in func(**kwargs):
            # if result:
                dct = {'args':arg, 'result': str(result)}
                json_file.append(dct)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(json_file, json_f, indent=2)
            # else:
            #     break

    return wrapper


def get_sqr(**kwargs):
    a, b, c = map(int, kwargs.values())
    if a == 0:
        return 0, 0, 0
    diskrim = b ** 2 - 4 * a * c
    x1 = (- b + (diskrim ** 0.5)) / (2 * a)
    x2 = (- b - (diskrim ** 0.5)) / (2 * a)
    return diskrim, x1, x2


@save_json
@statr_funk('gen_kt_abc')
def start_sqr(**kwargs):
    return get_sqr(**kwargs)


if __name__ == '__main__':
    start_sqr()
