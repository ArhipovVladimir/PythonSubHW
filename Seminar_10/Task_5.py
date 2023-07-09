"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""

class Fish:

    def __init__(self, name, subm):
        self.name = name
        self.subm = subm

    def specif(self):
        if self.subm < 10:
            print("медлководная")
        if 10 < self.subm < 50:
            print("средневодная")
        if self.subm > 50:
            print("губоководная")

class Brids:

    def __init__(self, name, wingspan):
        self.name= name
        self.wingspan = wingspan

    def specif(self):
        print(self.wingspan / 2)

class Manals:

    def __init__(self, name, monat):
        self.name = name
        self.monat = monat

    def _chec_monat(self):
        self.monat = min(12, self.monat)

    def specif(self):
        if self.monat < 12:
            print('не спит зимой')
        else:
            print('спит зимой')

if __name__ == '__main__':
    f1 = Fish('карась', 15)
    f2 = Fish('кит', 120)

    b1 = Brids('Воробой', 10)
    b2 = Brids('Сова', 15)

    m1 = Manals('bar', 8)
    m2 = Manals('Lion', 12)

    f2.specif()
    f1.specif()
    b1.specif()
    b2.specif()
    m1.specif()
    m2.specif()
    print(f1.name)
    print(f2.name)



