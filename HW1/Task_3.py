# задача 4
#4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

MIN_LIMIT = 0
MAX_LIMIT = 1000

digit = randint(MIN_LIMIT, MAX_LIMIT)

count = 10

while count > 0:
    print(f'Веедите число между {MIN_LIMIT} и {MAX_LIMIT} у Вас {count} попыток')
    num = int(input())
    if num < MIN_LIMIT or num > MAX_LIMIT:
        print(f'Число {num} не в границах интервала {MIN_LIMIT} {MAX_LIMIT}')
        count -= 1
    elif num < digit:
        print(f'Число {num} меньше загаданного')
        count -= 1
    elif num > digit:
        print(f'Число {num} больше загаданного')
        count -= 1
    else:
        print(f'правильно компьютер загадывал {num}')
        break
else:
    print(f' колическо попыток ичерпано - компьютер загадывал {digit}')
    quit()
