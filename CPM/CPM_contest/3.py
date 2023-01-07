from itertools import accumulate
N, K = [int(i) for i in input().split()]
partial_sums = list(accumulate([0] + [int(i) for i in input().split()]))
partial_sums_set = set(partial_sums)
answer = 0
for sum in partial_sums:
    if sum + K in partial_sums_set:
        answer += 1
print(answer)

