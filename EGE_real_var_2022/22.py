for i in range(10000, 1, -1):
    x = i
    Q = 6
    P = 10
    K1 = 0
    K2 = 0
    while x <= 100:
        K1 += 1
        x = x + P
    while x >= Q:
        K2 = K2 + 1
        x = x - Q
    L = x + K1
    M = x + K2
    if L == 8 and M == 21:
        print(i)
        break
