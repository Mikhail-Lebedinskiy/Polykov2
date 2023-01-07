
min_num = 10 ** 3
for x in range(1, 100):
    for y in range(1, 100):
        if 3 * x + y == 60:
            min_num = min(min_num, max(x, y))
print(min_num)