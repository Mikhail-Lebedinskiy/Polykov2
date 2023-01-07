from itertools import product, permutations


def check(x1, y1, x2, y2):
    if x1 == x2:
        return True
    if y1 == y2:
        return True
    if x1 + y1 == x2 + y2:
        return True
    if x1 - y1 == x2 - y2:
        return True
    return False


answer = 0

for y_cords in product([0, 1, 2, 3, 4, 5, 6, 7], repeat=8):
    if any(check(pare[0], y_cords[pare[0]], pare[1], y_cords[pare[1]]) for pare in permutations([0, 1, 2, 3, 4, 5, 6, 7], 2)):
        pass
    else:
        answer += 1
print(answer)

