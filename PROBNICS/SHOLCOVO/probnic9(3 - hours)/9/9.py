with open('9.txt') as file:
    data = []
    for line in file:
        lst = [int(i) for i in line.split()]
        data.append(lst)

answer = 0
for string in data:
    if len(set(string)) < len(string):
        if sum(set(string)) % 2 == 1:
            print(string)
            answer += 1
print(answer)