'''

Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так,
 чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
 определите, есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

'''
def eight_queens (posiz):
    print (len(posiz))
    for pivot in range(len(posiz)):
        for point in range(pivot + 1, len(posiz)):
            print(posiz[pivot])
            print(posiz[point])
            if posiz[pivot][0] == posiz[point][0] or posiz[pivot][1] == posiz[point][1] \
                    or abs(posiz[pivot][0] - posiz[pivot][1]) == abs(posiz[point][0] - posiz[point][1]):
                print('stop')
                return False
    print('OK')
    return True


        
if __name__ == '__main__': 
    variant = [[1, 2], [2, 4], [8, 5], [4, 7], [8, 1], [7, 4], [3, 8], [3, 1]]
    eight_queens(variant)
    

# if  pivot [0] == point [0] \
            #         or pivot [1] == point [1] \
            #         or abs (pivot[0] - point[0]) == abs (pivot [1] - point [1]):
            #         correct = False
