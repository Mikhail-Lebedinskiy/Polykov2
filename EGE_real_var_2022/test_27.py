from math import ceil

count_of_boxes = {}
numbers = []
with open('data/27/27(test).txt') as file:
    for line in file:
        number, count = [int(i) for i in line.strip().split()]
        numbers.append(number)
        count_of_boxes[number] = ceil(count / 36)


def get_price_for_number(input_number: int) -> int:
    price = 0
    for number in numbers:
        price += abs(input_number - number) * count_of_boxes[number]
    return price





