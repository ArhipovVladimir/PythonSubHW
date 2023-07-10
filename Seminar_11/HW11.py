"""Задание
Решить задачи, которые не успели решить на семинаре.
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать.
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц"""

class Matrix:
    """Class Matrix"""
    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        return f'{self.mat}'

    def __repr__(self):
        return f'Matrix({self.mat})'

    def __add__(self, other):
        """__add__ Matrix"""

        if len(self.mat) != len(other.mat):
            print('сложение невозможно')
            return self

        list_matrix = []
        for i in range(len(self.mat)):
            list_line = []
            for j in range(len(self.mat[i])):
                list_line.append(self.mat[i][j] + other.mat[i][j])
            list_matrix.append(list_line)
        return Matrix(list_matrix)

    def __mul__(self, other):
        """__mull__ Matrix"""

        if len(self.mat[0]) != len(other.mat):
            print('умножение невозможно')
            return self

        list_matrix = []
        for i in range(len(self.mat)):
            list_line = []
            for j in range(len(self.mat[i])):
                list_line.append(self.mat[i][j] * other.mat[j][i])
            list_matrix.append(list_line)
        return Matrix(list_matrix)



if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 5]])
    print(f'{m1 = }')
    m2 = Matrix([[3, 4, 5],
                 [2, 3, 4],
                 [1, 2, 3]])
    print(f'{m2 = }')
    m3 = m1 + m2
    print(f'{m3 = }')
    m4 = m1 * m2
    print(f'{m4 = }')

