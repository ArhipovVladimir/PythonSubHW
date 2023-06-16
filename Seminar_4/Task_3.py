'''
Задание №39
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте0 словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно
'''

def num_dict (digit_str):
    res_dict = {}
    a, b = sorted(map(int, digit_str.split()))
    for item in range (a, b + 1):
        res_dict.setdefault(chr(item), item)
    #     map(res_dict.setdefault, range (a, b + 1))

    print(a, b)
    print(res_dict)

num_dict(input('Etter text'))