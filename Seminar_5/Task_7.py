'''
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''
START = 2
def gen_prost(start, n):
    count = 0
    for i in range(start, n):
        if n % i == 0:
            count += 1
    if count > 1:
        yield i

t = int(input('введите число: '))
iter_prost = gen_prost(START, t)
print(*iter_prost)

