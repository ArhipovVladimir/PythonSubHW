"""✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа"""



my_tup = (1, "дом", 2, False, True, 2.4, "окно", 3.14,)

dickt_res = {}
for item in my_tup:
    type_item = type(item)
    if type_item in dickt_res:
        dickt_res[type_item].append(item)
    else:
        dickt_res[type_item] = [item]

print(dickt_res)

dickt_res1 = {}
for item in my_tup:
    # dickt_res1.setdefault(type(item), []).append(item)
    dickt_res1[type(item)] = dickt_res1.get(type(item), []) + [item]
print(dickt_res1)
