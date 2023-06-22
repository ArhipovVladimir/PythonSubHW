'''
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный
 случайные  варианты и выведите 4 успешных расстановки.

'''
from random import randint
__all__=['get_pozis']

SIZE = 8
def get_pozis():
    list_posis = []
    for i in range(SIZE):
        list_point = []
        for j in range(2):
            list_point.append(randint(1, SIZE))
        list_posis.append(list_point)
    return list_posis

if __name__ == '__main__':
    print(get_pozis())

