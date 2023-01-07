for s in range(10000):
    p = 10
    q = 8
    k1 = 0
    k2 = 0
    ss = s
    while ss <= 100:
        ss = ss + p
        k1 = k1 + 1
    while ss > q:
        ss = ss - q
        k2 = k2 + 1
    k1 += ss
    k2 += ss
    if k1 == 10 and k2 == 19:
        print(s)