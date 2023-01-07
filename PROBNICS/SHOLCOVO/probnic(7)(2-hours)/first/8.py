from itertools import product
from tqdm import tqdm


answer = 0
for number in tqdm(product('0123456789', repeat=8)):
    if number[-1] != '0' and number[-1] != 5:
        continue
    if number[0] == '0':
        continue
    if len(number) != len(set(number)):
        continue
    for i in range(1, 8):
        if number[i] in '13579' and number[i - 1] in '13579':
            break
        if number[i] in '02468' and number[i - 1] in '02468':
            break
    else:
        answer += 1
print(answer)