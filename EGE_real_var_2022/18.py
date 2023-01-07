def DEL(n, m) -> bool:
    return n % m == 0


for A in range(1, 1000):
    for x in range(1, 1000):
        v1 = DEL(x, 2)
        v2 = (not (DEL(x, 3)))
        v3 = x + A >= 80
        if not ((v1 <= v2) or v3):
            break
    else:
        print(A)
        break