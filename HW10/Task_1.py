"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа. Внутри класса создайте экземпляр на основе
переданного типа и верните его из класса-фабрики.

"""

from Task_1_Class import Fish
from Task_1_Class import Brids
from Task_1_Class import Manals


class Get_class:

    def __init__(self, type_cls, *args, **kwargs):
        self.type_cls = type_cls

    def get_amimals(self):

        if 'fish' in self.type_cls:
            return Fish(self)

        if self.type_cls == 'Brids':
            return Brids(self)

        if self.type_cls == 'Manals':
            return Manals(self)

        print("не найден тип")


if __name__ == '__main__':
    animals1 = Get_class.get_amimals('fish')
    # animals2 = Fish('fish', 55)
    # print(animals1)
    # print(animals2)
    # animals1.specif()
    # animals1.name()
