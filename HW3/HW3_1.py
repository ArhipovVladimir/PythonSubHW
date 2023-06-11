'''Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.'''

my_list = [12, 11, 15, 15, 12, 'дом', 'окно','дом','рама','окно']

#  второй вариант

print(my_list)
new_list = []
for item in my_list:
    if my_list.count(item) > 1 and item not in new_list:
        new_list.append(item)

print(new_list)

