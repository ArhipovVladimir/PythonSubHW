"""
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
"""

class Archive:
    list_num = []
    list_str =[]

     # def __new__(cls, *args, **kwargs):
     #      intanse = super().__new__(cls, *args, **kwargs)
     #      intanse.list_arhive.append(*args, **kwargs)
     #      return intanse

    def __init__(self, number, strg):
        self.number = number
        self.strg = strg
        self.list_num.append(number)
        self.list_str.append(strg)


if __name__ == '__main__':
    i = Archive(5, 'grhdsq')
    print(f'{i}')
    print(i.list_str, i.list_num)
    i2 = Archive(6, '120000')
    print(i2)
    print(i2.list_num, i2.list_str)
    # i3 = Archive(7)
    # print(i3)
    # print(i3.list_arhive)