with open('17__x9cc.txt') as file:
    numbers = [i.strip() for i in file]

answer = []
for i in range(1, len(numbers)):
    if numbers[i][-1] == numbers[i - 1][-1] and int(numbers[i][-1]) % 2 == 1:
        answer.append(abs(int(numbers[i]) * int(numbers[i - 1])))

print(len(answer))
print(max(answer))
