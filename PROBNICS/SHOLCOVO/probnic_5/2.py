from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    v1 = x <= y
    v2 = not w
    if v1 and z and v2:
        print(x, y, z, w)