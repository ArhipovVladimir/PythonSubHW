"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json
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

    def __enter__(self):
       return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        f_json = open('file_json.json', 'w', encoding='utf-8')
        json.dump(self._histoty, f_json)
        f_json.close()

if __name__ == '__main__':

     fact = Factorial(5)
     with fact:
        for i in range(3, 10):
            fact(i)
            fact.get_history()