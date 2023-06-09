"""
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
"""
import random

list_hand = []

for _ in range(30):
    list_hand.append(random.randint(-10, 10))

# list_hand2 = random.sample(range(1, 1100), 20)

print(f'{list_hand = }')
print(len(list_hand))

list_unik = list(set(list_hand))

print(f'{list_unik = }')
print(len(list_unik))

list_unik2 = []
for elem in list_hand:
    if list_hand.count(elem) == 1:
        list_unik2.append(elem)

print(f'{list_unik2 = }')
print(len(list_unik2))

list_unik3 = []
for elem in list_hand:
    if elem not in list_unik3:
        list_unik3.append(elem)

print(f'{list_unik3 = }')
print(len(list_unik3))

