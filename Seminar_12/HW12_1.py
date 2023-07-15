"""Gen predmet"""

from random import randint
import csv
COUNT_ORDER = 21
def gen_csv (min_order=0, max_order=5, max_test=0, min_test=100, stud_name="file"):
      with open(f'{stud_name}.csv', 'w', encoding='utf-8', newline='') as f:
        predmets = ['химия', 'физика', 'математика', 'русский', 'информатика']
        csv_write = csv.DictWriter(f, fieldnames=predmets)
        csv_write.writeheader()
        for _ in range(COUNT_ORDER):
            row_order = []
            row_order.append({'химия': randint(min_order, max_order),
                                   'физика': randint(min_order, max_order),
                                   'математика': randint(min_order, max_order),
                                   'русский': randint(min_order, max_order),
                                   'информатика': randint(min_order, max_order)})
            csv_write.writerows(row_order)
        row_order.append({'химия': randint(max_test, min_test),
                              'физика': randint(max_test, min_test),
                              'математика': randint(max_test, min_test),
                              'русский': randint(max_test, min_test),
                              'информатика': randint(max_test, min_test)})
        csv_write.writerows(row_order)


if __name__ == '__main__':
    gen_csv(2, 5, 0, 100, 'Иван Петров')
