'''Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''

def code_list(text):
    return sorted((map(ord, set(text))), reverse=True)

print(code_list(input('Enter text: ')))