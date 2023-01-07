from collections import Counter
from math import log2


def f(number):
    deg_of_2 = 0
    while number % 2 == 0:
        number //= 2
        deg_of_2 += 1
    return deg_of_2, number


n = int(input())
numbers_counter = Counter([int(i) for i in input().split()])
simple_numbers_counter = Counter()

for number, count in numbers_counter.items():
    deg_of_2, simple_number = f(number)
    simple_numbers_counter[simple_number] += count * 2 ** deg_of_2


max_number = 0
for simple_number, count in simple_numbers_counter.items():
    max_number = max(max_number, 2 ** int(log2(count)) * simple_number)

print(max_number)