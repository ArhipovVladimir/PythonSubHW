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
text = 'Вова едент в санаторий, на 12 дней'
# text = input('Введите текст: ')
text = text.replace(' ', '').replace(',', '').lower()
char_list = [char for char in text]
print(char_list)
res_dict = {}
for car in char_list:
    # res_dict.setdefault(car, {}).add(char_list.count(car))
    if car in res_dict:
    if type(item) in dickt_res:
        dickt_res[type(item)].append(item)
    else:
         dickt_res[type(item)] = [item]

print(res_dict)
