'''Домашнее Задание

✔ Напишите функцию для транспонирования матрицы'''

matrix = [[1,2,3], [4,5,6], [7,8,9]]


def transp (matr):
    return [*zip(*matr)]


print(matrix)
print(transp(matrix))






