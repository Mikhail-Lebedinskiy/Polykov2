from tqdm import tqdm


answer = 0
for i in range(2 ** 64):
    if i & 1365 == 1365 and i & 682 == 682:
        answer += 1
print(answer)