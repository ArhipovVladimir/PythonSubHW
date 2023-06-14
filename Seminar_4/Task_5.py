'''
Задание № 5
Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
'''

name = ['Ivan', 'Petr', 'Serg', 'Fedot']
tax = [1000, 1200, 900, 1500]
bonus = ['10,3%', '10.5', '10,25', '10,75']



def salary (name, tax, b):
    dict_salary = {}
    bonus_ok = [*map(lambda x: (float(x.replace(',', '.').replace('%', '')))/100, b)]
    for x in zip(name, tax, bonus_ok):
        dict_salary.setdefault(x[0], x[1] + x[1] * x[2])
    print(dict_salary)


salary(name, tax, bonus)
