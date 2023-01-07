from itertools import product
from tqdm import tqdm


answer = 0
for A in tqdm(range(-10000, 10000)):
    for x, y in product(range(0, 1000), repeat=2):
        v1 = x > 8
        v2 = (x**2 + 3 * x) >= A
        v3 = (y ** 2 + 5 * y) > A
        v4 = y >= 4
        if not((v1 <= v2) and (v3 <= v4)):
            break
    else:
        answer += 1
# 85
print(answer)
