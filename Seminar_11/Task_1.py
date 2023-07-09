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




if __name__ == '__main__':

    m_str = My_str("Я сказал так ", "Архипов ВС")
    print(m_str)
    print(m_str.upper())
    print(m_str.lower())
    print(m_str.autor)
    print(m_str.date_gen)
