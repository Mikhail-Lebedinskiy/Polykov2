from itertools import product


good_numbers = []

for i in range(4):
    for s in product('0123456789', repeat=i):
        number = int('1234' + ''.join(s) + '7')
        if number % 141 == 0:
            good_numbers.append(number)


for number in sorted(good_numbers):
    print(f'{number}_{number // 141}', end='_')
