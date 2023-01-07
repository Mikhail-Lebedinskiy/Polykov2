from itertools import product


print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    v1 = z <= y
    v2 = not x
    v3 = v2 <= w
    V1 = v1 and v3
    v1 = z == w
    v2 = y and (not x)
    V2 = v1 or v2
    V = V1 <= V2
    if not V:
        print(x, y, z, w)

