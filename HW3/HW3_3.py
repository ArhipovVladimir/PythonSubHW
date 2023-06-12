'''Создайте словарь со списком вещей для похода в качестве ключа
и их массой в качестве значения. Определите какие вещи влезут в рюкзак
передав его максимальную грузоподъёмность. Достаточно вернуть один
допустимый вариант. *Верните все возможные варианты комплектации рюкзака.'''

stuff = {'матрас': 1, 'кострюля': 2, 'палатка': 3, 'обувь': 5, 'одеяло': 3}

def backpack(capacity, stuff):
    packaging = []
    for item, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging.append(item)
    return packaging


print(f' возможный комплект: {backpack(10, stuff)}')