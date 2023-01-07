from math import prod

answer = -1
for i in range(175, 1239875):
    answer = max(answer, prod([int(j) for j in str(i)]))
print(answer)