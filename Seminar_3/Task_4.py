"""✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды."""

my_list = [12, 12, 15, 15, 12, 'дом', 'окно','дом','окно','окно']
print(my_list)
for item in my_list:
    if my_list.count(item) == 2:
        dell_elem = item
        my_list.remove(item)
        my_list.remove(dell_elem)


print(my_list)

