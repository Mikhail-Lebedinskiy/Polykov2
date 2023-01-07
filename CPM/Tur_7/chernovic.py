from math import asin, acos, sqrt, pi


def is_angel1_equals_angel2(angel1, angel2):
    t = max(angel2, angel1) - min(angel1, angel2)
    print(f't = {t}')
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
    print(angel_1)
    print(angel_2)

    if is_angel1_equals_angel2(angel_1, angel_2):
        print(1)
        return angel_2

    if is_angel1_equals_angel2(pi - angel_1, angel_2):
        print(2)
        return angel_2

    if is_angel1_equals_angel2(angel_1, 2 * pi - angel_2):
        print(3)
        return 2 * pi - angel_2

    if is_angel1_equals_angel2(pi - angel_1, 2 * pi - angel_2):
        print(4)
        return 2 * pi - angel_2


def f(alpha1, alpha2, alpha3):
    alpha1_1 = get_angel(alpha1 + pi)
    # alpha1 находиться в первой четверти


# [(1, 1, 0.7853981633974484), (1, -1, 0.7853981633974484), (-1, -1, 2.356194490192345), (-1, 1, 2.356194490192345)]
print(get_angel(1, -1))