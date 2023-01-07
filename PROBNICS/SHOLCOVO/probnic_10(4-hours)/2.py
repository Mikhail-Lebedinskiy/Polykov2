from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    v1 = x <= y
    v2 = v1 <= z
    v3 = not w
    if not(v2 or v3):
        print(x, y, z, w)
