# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
for i in range(n, 10):
    for j in range(n, 10):
        print(f'{i} x {j} = {i*j}')
    print()