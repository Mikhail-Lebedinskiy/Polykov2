from tqdm import tqdm


file = open('27(4724)_data/27(4724)(B).txt')
nums_71 = {}
nums_not_71 = []
i = 0
for num in file:
    num_int = int(num.strip())
    if num_int % 71 == 0:
        nums_71[i] = num_int
    else:
        nums_not_71.append(num_int)
    i += 1


products = set()
additive = set()
answer = 0

for num_71_index, num_71 in tqdm(nums_71.items()):
    for num_not_71 in nums_not_71:
        if num_71 * num_not_71 in products:
            # print('AA', num_71, num_not_71)
            additive.add(num_71 * num_not_71)
            answer += 1
        else:
            products.add(num_71 * num_not_71)
    for second_num_71_index, second_num_71 in nums_71.items():
        if num_71_index >= second_num_71_index:
            continue
        if num_71 * second_num_71 in products:
            # print(num_71, second_num_71)
            additive.add(num_71 * second_num_71)
            answer += 1
        else:
            products.add(num_71 * second_num_71)

print(answer + len(additive))
