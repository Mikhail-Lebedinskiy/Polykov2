string = open('data/Задание 24/24.txt').readline().strip()
last_digit = -1
len_of_sequence = 0
answer = 0

for digit in string:
    if int(digit) > last_digit:
        last_digit = int(digit)
        len_of_sequence += 1
    else:
        if len_of_sequence == 5:
            answer += 1
        len_of_sequence = 0
        last_digit = -1
print(answer)
