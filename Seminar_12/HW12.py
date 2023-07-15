"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых."""

# str.isalpha()
# str.istitle()

class GetFulLName:

    def __set_name__(self, owner, name):
        self.param_name = name

    def __set__(self, instance, value):
        self.validate(value)
        self.param_name = value

    def validate(sels, value):
        if not value.isalpha():
            raise ValueError(f'в строке должны быть только буквы {value}')
        if not value.istitle():
            raise ValueError(f' ФИО не с большой буквы {value}')
class Student:

    name_stud = GetFulLName()
    first_name = GetFulLName()
    def get_predmet(self):

         return
    def __init__(self, name_stud, first_name):
        self.name_stud = name_stud
        self.first_name = first_name
        self.full_name = self.name_stud + self.first_name
        self._predm = self.get_predmet(self.full_name)

    def __str__(self):
        return f'Имя {self.name_stud} Фамилия {self.name_stud}'

if __name__ == '__main__':
    s1 = Student('Иван', 'Петров')
    print(s1)
