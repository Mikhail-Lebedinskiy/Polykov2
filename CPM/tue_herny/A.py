a, b = [int(i) for i in input().split()]

if a > 7:
    print(a - 7)
    exit(0)

x = 14 - a

last_day = b + x

next_day = b
for i in range(7):
    next_day = (next_day + 1) % (last_day + 1)
print(next_day)


"""

3 2 1 30 29 28 27 '26' 25 24 23 22 21 20 '19' 18 17 15

x = 14 - 3 = 11


"""