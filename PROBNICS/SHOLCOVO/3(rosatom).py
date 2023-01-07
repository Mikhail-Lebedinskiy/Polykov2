from itertools import product


answer = 0
for x, y in product(range(1, 10 ** 3), repeat=2):
    if (x + y) ** 2 + 3 * x + y == 2021 * 2:
        print(x, y)
        answer += (x + y)

print(answer)
print((5 + 58) ** 2 + 3 * 5 + 58)