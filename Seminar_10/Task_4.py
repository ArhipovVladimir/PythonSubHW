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
    def __init__(self, id_num, *args, **kwargs):
        def get_access(self):
            return sum(map(int, str(self.id_num))) % 7

        super().__init__(*args, **kwargs)
        self.id_num = randint(100000, 999999)
        self.access = get_access(self)


if __name__ == '__main__':

    p2 = Person(15, 'Ivan', 'Petrov', 'Sidorovich', 25)
    print(p2.full_name())
    print(p2.get_age())
    p2.birthday()
    print(p2.get_age())
    print(p2.id_num)
    print(p2.access)