from math import ceil

a, b, h, w = [int(i) for i in input().split()]
answer = ceil(h / a) * ceil(w / b)
print(answer, end='')
