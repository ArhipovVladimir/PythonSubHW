"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так,
 чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
 определите, есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

__all__ = ['eight_queens']


def eight_queens(pozis):
    # chech = pozis[1:]
    # print(chech)
    # print(pozis)
    pivot = 0
    for x0, y0 in pozis:
        pivot += 1
        for x1, y1 in pozis[pivot:]:
            if x0 == x1 or y0 == y1 or abs(x0 - x1) == abs(y0 - y1):
                # print(f'точка 0 - ({x0} {y0})')
                # print(f'точка 1 - ({x1} {y1})')
                # print('stop')
                return False
    return True
#     for pivot in range(len(pozis)):
#         for point in range(pivot + 1, len(pozis)):
#             # print(f' pivot {pozis[pivot][0], pozis[pivot][1]}')
#             # print(f' pozis {pozis[point][0], pozis[point][1]}')
#             # print(f' step  = {step}')
#             # step += 1
#
#
#
#             if pozis[pivot][0] == pozis[point][0] or pozis[pivot][1] == pozis[point][1]\
#                     or abs(pozis[pivot][0] - pozis[point][0]) == abs(pozis[pivot][1] - pozis[point][1]):
#                 print('stop')
#                 return False
#     return True
#

if __name__ == '__main__':
    variant = [[8, 4], [1, 5], [6, 8], [3, 1], [2, 3], [4, 7], [5, 2], [7, 6]]
    eight_queens(variant)

# проверка на вертикали - происходит по координатам что бы не было одинаковых значений иксов и ъигриков
#  провкрка на диагонали приосходика как разница абсолютного значения между кординатами икс и игрик одной точки
# и икс игрик дпцгой точка например точка [8, 6] и точка [4, 2]
