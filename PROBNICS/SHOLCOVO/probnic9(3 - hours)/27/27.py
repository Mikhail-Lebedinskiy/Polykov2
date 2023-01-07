with open('27B.txt') as file:
    N = int(file.readline())
    numbers = []
    for line in file:
        numbers.append(int(line))

d = {i: -1 for i in range(-1000000, 1000001)}
odd_sum = 0
even_sum = 0
max_sum = -1
for i, number in enumerate(numbers):
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
    if d[even_sum - odd_sum] == -1:
        d[even_sum - odd_sum] = even_sum + odd_sum
    r = even_sum - odd_sum
    if d[r] != -1:
        cur_sum = even_sum + odd_sum - d[r]
        max_sum = max(max_sum, cur_sum)
print(max_sum)

