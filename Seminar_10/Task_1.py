"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.

"""

import decimal
from math import pi
from decimal import Decimal
decimal.getcontext().prec = 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def sqare(self):
       return decimal.Decimal(pi * self.radius * 2  * self.radius * 2 / 4)

    def len_cirk(self):
        return decimal.Decimal(pi * self.radius * 2)


if __name__ == '__main__':
    circ1 = Circle(5)
    print(Circle.sqare(circ1))
    print(circ1.radius)
    print(circ1.sqare())
    print(circ1.len_cirk())
