from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    return 2 * f(n - 1) + f(n - 2)


print(f(20))

numbers = [0] * 21
numbers[1] = 1
for i in range(2, len(numbers)):
    if i % 2 == 0:
        numbers[i] = i + numbers[i - 1]
    else:
        numbers[i] = 2 * numbers[i - 1] + numbers[i - 2]
print(numbers)
