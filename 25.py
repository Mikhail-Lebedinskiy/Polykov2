def min_del(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i


len_data = 800000 * 5
data = [0] * len_data
data[0] = 1
data[1] = 1
for i in range(len_data):
    if not(data[i]):
        for j in range(i, len_data, i):
            if not(data[j]):
                data[j] = i


j = 0
for i in range(800000, len_data):
    if j == 5:
        break
    if data[i] != i and (data[i] + i / data[i]) % 138 == 0:
        print(i)
        j += 1

