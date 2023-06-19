'''
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def gen_fibo(num):
    if num == 0:
        yield 0
    elif num == 1:
        yield 1
    f1 = 0
    f2 = 1
    for _ in range(num):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        yield f3



fibo_user = gen_fibo(20)
print(*fibo_user)




