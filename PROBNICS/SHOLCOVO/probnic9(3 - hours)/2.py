from itertools import product


print('a b c F')
for a, b, c in product([0, 1], repeat=3):
    v1 = a and b
    v2 = (not a) or b
    v3 = c and v2
    V = v1 or v3
    print(b, c, a, int(V))
