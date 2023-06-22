'''
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный
 случайные  варианты и выведите 4 успешных расстановки.
'''
from HW6_Task_3 import get_pozis
from HW6_Task_2 import eight_queens

count = 4
dict_res = {}
while count > 0:
    variatn = get_pozis()
    # print(variatn)
    res = eight_queens(get_pozis())
    # print(res)
    if res:
        dict_res[count] = variatn
        count -= 1
        print('oK')

print(dict_res)
# with
