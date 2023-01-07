file = open('data/17/17.txt')

numbers = []
for line in file:
    number = int(line.strip())
    numbers.append(number)

min_number = min(numbers)
good_pares = []
for i in range(1, len(numbers)):
    if numbers[i] % 117 == min_number or numbers[i - 1] % 117 == min_number:
        good_pares.append(numbers[i] + numbers[i - 1])

print(len(good_pares))
print(max(good_pares))
file.close()
