"""
генерация коэфф уравнения в фаил cvs
"""
import csv
from random import randint


def gen_kt_abc(count):
    with open(f'{gen_kt_abc.__name__}', 'w', encoding='utf-8', newline='') as f_csv:
        csv_write = csv.DictWriter(f_csv, fieldnames=['a', 'b', 'c'])
        csv_write.writeheader()
        data = []
        for _ in range(count):
            data.append({'a': randint(-100, 100),
                         'b': randint(-100, 100),
                         'c': randint(-100, 100)})

        csv_write.writerows(data)

if __name__ == '__main__':
    gen_kt_abc(1000)