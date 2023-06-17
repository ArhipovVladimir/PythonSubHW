'''
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''


names = 'petr'
namet = 'ivan'
books= 'ivanov'
firsnamet = 'ivanovs'
sss = 'serg'
s = 'son'
llibs = 'ddd'


# print(*filter(lambda x: not x[0].startswith('__'), globals().items()))
def s_del():
    glob_dict = globals()
    dict_s = dict(filter(lambda x: x[0].endswith('s', 1) and not x[0].startswith('__'), globals().items()))
    print(dict_s.items())
    for item in dict_s.items():
        print(str(item[0][0:-1]), item[1])
        glob_dict.setdefault(item[0][0:-1], item[1])
        glob_dict[item[0]] = None

s_del()

dictt = dict(filter(lambda x: not x[0].startswith('__'), globals().items()))
print(f'{dictt.items()=}')