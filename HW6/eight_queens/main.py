'''
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный
 случайные  варианты и выведите 4 успешных расстановки.
'''
from HW6.eight_queens.HW6_Task_3 import get_pozis
from HW6.eight_queens.HW6_Task_2 import eight_queens
from datetime import datetime


def save_variant(*arg):
    with open('varianrs.txt', 'a') as h:
        time_date = str(datetime.now())
        h.write(f'{time_date}  {arg}\n')

def start (count):

    count = count
    dict_res = {}
    while count > 0:
        variatn = get_pozis()
        res = eight_queens(get_pozis())
        if res:
            dict_res[count] = variatn
            count -= 1
            print('oK')
            save_variant(variatn, count)

if __name__ == '__main__':
    start(4)
