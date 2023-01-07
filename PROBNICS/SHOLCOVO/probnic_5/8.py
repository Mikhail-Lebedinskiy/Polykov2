from itertools import product


answer = 0
for number in product([0, 1, 2, 3], repeat=3):
    if number[0] == 0:
        continue
    for i in range(1, 3):
        if number[i] > number[i - 1]:
            break
    else:
        answer += 1
        print(number)


print(answer)