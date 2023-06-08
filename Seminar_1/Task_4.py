'''
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
'''
import decimal
from math import pi
from decimal import Decimal
decimal.getcontext().prec = 42

def param(d):
    square = decimal.Decimal(pi * d * d / 4)
    length_1 = decimal.Decimal(pi * d)
    return square, length_1


while True:
    diam = int(input('Веедите диамет круга до 1000 у.е.'))
    if diam < 1000:
        break
    print('Введено больше  1000')

print(*param(diam))

