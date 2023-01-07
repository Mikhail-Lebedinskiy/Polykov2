from itertools import product


def f(a, b):
    len_a, len_b = len(a), len(b)
    if len_a < len_b:
        return a == b[:len_a]
    else:
        return a[:len_b] == b


def g(a, b):
    len_a, len_b = len(a), len(b)
    if len_a < len_b:
        return a == b[len_b - len_a:]
    else:
        return a[len_a - len_b:] == b


cods = ['00', '1001', '0101', '111']

for cod1 in product(['0', '1'], repeat=2):
    for cod2 in product(['0', '1'], repeat=2):
        for cod in cods:
            if f(''.join(cod1), cod) or f(''.join(cod2), cod):
                break
        else:
            print(cod1)
            print(cod2)

for cod1 in product(['0', '1'], repeat=2):
    for cod2 in product(['0', '1'], repeat=3):
        for cod in cods:
            if g(''.join(cod1), cod) or g(''.join(cod2), cod):
                break
        else:
            print(cod1)
            print(cod2)