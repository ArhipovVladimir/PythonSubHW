'''Pflfybt # 1
 Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
'''

def kod_word (text_str):

    text_sort = text.split()
    text_sort.sort()
    print(text)
    print(f'{text_sort =}')
    point = len(max(text_sort, key=len))
    for number, word in enumerate(text_sort, start=1):
        print(f'{number} {word:>{point}}')


text = input('Введите текст: ')
kod_word (text)