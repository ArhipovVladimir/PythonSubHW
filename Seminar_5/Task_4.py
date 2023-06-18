'''
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку
'''

iter_user = (item for item in range(0, 101, 2) if sum(map(int, str(item))) != 8)
print(*iter_user)

# Вариант без map
iter_user = (item for item in range(0, 101, 2) if (item // 10 + item % 10) != 8)
print(*iter_user)

