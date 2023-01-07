from collections import Counter


number_of_blocks = int(input())
lens_of_blocks = Counter([int(i) for i in input().split()])
keys = sorted(lens_of_blocks.keys(), reverse=True)
keys_ = keys[::-1]

max_number = 20
d = [[0] * max_number for i in range(len(keys))]
dd = {i: 0 for i in range(1, max_number + 1)}
for i in range(len(keys)):
    for j in range(1, keys[i]+1):
        dd[j] += 1


for i in range(max_number):
    for j in range(lens_of_blocks[keys_[0]]):
        if keys_[0] * (j + 1) > i + 1:
            d[0][i] += 1

for i in range(1, len(keys_)):
    for j in range(max_number):
        d[i][j] = d[i - 1][j]
        for l in range(lens_of_blocks[keys_[i]]):
            if j - keys_[i] * (l + 1) + 1 >= 0:
                d[i][j] += d[i - 1][j - keys_[i] * (l + 1) + 1]
            else:
                d[i][j] += d[i - 1][0] + 1

mod = 10 ** 9 + 7
answer = 0
curr_number_of_blocks = number_of_blocks
for i in range(len(keys)):
    if lens_of_blocks[keys[i]] > 1:
        answer = (answer + 2 ** (number_of_blocks - 2) - 1) % mod
    answer += (d[len(keys) - i - 1][keys[i] - 1] - dd[keys[i]]) % mod


print(answer)




