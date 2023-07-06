"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""

class Human:

    def __init__(self, name, surname, patranomic, age):
        self.name = name
        self.surname = surname
        self.patranomic = patranomic
        self.__age = age

    def full_name(self):
        return f'{self.name} {self.surname} {self.patranomic}'

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

if __name__ == '__main__':

    h1 = Human('Ivan', 'Petrov', 'Sidorovich', 25)
    print(h1.full_name())
    print(h1.get_age())
    h1.birthday()
    print(h1.get_age())
    h1.__age = 33
    print(h1.__age)

