"""Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
import random

from Task_3 import Human
from random import randint

class Person(Human):

    GET = 7
    def __init__(self, *args, **kwargs):


        def _get_id_num(self):
            return randint(100000, 999999)

        def _get_access(self):
            return sum(map(int, str(self.id_num))) % self.GET

        self.id_num = _get_id_num(self)
        self.access = _get_access(self)
        super().__init__(*args, **kwargs)


if __name__ == '__main__':

    p2 = Person('Ivan', 'Petrov', 'Sidorovich', 25)
    print(p2.full_name())
    print(p2.get_age())
    p2.birthday()
    print(p2.get_age())
    print(p2.id_num)
    print(p2.access)