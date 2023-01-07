for i in range(-1000, 1000):
    x = i
    s = 1
    a = 11
    while x // 7 > 0:
        if x % 7 < 4:
            s = s + a
        else:
            s = s + (x % 7)
        x = x // 7
    if s == 27:
        print(i)
        break