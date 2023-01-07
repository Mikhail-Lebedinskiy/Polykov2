for i in range(-1000, 1000):
    if i == 0:
        continue
    d = i
    n = 10
    s = 122
    while s // d > 0:
        s = s - d
        n = n + 5
    if n == 60:
        print(i)
        break
