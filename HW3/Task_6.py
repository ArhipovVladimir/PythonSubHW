"""Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки."""

text = input('Введите текст: ')
text_sort = text.split()
text_sort.sort()
print(text)
print(f'{text_sort =}')
point = len(max(text_sort))
for number, word in enumerate(text_sort, start=1):
    print(f'{number} {word:>{point}}')
