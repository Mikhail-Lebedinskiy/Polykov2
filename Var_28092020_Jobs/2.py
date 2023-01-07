from itertools import product


print('x y z')
for x, y, z in product([0, 1], repeat=3):
    v1 = x <= y
    v2 = y <= z
    if v1 and v2:
        print(x, y, z)