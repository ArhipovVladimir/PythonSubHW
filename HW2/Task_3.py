"""Напишите программу, которая принимает две строки вида
 “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions."""
import fractions
import re
import math


def ReduceFraction(n, m):
    x = math.gcd(n, m)
    p = n // x
    q = m // x
    return p, q


a1, b1, = map(int, re.split('/', input('Веедите две дроби в формате a/b: ')))
a2, b2, = map(int, re.split('/', input('Веедите две дроби в формате a/b: ')))

# a1, b1, a2, b2 = map(int, input('Веедите две дhоби в формате a/b: ').split('/' ''))

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)

nok = math.lcm(b1, b2)

numerator_sum = (int(nok / b1) * a1) + (int(nok / b2) * a2)
numer_sum, deomer_sum = ReduceFraction(numerator_sum, nok)
print(f'результат суммы {numer_sum}/{deomer_sum}')

print(f'Проверка суммы {f1 + f2}')

numer_mult, deomer_mult = ReduceFraction(a1 * a2, b1 * b2)
print(f'результат умножения {numer_mult}/{deomer_mult}')

print(f'Проверка умножения {f1 * f2}')
