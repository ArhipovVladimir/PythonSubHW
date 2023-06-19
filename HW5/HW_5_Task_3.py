'''
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def gen_fibo(num):
    if num == 0:
        yield 0
    f1 = 0
    f2 = 1
    yield 0
    yield 1
    for _ in range(num-2):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        yield f3



fibo_user = gen_fibo(int(input('Enter num: ')))
print(*fibo_user)




