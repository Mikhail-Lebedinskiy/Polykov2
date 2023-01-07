def f(a, b, c, d):
    if c < a < d and not(c < b < d):
        return True
    if c < b < d and not(c < a < d):
        return True
    return False


with open('17.txt') as file:
    numbers = [int(i) for i in file]

min_37 = 10 ** 5
max_73 = -1

for number in numbers:
    if number % 37 == 0:
        min_37 = min(min_37, number)
    if number % 73 == 0:
        max_73 = max(max_73, number)

print(min_37, max_73)
answer = []
for i in range(1, len(numbers)):
    if f(numbers[i - 1], numbers[i], max_73, min_37):
        answer.append(numbers[i - 1] + numbers[i])


print(len(answer))
print(min(answer))