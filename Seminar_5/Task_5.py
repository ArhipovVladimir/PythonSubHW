'''
Задание №5
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.

'''

MIN = 1
MAX = 101
def get_chr(min, max):
    for item in range(min, max):
        if item % 3 == item % 5 == 0:
            yield 'FizzBuzz'
        elif item % 3 == 0:
            yield 'Fizz'
        elif item % 5 == 0:
            yield 'Buzz'
        else: yield item


iter_user1 = get_chr(MIN, MAX)
print(*iter_user1)

# через многострочный генератор

iter_user2= ("FizzBuzz" if item % 15 == 0 else\
            "Fizz" if item % 3 == 0 else\
            "Buzz" if item % 5 == 0 else  item for item in range(MIN, MAX))

print(*iter_user2)
