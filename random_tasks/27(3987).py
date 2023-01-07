min_1_0 = 10 ** 5
min_0_1 = 10 ** 5
min_1_1 = 10 ** 5

file = open('27(3987)_data/27(3987)(B).txt')

answer = 0
sum_max_numbers = 0
sum_min_numbers = 0
for i in file:
    num_1, num_2 = (int(j) for j in i.strip().split())
    if num_1 % 2 == 0:
        continue
    num_max, num_min = max(num_1, num_2), min(num_1, num_2)
    sum_of_numbers = num_max + num_min
    answer += sum_of_numbers
    sum_max_numbers += num_max
    sum_min_numbers += num_min

    if num_max % 2 == 1 and num_min % 2 == 0:
        if min_1_0 > sum_of_numbers:
            min_1_0 = sum_of_numbers

    if num_max % 2 == 0 and num_min % 2 == 1:
        if min_0_1 > sum_of_numbers:
            min_0_1 = sum_of_numbers

    if num_max % 2 == 1 and num_min % 2 == 1:
        if min_1_1 > sum_of_numbers:
            min_1_1 = sum_of_numbers


# 1, 0
print(min_1_1, min_1_0, min_0_1)
if sum_max_numbers % 2 == 0 and sum_min_numbers % 2 == 0:
    print(sum_max_numbers, sum_min_numbers)
    first_answer = answer - min_1_0
    second_answer = answer - min_1_1 - min_0_1
    print(max(first_answer, second_answer))

if sum_max_numbers % 2 == 1 and sum_min_numbers % 2 == 0:
    print(sum_max_numbers, sum_min_numbers)
    print(answer)

if sum_max_numbers % 2 == 0 and sum_min_numbers % 2 == 1:
    print(sum_max_numbers, sum_min_numbers)
    first_answer = answer - min_1_1
    second_answer = answer - min_1_0 - min_0_1
    print(max(first_answer, second_answer))

if sum_max_numbers % 2 == 1 and sum_min_numbers % 2 == 1:
    print(sum_max_numbers, sum_min_numbers)
    first_answer = answer - min_0_1
    second_answer = answer - min_1_1 - min_1_0
    print(max(first_answer, second_answer))

