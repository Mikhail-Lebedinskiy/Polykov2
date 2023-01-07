def DEL(x, y):
    return x % y == 0


for A in range(1, 10 ** 4):
    for x in range(1, 10 ** 5):
        v1 = DEL(72, x)
        v2 = not DEL(90, x)
        v3 = v1 <= v2
        v4 = (A - x) > 80
        v5 = v3 or v4
        if not v5:
            break
    else:
        print(A)
        break