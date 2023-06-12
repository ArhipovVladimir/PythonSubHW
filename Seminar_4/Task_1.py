'''Pflfybt # 1
 Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
'''

def sort_word (words):
    words_sort = words.lower().split()
    words_sort.sort()
    point = len(max(words_sort))
    print(point)
    print(words_sort)
    for number, word in enumerate(words_sort, start=1):
        print(f'{number} {word:>{point}}')

sort_word('Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.')
