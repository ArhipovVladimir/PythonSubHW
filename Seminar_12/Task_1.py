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
    def __init__(self, k):
        self._k = k
        self._histoty = []

    def __call__(self, num):
        self._histoty.append({num: factorial(num)})
        self._histoty = self._histoty[-self._k:]
        return factorial(num)

    def get_history(self):
        return self._histoty



if __name__ == '__main__':
     f = Factorial(3)
     for i in range(3, 10):
         print(f(i))

     print(f.get_history())