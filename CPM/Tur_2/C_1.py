from collections import Counter


number_of_blocks = int(input())
lens_of_blocks = Counter([int(i) for i in input().split()])
keys = sorted(lens_of_blocks.keys(), reverse=True)
keys_ = keys[::-1]

max_number = 4000
d = [[0] * max_number for i in range(len(keys))]


dd = [{}]
for i in range(max_number + 1):
    if keys_[0] > i:
        dd[0][i] = 1
    else:
        dd[0][i] = 0


for i in range(1, len(keys)):
    dd.append(dd[i - 1].copy())
    for j in range(max_number + 1):
        if keys_[i] > j:
            dd[i][j] += 1

for i in range(max_number):
    for j in range(lens_of_blocks[keys_[0]]):
        if keys_[0] * (j + 1) > i:
            d[0][i] += 1

for i in range(1, len(keys_)):
    for j in range(max_number):
        d[i][j] = d[i - 1][j]
        for l in range(lens_of_blocks[keys_[i]]):
            if j - keys_[i] * (l + 1) >= 0:
                d[i][j] += d[i - 1][j - keys_[i] * (l + 1)]
            else:
                d[i][j] += d[i - 1][0] + 1


mod = 10 ** 9 + 7
answer = 0
if lens_of_blocks[keys_[0]] > 2:
    answer = lens_of_blocks[keys_[0]] - 2
curr_number_of_blocks = lens_of_blocks[keys_[0]]
for i in range(1, len(keys_)):
    curr_number_of_blocks += lens_of_blocks[keys_[i]]
    if lens_of_blocks[keys_[i]] > 1:
        answer = (answer + 2 ** (curr_number_of_blocks - 2) - 1) % mod
    answer += (d[i - 1][keys_[i]] - dd[i - 1][keys_[i]]) % mod

print(answer)