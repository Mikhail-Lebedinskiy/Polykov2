l = int(input())

n_curr = (2 * l) ** 0.5 // 1

while (n_curr + 1) * (n_curr) / 2 <= l:
    n_curr += 1

print(int(n_curr - 1))

