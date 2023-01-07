from itertools import product


numbers = product('01234567', repeat=4)


answer = 0
for num in numbers:
    number = ''.join(num)
    if int(number, 8) % 4 == 0:
        answer += 1

print(answer)
