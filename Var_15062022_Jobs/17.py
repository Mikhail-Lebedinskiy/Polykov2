print('Я тут')
min_103 = 10 ** 10
with open('17.txt') as file:
    numbers = []
    for line in file:
        number = int(line.strip())
        if number % 103 == 0:
            min_103 = min(number, min_103)
        numbers.append(number)
print(numbers)
print(min_103)
answers = []
for i in range(1, len(numbers)):
    x1, x2 = numbers[i], numbers[i - 1]
    if (x1 + x2) % 2 == 0 and abs(x1 - x2) % min_103 == 0:
        answers.append(x1 + x2)

print(len(answers), max(answers))
