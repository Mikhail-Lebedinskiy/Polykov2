def f(partial_sums, i, max_len, len_arr):
    while True:
        if i <= max_len + 1:
            return max_len
        if partial_sums[i] - partial_sums[i - max_len - 1] <= len_arr - max_len - 2:
            max_len += 1
        else:
            return max_len


len_arr = int(input())
arr = sorted([int(i) for i in input().split()])

# len_arr = 5
# arr = [-2, 1, 3, 4, 7]

distances = [arr[i] - arr[i - 1] - 1 for i in range(1, len_arr)]
partial_sums = [0] * (len_arr - 1)

curr_sum = distances[0]
partial_sums[0] = distances[0]
if partial_sums[0] <= len_arr - 2:
    max_len = 1
else:
    max_len = 0
for i in range(1, len_arr - 1):
    partial_sums[i] = partial_sums[i - 1] + distances[i]
    if partial_sums[i] <= len_arr - 2 - i:
        max_len = i + 1
# print(partial_sums)

i = max_len + 2
while True:
    max_len = f(partial_sums, i, max_len, len_arr)
    i = max(max_len + 2, i + 1)
    if i >= len_arr - 1:
        break

print(len_arr - max_len - 1)
#
#
# print(distances)
# print(partial_sums)


