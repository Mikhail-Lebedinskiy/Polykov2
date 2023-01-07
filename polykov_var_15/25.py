from math import log



right = 3 * 10 ** 8
left = 10 ** 8
for m in range(0, int(log(right, 2)), 2):
    for n in range(1, int(log(right, 7)), 2):
        if left <= 2 ** m * 7 ** n <= right:
            print(2 ** m * 7 ** n, n + m)