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
#  c count
# text = input('Введите текст: ')
# text = text.replace(' ', '').replace(',', '').lower()
# char_list = [char for char in text]
# res_dict = {}
# for car in char_list:
#     # res_dict.setdefault(car, {}).add(char_list.count(car))
#     if car not in res_dict:
#           res_dict[car] = text.count(car)
#
# print(res_dict)

# без count

text = input('Введите текст: ')
text = text.replace(' ', '').replace(',', '').lower()
char_list = [char for char in text]
res_dict = {}
char_list.sort()
count = 0
for i in len(char_list) - 1:
    if char_list[i] == char_list [i+1]:
        count += 1
    else:
        res_dict[char_list[i]] = count

print(res_dict)