"""✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы."""

my_list = [12, 12, 15, 15, 12, 13, 16, 13, 3, 3]
print(my_list)

rez_list = []


for item in my_list:
  if item % 2 != 0 and my_list.index(item) < :
         rez_list.append(my_list.index(item)+1)



print(rez_list)
