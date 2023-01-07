def DEL(x: int, a: int) -> bool:
    return x % a == 0


for A in range(10000):
    if A == 0:
        continue
    for x in range(10000):
        v1 = (not DEL(x, 84))
        v2 = (not DEL(x, 90))
        v3 = (not DEL(x, A))
        if not ((v1 or v2) <= v3):
            print(x, A)
            print(v1)
            print(v2)
            print(v3)
            break
    else:
        print(A)
        break