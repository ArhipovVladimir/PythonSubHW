"""Gen predmet"""

from random import choice, randint
import csv
COUNT_ORDER = 21
MIN_TEST = 0
MAX_TEST = 100
def gen_csv_order (stud_name="file"):
      with open(f'{stud_name}_order.csv', 'w', encoding='utf-8', newline='') as f:
        predmets = ['химия', 'физика', 'математика', 'русский', 'информатика']
        csv_write = csv.DictWriter(f, fieldnames=predmets)
        csv_write.writeheader()
        lisl_order = [2, 3, 4, 5]
        for _ in range(COUNT_ORDER):
            row_order = []
            row_order.append({'химия': choice(lisl_order),
                                   'физика': choice(lisl_order),
                                   'математика': choice(lisl_order),
                                   'русский': choice(lisl_order),
                                   'информатика': choice(lisl_order)})
            csv_write.writerows(row_order)


def gen_csv_test(stud_name="file"):
    with open(f'{stud_name}_test.csv', 'w', encoding='utf-8', newline='') as f:
        predmets = ['химия', 'физика', 'математика', 'русский', 'информатика']
        csv_write = csv.DictWriter(f, fieldnames=predmets)
        csv_write.writeheader()
        row_order = [{'химия': randint(MIN_TEST, MAX_TEST),
                          'физика': randint(MIN_TEST, MAX_TEST),
                          'математика': randint(MIN_TEST, MAX_TEST),
                          'русский': randint(MIN_TEST, MAX_TEST),
                          'информатика': randint(MIN_TEST, MAX_TEST)}]
        csv_write.writerows(row_order)



if __name__ == '__main__':
    gen_csv_order('Иван Петров')
    gen_csv_test('Иван Петров')

