'''Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''

user_text = input('введите текст: ')

dict_code = {item: ord(item) for item in user_text}

print(dict_code)

dict_iret = iter(dict_code.items())
for _ in range(5):
    print(next(dict_iret))
