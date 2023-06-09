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
for i in list_hand:
    if list_hand.count(i) == 1:
        list_unik2.append(i)

print(f'{list_unik2 = }')
print(len(list_unik2))


