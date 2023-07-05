"""Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат."""

class Qaudr:

    def __init__(self, line, hegt=None):
        if hegt == None:
            self.line = self.hegt = line
        else:
            self.line = line
            self.hegt = hegt

    def perin(self):
        return self.line * 2 + self.hegt * 2

    def sqrq(self):
        return self.line * self.hegt

if __name__ == '__main__':
    q1 = Qaudr(20, 5)
    print(q1.perin())
    print(q1.sqrq())