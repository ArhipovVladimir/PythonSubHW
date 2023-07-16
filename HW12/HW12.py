"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых."""

from HW12_1 import gen_csv_test
from HW12_1 import gen_csv_order
import csv
from statistics import mean


class GetFulLName:


    def __set_name__(self, owner, name):
        self.param_name = name.split(' ')

    def __set__(self, instance, value):
        self.validate(value)
        # setattr(instance, self.param_name, value)
        self.param_name = value

    def validate(sels, value):
        if not value.isalpha():
            raise ValueError(f'в строке должны быть только буквы {value}')
        if not value.istitle():
            raise ValueError(f' ФИО не с большой буквы {value}')


def Readfile(first_name, last_name):
    gen_csv_test (f'{first_name} {last_name}')
    gen_csv_order (f'{first_name} {last_name}')
    file_order = f'{first_name} {last_name}_order.csv'
    file_test = f'{first_name} {last_name}_test.csv'


    with (open(file_order, 'r', encoding='utf-8', newline='') as f_ord,
          open(file_test, 'r', encoding='utf-8', newline='') as f_test):

            csv_file = csv.reader(f_ord)
            lst_ord = []
            file = [*csv_file]
            a, b, c, d, e = file[0]

            for a_ord, b_ord, c_ord, d_ord, e_ord in file[1:]:
                lst_ord.append({a: int(a_ord), b: int(b_ord), c: int(c_ord),
                                d: int(d_ord), e: int(e_ord)})

            csv_file = csv.reader(f_test)
            lst_test = []
            file = [*csv_file]
            a, b, c, d, e = file[0]

            for a_ord, b_ord, c_ord, d_ord, e_ord in file[1:]:
                lst_test.append({a: int(a_ord), b: int(b_ord), c: int(c_ord), d:
                                    int(d_ord), e: int(e_ord)})


            return lst_ord, lst_test



class Student:

    # first_name = GetFulLName()
    # last_name = GetFulLName()



    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.order, self.test = Readfile(self.first_name, self.last_name)


    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.order}'

    def get_mean(self, predmrt):
        list_ord_predmet = []
        for i in range(len(self.order)):
            for k, v in self.order[i].items():
                if k == predmrt:
                    list_ord_predmet.append(v)
        print(f'{self.last_name} среднее {mean(list_ord_predmet)} по {predmrt}')

    def get_test(self):
        # print(self.test[0])
        for k, v in self.test[0].items():
             print(f'{self.last_name} итоговые тесты {k} {v}')




if __name__ == '__main__':
    s2 = Student('Иван', 'Петров')
    print(s2)
    s3 = Student('Владимир', 'Архипов')
    print(s3)
    print(s2.get_mean('химия'))
    print(s3.get_mean('физика'))

    print(s3.get_test())