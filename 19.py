from functools import lru_cache


def moves(a):
    return [a + 1, a * 3]


@lru_cache(None)
def game(a):
    if a >= 65 and a <= 100:
        return 0
    if a >= 65 and a > 100:
        return 1
    move = [game(i) for i in moves(a)]
    lose = [i for i in move if i <= 0]
    if lose:
        result = -max(lose) + 1
    else:
        result = - max(move)
    return result


for a in range(1, 100):
    print(a, game(a))

