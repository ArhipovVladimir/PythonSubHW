"""Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера."""


class Dickript:

    def __set_nane__(self, name):
        self.name = name

    def __get__(self, instance, ower):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        self.name = value

    def validate(self, value):
        if value < 0:
            raise ValueError(f' значение {value} должно быть больше 0')


class Qaudr:
    """class QUADR"""
    # __slots__ = ('_line', '_hegt')

    line = Dickript()
    wegth = Dickript()

    def __init__(self, line, wegth=None):
        if wegth == None:
            self.line = self.wegth = wegth
        else:
            self.line = line
            self.wegth = wegth

    def perim(self):
        return self.line * 2 + self.wegth * 2

    def sqrq(self):
        return self.line * self.wegth

    def __add__(self, other):
        """add merthod class Quadr"""

        perim_sum = self.perim() + other.perim()
        line = max(self.line, self.wegth, other.line, other.wegth)
        hegt = perim_sum // 2 - line
        return Qaudr(line, hegt)

    def __sub__(self, other):
        """sub merthod class Quadr"""

        if self.perim() < other.perim():
            return self
        perim_sub = self.perim() - other.perim()
        line = min(self.line, self.wegth, other.line, other.wegth)
        hegt = perim_sub // 2 - line
        return Qaudr(line, hegt)

    def __eq__(self, other):
        """__eq__ method class Quadr"""

        return self.perim() == other.perim()

    def __gt__(self, other):
        """__qt__ method class Quadr"""

        return self.perim() > other.perim()

    def __lt__(self, other):
        """__lt__ method class Quadr"""
        return self.perim() < other.perim()

    def __str__(self):
         return f'длинна {self.line} ширина {self.wegth}'






if __name__ == '__main__':
    q1 = Qaudr(20, 20)
    # print(q1)
    q2 = Qaudr(-12, 12)
    q3 = Qaudr(5, 3)
    # print(q2)
    # print(q3)

    # q4 = q1 + q3
    # print(q1 < q2)
    # print(q1 > q2)
    # print(q3 == q2)
    # print(q1 != q2)
    # print(q4)
    # print(q4.__slots__)
    # q4.size = 3
    # print(q4)

