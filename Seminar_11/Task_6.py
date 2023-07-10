"""
Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Qaudr:

    def __init__(self, line, hegt=None):
        if hegt == None:
            self.line = self.hegt = line
        else:
            self.line = line
            self.hegt = hegt

    def perim(self):
        return self.line * 2 + self.hegt * 2

    def sqrq(self):
        return self.line * self.hegt

    def __add__(self, other):
        perim_sum = self.perim() + other.perim()
        line = max(self.line, self.hegt, other.line, other.hegt)
        hegt = perim_sum // 2 - line
        return Qaudr(line, hegt)

    def __sub__(self, other):
        if self.perim() < other.perim():
            return self
        perim_sub = self.perim() - other.perim()
        line = min(self.line, self.hegt, other.line, other.hegt)
        hegt = perim_sub // 2 - line
        return Qaudr(line, hegt)

    def __eq__(self, other):
        return self.perim() == other.perim()

    def __gt__(self, other):
        return self.perim() > other.perim()

    def __lt__(self, other):
        return self.perim() < other.perim()

    def __str__(self):
        return f'длинна {self.line} ширина {self.hegt}'




if __name__ == '__main__':
    q1 = Qaudr(20, 5)
    q2 = Qaudr(5, 3)
    q3 = Qaudr(5, 3)
    print(q1 < q2)
    print(q1 > q2)
    print(q3 == q2)
    print(q1 != q2)