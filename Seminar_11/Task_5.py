"""
Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

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
        line = max(self.line, self.hegt, other.line, other._hegt)
        hegt = perim_sum // 2 - line
        return Qaudr(line, hegt)

    def __sub__(self, other):
        if self.perim() < other.perim():
            return self
        perim_sub = self.perim() - other.perim()
        line = min(self.line, self.hegt, other.line, other._hegt)
        hegt = perim_sub // 2 - line
        return Qaudr(line, hegt)

    def __str__(self):
        return f'длинна {self.line} ширина {self.hegt}'




if __name__ == '__main__':
    q1 = Qaudr(20, 5)
    q2 = Qaudr(5, 3)
    q3 = q1 + q2
    q4 = q1 - q2
    q5 = q2 - q1
    print(q1)
    print(q2)
    print(q3)
    print(q4)
    print(q1.perim())
    print(q2.perim())
    print(q3.perim())
    print(q4.perim())
    print(q5.perim())