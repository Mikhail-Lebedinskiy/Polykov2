from math import ceil
from EGE_real_var_2022.test_27 import get_price_for_number


numbers = []
count_of_boxes = {}
number_of_boxes = 0

with open('data/27/27B.txt') as file:
    for line in file:
        number, count = [int(i) for i in line.strip().split()]
        numbers.append(number)
        count_of_boxes[number] = ceil(count / 36)
        number_of_boxes += ceil(count / 36)

last_price = 0
last_number = numbers[0]
for number in numbers[1:]:
    last_price += count_of_boxes[number] * (number - last_number)


last_number_of_boxes_left = 0
min_price = last_price
for number in numbers[1:]:
    number_of_boxes_right = number_of_boxes - last_number_of_boxes_left - count_of_boxes[last_number]
    last_price = last_price + (last_number_of_boxes_left + count_of_boxes[last_number]) * (
                number - last_number) - number_of_boxes_right * (number - last_number)
    # if last_price != get_price_for_number(number):
    #     print(number)
    #     print(last_price)
    #     print(get_price_for_number(number))
    #     break
    last_number_of_boxes_left += count_of_boxes[last_number]
    last_number = number
    min_price = min(min_price, last_price)

print(min_price)
