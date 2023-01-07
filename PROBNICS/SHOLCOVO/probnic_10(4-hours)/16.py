from functools import lru_cache
MOD = 10 ** 4


@lru_cache(None)
def F(a, x):
    if x == 1:
        return a % MOD
    if x % 2 == 1:
        return a * F(a, x - 1) % MOD
    return F(a, x // 2) ** 2 % MOD


answer = 0
for i in range(2, 10 ** 4 + 1):
    answer = (answer + F(i, i)) % MOD

print(answer)


