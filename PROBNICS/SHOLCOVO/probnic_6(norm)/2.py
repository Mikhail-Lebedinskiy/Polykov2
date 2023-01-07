from itertools import product


print('x y z')
for x, y, z in product([0, 1], repeat=3):
    v1 = not y
    v2 = x <= v1
    v3 = not z
    v4 = v2 <= v3
    v5 = not y
    v6 = x and v5
    v7 = v4 == v6
    if v7:
        print(x, y, z)
