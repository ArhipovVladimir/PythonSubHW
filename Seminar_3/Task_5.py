"""✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы."""

my_list = [12, 12, 15, 15, 12, 13, 16, 12, 18, 3]
print(my_list)

rez_list = []

def elem_find (poz=0)
    for item in my_list:
        if item % 2 == 0:
            rez_list.append(my_list.index(item)+1)



print(rez_list)
