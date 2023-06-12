'''Pflfybt # 1
 Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
'''

def sort_word (words):
    for number, word in enumerate(sorted(words.split()), start=1):
        print(f'{number} {word}')

sort_word('Напишите функцию, которая принимает строку текста.'
          'Вывести функцией каждое слово с новой строки.'
          '✔ Строки нумеруются начиная с единицы.'
          '✔ Слова выводятся отсортированными согласно кодировки Unicode.'
          '✔ Текст выравнивается по правому краю так, чтобы у самого'
          'длинного слова был один пробел между ним и номером строки.')