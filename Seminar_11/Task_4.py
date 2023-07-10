"""
Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""

class Archive:
    """"Мой трен6ировоный класс"""

    list_num = []
    list_str =[]

     # def __new__(cls, *args, **kwargs):
     #      intanse = super().__new__(cls, *args, **kwargs)
     #      intanse.list_arhive.append(*args, **kwargs)
     #      return intanse

    def __init__(self, number, strg):
        """добавление экземпляра в класс"""
        self.number = number
        self.strg = strg
        self.list_num.append(number)
        self.list_str.append(strg)

    def __str__(self):
        return f' текущий экземпляр {self.number} Архивы {self.list_str} и {self.list_num}'

    def __repr__(self):
        return f'Arhive({self.number}, {self.strg})'


if __name__ == '__main__':
    i = Archive(5, 'grhdsq')
    print(i)
    print(f'{i = }')
    i2 = Archive(6, '120000')
    print(i2)
    print(f'{i2 = }')



    # i3 = Archive(7)
    # print(i3)
    # print(i3.list_arhive)
