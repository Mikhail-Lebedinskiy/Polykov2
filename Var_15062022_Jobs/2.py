from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    v1 = (not x) <= y
    v2 = (not y) == z
    if v1 and v2 and w:
        print(x, y, z, w)
