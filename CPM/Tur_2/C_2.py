from collections import Counter

max_number = 4000
number_of_blocks = int(input())
lens_of_blocks = sorted([int(i) for i in input().split()])

d = [[0] * (max_number + 1) for i in range(len(lens_of_blocks))]


dd = [{}]
for i in range(max_number + 1):
    if lens_of_blocks[0] > i:
        dd[0][i] = 1
    else:
        dd[0][i] = 0


for i in range(1, len(lens_of_blocks)):
    dd.append(dd[i - 1].copy())
    for j in range(max_number + 1):
        if lens_of_blocks[i] > j:
            dd[i][j] += 1

for i in range(max_number + 1):
    if lens_of_blocks[0] > i:
        d[0][i] += 1

for i in range(1, len(lens_of_blocks)):
    for j in range(max_number + 1):
        d[i][j] = d[i - 1][j]
        if j - lens_of_blocks[i] >= 0:
            d[i][j] += d[i - 1][j - lens_of_blocks[i]]
        else:
            d[i][j] += d[i - 1][0] + 1


mod = 10 ** 9 + 7
answer = 0
for i in range(2, len(lens_of_blocks)):
    answer += (d[i - 1][lens_of_blocks[i]] - dd[i - 1][lens_of_blocks[i]]) % mod

print(answer)