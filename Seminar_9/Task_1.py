"""Задание №1
Создайте функцию-замыкание, которая принимает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. """

def funk_close(digit, level):
    def funk_round():
        # digit = random.randint(min_lim, max_lim)
        att = 0
        while att < level:
            print(f'Веедите число между {1} и {100} у Вас {level} попыток')
            num = int(input())
            att += 1
            if num < 1 or num > 100:
                print(f'Число {num} не в границах интервала {1} {100}')

            elif num < digit:
                print(f'Число {num} меньше загаданного')

            elif num > digit:
                print(f'Число {num} больше загаданного')

            else:
                print(f'правильно компьютер загадывал {num}')
                return True

        else:
            print(f' колическо попыток ичерпано - компьютер загадывал {digit}')
            return False
    return funk_round

if __name__ == '__main__':
    res = funk_close(15, 10)
    res()




