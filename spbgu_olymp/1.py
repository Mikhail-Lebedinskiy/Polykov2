from itertools import permutations
from tqdm import tqdm


s = '++222222222'
answer = set()
for n in tqdm(list(permutations(s))):
    s_str = ''.join(n)
    if s_str[0] == '+':
        continue
    if s_str[-1] == '+':
        continue
    if '++' in s_str:
        continue
    arr = [int(i) for i in s_str.split('+')]
    answer.add(sum(arr))

print(answer)
print(len(answer))
