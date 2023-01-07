for i in range(1000, 1, -1):
    s, n = 0, 0
    d = i
    while s < 111:
        s += 8
        n += d
    if n == 28:
        print(i)
        break
