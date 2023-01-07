def DEL(n, m):
    return n % m == 0


for A in range(10000, 0, -1):
    for x in range(1, 10 ** 4):
        v1 = not DEL(x, A)
        v2 = not(DEL(96, x))
        v3 = DEL(x, 24) <= v2
        V = v1 <= v3
        if not V:
            break
    else:
        print(A)
        break
