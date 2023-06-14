'''
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''
import random

list_for_sort = []
for _ in range (1, 20):
    list_for_sort.append(random.randint(1, 100))

def bobl_sort (list_sort):
    n = len(list_sort)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list_sort[j] > list_sort[j + 1]:
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]




print(list_for_sort)
bobl_sort(list_for_sort)
print(list_for_sort)

