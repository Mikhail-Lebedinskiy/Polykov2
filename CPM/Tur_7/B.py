from math import asin, acos, sqrt, pi


def is_angel1_equals_angel2(angel1, angel2):
    t = max(angel2, angel1) - min(angel1, angel2)
    while t - 2 * pi > 0:
        t -= 2 * pi
    if t < 0.00001:
        return True
    if abs(t - 2 * pi) < 0.00001:
        return True
    return False


def get_angel(x, y):
    l = sqrt(x ** 2 + y ** 2)
    angel_1 = asin(y / l)
    angel_2 = acos(x / l)

    if is_angel1_equals_angel2(angel_1, angel_2):
        return angel_2

    if is_angel1_equals_angel2(pi - angel_1, angel_2):
        return angel_2

    if is_angel1_equals_angel2(angel_1, 2 * pi - angel_2):
        return 2 * pi - angel_2

    if is_angel1_equals_angel2(pi - angel_1, 2 * pi - angel_2):
        return 2 * pi - angel_2


def angel_2pi(angel):
    while angel - 2 * pi >= 0:
        angel -= 2 * pi
    return angel


def main():
    number_of_points = int(input())
    xO, yO = [int(i) for i in input().split()]
    points_cords = []
    for i in range(number_of_points):
        x, y = [int(i) for i in input().split()]
        if x - xO == 0 and y - xO:
            print('NO')
            exit(0)
        points_cords.append((x - xO, y - yO, get_angel(x - xO, y - yO)))
    points_cords.sort(key=lambda x: x[2])

    for i in range(number_of_points):
        next_i = (i + 1) % number_of_points
        prev_i = (i - 1) % number_of_points
        print(points_cords)
        if angel_2pi(points_cords[i][2] + pi) <= points_cords[next_i][2]:
            print('hey')
            print('YES')
            print(i)
            exit(0)
        elif angel_2pi(points_cords[i][2] + pi) >= points_cords[prev_i][2] > points_cords[i][2]:
            print('YES')
            print(i)
            exit(0)
    print('NO')



main()


