"""✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды."""

my_list = [12, 12, 15, 15, 12, 'дом', 'окно','дом','окно','окно']

#  второй вариант

print(my_list)
for item in my_list:
    if my_list.count(item) == 2:
        my_list.remove(item)
        my_list.remove(item)
print(my_list)

#  первый вариант

print(my_list)
for item in my_list:
    if my_list.count(item) == 2:
        for _ in range(2):
            my_list.remove(item)

print(my_list)

