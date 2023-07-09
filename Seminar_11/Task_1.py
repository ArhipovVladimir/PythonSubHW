"""
Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)

"""
import time


class My_str(str):

    def __new__(cls, value, autor):
        intance = super().__new__(cls, value)
        intance.autor = autor
        intance.date_gen = time.time()
        return intance

    def __init__(self, text, autor):
        self.text = text
        self.autor = autor


    def __str__(self):
         return f'{self.text} автор - {self.autor} написал в {self.date_gen}'


if __name__ == '__main__':

    m_str = My_str("Я сказал так ", "Архипов ВС")
    print(m_str)
