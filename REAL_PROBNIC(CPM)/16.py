from tqdm import tqdm

def f(n):
    if n == 0:
        return 0
    return f(n - 1) + n


# answer = 0
# for i in tqdm(range(765432010, 1542613234)):
#     if i % 3 == 1:
#         answer += 1

for i in range(50):
    if f(i) % 3 != 0:
        print(i)