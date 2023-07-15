"""Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств."""

class Qaudr:
    """class QUADR"""
    # __slots__ = ('_line', '_hegt')

    def __init__(self, line, hegt=None):
        if hegt == None:
            self._line = self._hegt = line
        else:
            self._line = line
            self._hegt = hegt

    def perim(self):
        return self._line * 2 + self._hegt * 2

    def sqrq(self):
        return self._line * self._hegt

    def __add__(self, other):
        """add merthod class Quadr"""

        perim_sum = self.perim() + other.perim()
        line = max(self._line, self._hegt, other.line, other._hegt)
        hegt = perim_sum // 2 - line
        return Qaudr(line, hegt)

    def __sub__(self, other):
        """sub merthod class Quadr"""

        if self.perim() < other.perim():
            return self
        perim_sub = self.perim() - other.perim()
        line = min(self._line, self._hegt, other.line, other._hegt)
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
         return f'длинна {self._line} ширина {self._hegt}'

    @property
    def line(self):
        return self._line

    @property
    def hegt(self):
        return self._hegt

    @line.setter
    def line(self, value):
        if value > 0:
            self._line = value
        else:
            raise ValueError(f'ошибка {value}')


    @hegt.setter
    def hegt(self, value):
        if value > 0:
            self._hegt = value
        else:
            raise ValueError (f'ошибка {self._hegt}')





if __name__ == '__main__':
    q1 = Qaudr(20, 5)
    print(q1)
    q2 = Qaudr(12, 3)
    q3 = Qaudr(5, 3)
    q1.line = 1
    print(q1)
    q4 = q1 + q3
    print(q1 < q2)
    print(q1 > q2)
    print(q3 == q2)
    print(q1 != q2)
    print(q4)
    print(q4.__slots__)
    q4.size = 3
    print(q4)
