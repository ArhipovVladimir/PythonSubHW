#решение квадратного уравнения

def get_sqr(**kwargs):

    a, b, c = map(int, kwargs.values())
    if a == 0:
        return 0, 0, 0
    diskrim = b ** 2 - 4 * a * c
    x1 = (- b + (diskrim ** 0.5)) / (2 * a)
    x2 = (- b - (diskrim ** 0.5)) / (2 * a)
    return diskrim, x1, x2


if __name__ == '__main__':
    print(get_sqr(a='2', b='-11', c='-67'))
    print(get_sqr(a='0', b='-11', c='-67'))


