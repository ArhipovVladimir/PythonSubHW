"""
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.

"""
class Animal:
    def __init__(self, name):
        self.name = name

    def get_mame(self):
        return self.name

class Fish(Animal):

    def __init__(self, subm, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subm = subm

    def specif(self):
        if self.subm < 10:
            print("медлководная")
        if 10 < self.subm < 50:
            print("средневодная")
        if self.subm > 50:
            print("губоководная")

class Brids(Animal):

    def __init__(self, wingspan, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.wingspan = wingspan

    def specif(self):
        print(self.wingspan / 2)

class Manals(Animal):

    def __init__(self, monat, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.monat = monat

    def _chec_monat(self):
        self.monat = min(12, self.monat)

    def specif(self):
        if self.monat < 12:
            print('не спит зимой')
        else:
            print('спит зимой')

if __name__ == '__main__':
    f1 = Fish(15, 'карась')
    f2 = Fish(120, 'кит')

    b1 = Brids('Воробой', 10)
    b2 = Brids('Сова', 15)

    m1 = Manals('bar', 8)
    m2 = Manals('Lion', 12)


    print(f1.name)
    print(f2.name)
    print(f1.specif())
    print(f2.specif())