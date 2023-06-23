'''
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''


def gen_fibo(num):
    f1,  f2 = 0, 1
    for _ in range(num):
        yield f1
        f1,  f2 = f2, f1 + f2



fibo_user = gen_fibo(int(input('Enter num: ')))
print(*fibo_user)




