'''Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно'''

# def conv(number: int, system: int) -> bool:
#     temp = ''
#     while number > 0:
#         temp = temp + str(number % system)
#         number //= system
#     return temp[::-1]

def conv(number: int, system: int) -> list:
    temp = []
    while number > 0:
        temp.append(str(number % system))
        number //= system
    temp.reverse()
    return ''.join(temp)



num, syst = map(int, input('введите число: ').split())
print(f'Число {num} в системе {syst} исчисления рано {conv(num, syst)}')
print(f'проверка двоичная {bin(num)}; восьмеричная {oct(num)}')
