'''

Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так,
 чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
 определите, есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

'''


def eight_queens (points_queens):
    correct = True
    for pivot in range(len(points_queens)):
        for point in range(pivot + 1, len(points_queens)):
            print()
            if points_queens[pivot][0] == points_queens[point][0] \
                    or  points_queens[pivot][1] == points_queens[point][1] or abs(points_queens[pivot][0] )


            if  pivot [0] == point [0] or pivot [1] == point [1] or abs (pivot[0] - point[0])\
                == abs (pivot [1] - point [1]):
                    correct = False


points = [[1,4], [2,8], [3,5], [6,4], [7,3], [5,2], [4,2]]
eight_queens(points)