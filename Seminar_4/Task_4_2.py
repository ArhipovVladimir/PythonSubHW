"""Функция получает на вход список чисел.

Отсортируйте список по убыванию суммы цифр"""

def funk (list_number):
    dict_number = {}
    for item in list_number:
        dict_number.setdefault(item, sum(map(int, str(item))))
    resalt = sorted(dict_number, key= lambda x: dict_number[x], reverse=True)
    print(resalt)

lst = [75, 41, 80, 19, 16,1]
funk(lst)