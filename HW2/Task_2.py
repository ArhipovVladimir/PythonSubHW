'''
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

def conv(number: int, system: int) -> list:
    dict_hex = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                11: 'B', 12: 'C', 13: 'D', 14: 'E', 16: 'F'}
    # dict_hex = dict(1: 1, 2: 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6, 7 = 7, 8 = 8, 9 = 9, 10 = 'A', 11 = 'B', 12 = 'C')
    temp = []
    while number > 0:
        temp.append(dict_hex(number % system))
        number //= system
    temp.reverse()
    return ''.join(temp)



num, syst = map(int, input('введите число: ').split())
print(f'Число {num} в системе {syst} исчисления рано {conv(num, syst)}')
print(f'проверка двоичная {bin(num)}; восьмеричная {oct(num)} щеснадцатеричная {}')