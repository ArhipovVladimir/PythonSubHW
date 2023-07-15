"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.

"""

from collections import defaultdict
from math import factorial
class Factorial:
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        results = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return results

    def __call__(self, value):
        self.storage[value].append(factorial(value))


if __name__ == '__main__':
     f1 = Factorial()
     print(f1(5))
     print(f1(12))
    # print(factorial(5))