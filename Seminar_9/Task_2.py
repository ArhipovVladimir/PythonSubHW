"""Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов."""

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
