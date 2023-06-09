"""Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях"""

text = input('Введитее строку: ')

if text.isdecimal():
    if int(text) > 0:
        digit_text = int(text)
        print(f'{digit_text = } {type(digit_text)}')

if text.replace('.', '').replace('-','').replace(',''').isdecimal() \
and text.count('.') == 1 and text.count('-') <= 1 and text[1:].count('-'):
       float_text = float(text)
       print(f'{float_text = } {type(float_text)}')