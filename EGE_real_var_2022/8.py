from itertools import product


def is_good_number(number: str) -> bool:
    if number.count('6') != 1:
        return False
    index_of_6 = number.find('6')
    if index_of_6 == 0:
        return int(number[index_of_6 + 1]) % 2 == 0
    if index_of_6 == len(number) - 1:
        return int(number[index_of_6 - 1]) % 2 == 0
    return int(number[index_of_6 + 1]) % 2 == 0 and int(number[index_of_6 - 1]) % 2 == 0


answer = 0
for number in product('01234567', repeat=5):
    if number[0] == '0':
        continue
    if is_good_number(''.join(number)):
        answer += 1
print(answer)
