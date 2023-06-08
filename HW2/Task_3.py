"""Напишите программу, которая принимает две строки вида
 “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions."""
import fractions
import re
import math

a1, b1, = map(int, re.split('/', input('Веедите две дроби в формате a/b: ')))
a2, b2, = map(int, re.split('/', input('Веедите две дроби в формате a/b: ')))

# a1, b1, a2, b2 = map(int, input('Веедите две дhоби в формате a/b: ').split('/' ''))

print(a1, b1, a2, b2)

nok = math.lcm(b1, b2)

print(nok)

numerator_sum = (nok / b1 * a1) + (nok / b2 * a2)
print(f'результат суммы {numerator_sum}/{nok}')
f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print(f'Проверка суммы {f1 + f2}')
print(f'результат умножения {a1 * a2}/{b1 * b2}')
print(f'Проверка умножения {f1 * f2}')

