from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    v1 = (not (w <= z))
    v2 = x <= y
    v3 = (not x)
    if not(v1 or v2 or v3):
        print(x, y, z, w)
