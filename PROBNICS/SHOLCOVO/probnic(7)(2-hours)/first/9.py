with open('9.txt') as file:
    cords = []
    for line in file:
        cords.append([int(i) for i in line.split()])

answer = 0
for cord in cords:
    y1, y2, x1, x2 = cord[2], cord[3], cord[0], cord[1]
    flag = False
    for i in (x1, x2, y1, y2):
        if i < 1 or i > 8:
            flag = True
            break
    if flag:
        continue

    if x1 + 1 == x2 and (y1 + 2 == y2 or y1 - 2 == y2):
        answer += 1
        # print(x1, y1, x2, y2, 'V1')
    elif x1 + 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2):
        answer += 1
        # print(x1, y1, x2, y2, 'V2')
    elif x1 - 1 == x2 and (y1 + 2 == y2 or y1 - 2 == y2):
        answer += 1
        # print(x1, y1, x2, y2, 'V3')
    elif x1 - 2 == x2 and (y1 + 1 == y2 or y1 - 1 == y2):
        answer += 1
        # print(x1, y1, x2, y2, 'V4')

print(answer)

