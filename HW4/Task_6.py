
'''
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
для простоты используем положительную индексацию
'''

def funk(lst, i1, i2):
    start = min(i1, i2)
    stop = max(i1, i2)
    if stop > len(lst):
        stop = len(lst)
    if start < 0:
        start = 0

    return sum(lst[start:stop+1])

    # print(type(lst), i1, type(i1), i2, type(i2))



lst = [75, 41, 80, 19, 16,1]
a, b = map(int, input('Enter text: ').split())
print(funk(lst, a, b))