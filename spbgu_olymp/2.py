from tqdm import tqdm


max_count, max_x, max_arr = -1, -1, []
for x in tqdm(range(0, 10000, 1)):
    if x == 0:
        continue
    arr = []
    i = 1
    cost = 10 ** 8
    while cost % 10000 == 0:
        cost = (10000 + (-1) ** i * x) * (cost // 10000)
        arr.append(cost)
        i += 1
    if len(arr) > max_count:
        max_count = len(arr)
        max_x = x
        max_arr = arr.copy()


print(max_count)
print(max_x)
print(max_arr)