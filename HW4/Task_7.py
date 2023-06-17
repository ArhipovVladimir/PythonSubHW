
'''Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''

def copmani_analiti (data_comp):
    list_res = []
    for item in data_comp.values():
        if (sum(item)) > 0:
            list_res.append(True)
        else: list_res.append(False)
    return all(list_res)


    # return all(map(lambda x: sum(x) > 0, data_comp))


data_compani = {"OOO": [100, -50, -20],
                "AO": [120, -80, -20],
                "GOV": [200, -20, -30]}

print(copmani_analiti(data_compani))
