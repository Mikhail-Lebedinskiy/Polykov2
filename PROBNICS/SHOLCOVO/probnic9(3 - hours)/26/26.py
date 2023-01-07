table = [set() for i in range(10 ** 4)]

operations = []
with open('26.txt') as file:
    n = int(file.readline())
    for line in file:
        operations.append(line.strip())

print(n)
print(operations[:3])

for operation in operations:
    i, j, sign = operation.split()
    i, j = int(i), int(j)
    i -= 1
    j -= 1
    if sign == '+':
        if j not in table[i]:
            table[i].add(j)
    else:
        if j in table[i]:
            table[i] = table[i] - {j}

max_len = 0
number_line_of_max_len = -1
for i, line in enumerate(table):
    last_ind = -1
    cur_len = 0
    for ind in sorted(list(line)):
        if last_ind + 1 == ind:
            cur_len += 1
        else:
            if cur_len >= max_len:
                max_len = cur_len
                number_line_of_max_len = i
            cur_len = 1
        last_ind = ind

print(max_len, number_line_of_max_len)
print(table[3859])