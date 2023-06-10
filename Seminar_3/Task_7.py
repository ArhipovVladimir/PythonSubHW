"""
Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

text = input('Введите текст: ')
text = text.replace(' ', '').replace(',', '').lower()
char_list = [char for char in text]
res_dict = {}
for car in char_list:
    # res_dict.setdefault(car, {}).add(char_list.count(car))
    if car not in res_dict:
          res_dict[car] = text.count(car)

print(res_dict)
