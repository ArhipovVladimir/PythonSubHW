'''Домашнее Задание

✔ Напишите функцию для транспонирования матрицы'''

matrix = [[1,2,3], [4,5,6], [7,8,9]]


def transp (matr):

    matr1 = [*zip(*matr)]
    return matr1


print(matrix)
print(transp(matrix))






