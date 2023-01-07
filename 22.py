for i in range(10000, 0, -1):
    x = i
    L, M = 0, 0
    while x > 12:
        L = L + 1
        x = x // 4
        M = x
    if L > M:
        L, M = M, L
    if L == 3 and M == 7:
        print(i)
        break