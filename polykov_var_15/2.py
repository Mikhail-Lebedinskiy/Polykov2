from itertools import product


print("x y z w")
for x, w, y, z in product((0, 1), repeat=4):
    v1 = x <= w
    v2 = y <= (not z)
    if not((v1 or y and not z) and (v2 or x and not w)):
        print(x, y, z, w)

"""zwyx"""