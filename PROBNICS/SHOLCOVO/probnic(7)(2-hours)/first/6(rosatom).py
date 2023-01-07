from math import prod

answer = 0
for i in range(10, 100):
    for j in range(i + 1, 100):
        if not(i <= 77 and j >= 77):
            answer += 1
print(answer)