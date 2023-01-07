for i in range(1, 100000):
    x = i
    m = 0
    s = 0
    while x > 0:
        d = x % 6
        s += d
        if d > m:
            m = d
        x = x // 6
    if m == 5 and s == 16:
        print(i)
        break