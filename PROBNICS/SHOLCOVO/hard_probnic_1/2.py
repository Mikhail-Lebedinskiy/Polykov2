from itertools import product


def XOR(x, y):
    if (x or y) and x != y:
        return True
    return False


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    v1 = x or (not y)
    v2 = XOR(not x, y)
    v3 = z == v2
    v4 = (not w) <= v3
    v5 = v1 == v4
    if not v5:
        print(x, y, z, w)
