from math import ceil, sqrt


def f(max_el):
    n = (1 + sqrt(1 + 8 * max_el)) / 2
    if n % 1 == 0:
        return int(n) + 1
    return ceil(n)


count_of_confus = int(input())

arr = []
for i in range(count_of_confus):
    arr.append(int(input()))


for el in arr:
    n = f(el)
    all_sum = n * (n - 1) // 2
    print(all_sum - el)