from itertools import product


answer = 0
for number in product('012345678', repeat=6):
    number_str = ''.join(number)
    if number_str[0] == '0':
        continue
    count_of_4 = 0
    count_of_odd = 0
    for deg in number_str:
        if deg == '4':
            count_of_4 += 1
        if deg in '1357':
            count_of_odd += 1
    if count_of_odd == 2 and count_of_4 == 1:
        print(number_str)
        answer += 1


print(answer)