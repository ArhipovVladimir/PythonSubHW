"""
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
"""

class Archive(int):
    list_arhive = []

    def __new__(cls, value):
        intanse = super().__new__(cls, value)
        intanse.list_arhive.append(value)
        return intanse

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    i = Archive(5)
    print(i)
    print(i.list_arhive)
    i2 = Archive(6)
    print(i2)
    print(i2.list_arhive)
    i3 = Archive(7)
    print(i3)
    print(i3.list_arhive)