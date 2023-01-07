from itertools import product


def f(x, y, z, q):
    v1 = not x
    v2 = v1 <= y
    v3 = not y
    v4 = v3 == z
    v5 = v2 and v4 and w
    return v5


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if f(x, y, z, w):
        print(x, y, z, w)

#  answer - zyxw