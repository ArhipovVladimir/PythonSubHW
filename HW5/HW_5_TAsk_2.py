'''
✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии'''


name = ['Ivan', 'Petr', 'Serg', 'Fedot']
tax = [1000, 1200, 900, 1500]
bonus = ['10.3%', '10.5%', '10.25%', '10.75%']


bonus_ok = [*map(lambda x: (float(x.replace('%', ''))) / 100, bonus)]
dict_salary_only = {name: tax + tax * bonus_ok for name, tax, bonus_ok in zip(name, tax, bonus_ok)}

print(dict_salary_only)

