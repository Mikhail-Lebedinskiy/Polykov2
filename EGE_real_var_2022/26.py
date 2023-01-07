numbers = []
with open('data/26/26.txt') as file:
    for line in file:
        number = int(line.strip())
        numbers.append(number)

numbers.sort(reverse=True)

size_of_last_box = 10**5
number_of_box = 0
for size in numbers:
    if size_of_last_box - size >= 3:
        size_of_last_box = size
        number_of_box += 1

print(number_of_box)
print(size_of_last_box)