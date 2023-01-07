def get_Vp_to_n(n, p):
    Vp = 0
    while True:
        if n % p == 0:
            Vp += 1
            n //= p
        else:
            return Vp


with open('27B__wi2x.txt') as file:
    numbers_count = int(file.readline())
    numbers = []
    for i in file:
        numbers.append(int(i))


# 12 * 12 = 9 * 16 = 3 ** 2 * 2 ** 4


keys = []
for i_2 in range(5):
    for i_3 in range(3):
        keys.append((i_2, i_3))
data = {key: 0 for key in keys}

for number in numbers:
    V3 = min(get_Vp_to_n(number, 3), 2)
    V2 = min(get_Vp_to_n(number, 2), 4)
    data[(V2, V3)] += 1


answer = 0
for key in keys:
    good_keys = []
    for v2 in range(4 - key[0], 5):
        for v3 in range(2 - key[1], 3):
            good_keys.append((v2, v3))
    for good_key in good_keys:
        if key == good_key:
            answer += data[key] * (data[key] - 1) / 2
        else:
            answer += data[key] * data[good_key] / 2

print(numbers_count * (numbers_count - 1) / 2 - answer)


