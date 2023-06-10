"""✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа"""



my_tup = (1, "дом", 2, False, True, 2.4, "окно", 3.14,)

'''первй вариает через if'''

dickt_res = {}
for item in my_tup:
     if type(item) in dickt_res:
        dickt_res[type(item)].append(item)
     else:
        dickt_res[type(item)] = [item]

print(dickt_res)

'''втрой вариант через setdefault и еще ч/з get'''

dickt_res1 = {}
for item in my_tup:
    dickt_res1.setdefault(type(item), []).append(item)
    # dickt_res1[type(item)] = dickt_res1.get(type(item), []) + [item]
print(dickt_res1)
