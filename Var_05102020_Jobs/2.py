from itertools import product


print('a b c d')
for a, b, c, d in product([0, 1], repeat=4):
    v1 = (a <= d)
    v2 = (not(b <= c))
    if v1 and v2:
        print(a, b, c, d)
