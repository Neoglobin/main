def arguments():
    a = float(input('Сторона a: '))
    b = float(input('Сторона b: '))
    c = float(input('Сторона c: '))

    area = heron_formula(a, b, c)
    return area


def heron_formula(a,b,c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

