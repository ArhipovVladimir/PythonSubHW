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
# c count
# text = input('Введите текст: ')
# text = text.replace(' ', '').replace(',', '').lower()
# res_dict = {}
# for car in text:
#     res_dict.setdefault(car, text.count(car))
#
# print(res_dict)

# без count

#
text = input('Введите текст: ')
text = text.replace(' ', '').replace(',', '').lower()
char_list = [char for char in text]
res_dict = {}
char_list.sort()
print(char_list)
count = 1
for i in range(1, len(text)):
    if char_list[i] != char_list[i-1]:
        res_dict[char_list[i-1]] = count
        count = 1
    else:
        count += 1

count = 1
for i in range(len(char_list)-1, 0, -1):
    if char_list[i] == char_list[i-1]:
       count += 1
    else:
        res_dict[char_list[i]] = count
        break


print(res_dict)

