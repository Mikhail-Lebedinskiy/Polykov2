from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return f(n / 2) + 1
    return f(n - 3) + 3


answer = 0
for n in range(1, 10 ** 5 + 1):
    if f(n) == 12:
        answer += 1
print(answer)