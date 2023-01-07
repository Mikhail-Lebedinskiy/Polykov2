from collections import Counter


with open('9.txt') as file:
    data = []
    for line in file:
        data.append([int(i) for i in line.split()])


answer = 0
for numbers in data:
    if len(set(numbers)) != 4:
        continue
    numb_count = Counter(numbers)
    count = sorted(numb_count.values())
    if count != [1, 1, 2, 2]:
        continue
    sum_1 = 0
    sum_2 = 0
    for key in numb_count:
        if numb_count[key] == 1:
            sum_1 += key
        else:
            sum_2 += key
    if sum_1 < sum_2:
        answer += 1
        print(numbers)

print('*' * 100)
print(answer)



