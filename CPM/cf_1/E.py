def f1(a, b, c):
    bi = (c - a)

    ai = bi * (b - a)

    for i in range(a - 1):
        _ = 1 + ai * (b - c - 1) + (c - a + 1) + 1
        print(_, _, _ * 2)

    cur1 = 1
    cur2 = 1 + bi
    for i in range(b - a):
        print(cur1, cur2, cur1 + cur2)
        cur2 += bi
        if i < b - c - 1:
            cur1 += ai
        else:
            cur1 += 1

    print(1 + ai * (b - c - 1) + (c - a + 1), 1, ai * (b - c - 1) + (c - a + 1) + 2)


def f2(a, b, c):
    bi = (c - a)

    ai = bi * (b - a)

    for i in range(a - 1):
        _ = 1 + ai * (b - c - 1) + (c - a + 1) + 1
        print(_, _, _ * 2)

    cur1 = 1
    cur2 = 1 + bi
    for i in range(b - a):
        print(cur2, cur1, cur1 + cur2)
        cur2 += bi
        if i < b - c - 1:
            cur1 += ai
        else:
            cur1 += 1

    print(1, 1 + ai * (b - c - 1) + (c - a + 1), ai * (b - c - 1) + (c - a + 1) + 2)



a, b, c = [int(i) for i in input().split()]


if c > a and c > b:
    print(-1)
    exit(0)

if c < a and c < b:
    print(-1)
    exit(0)

if a < b:
    f1(a, b, c)
else:
    f2(b, a, c)




