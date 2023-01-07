from functools import lru_cache


@lru_cache(None)
def game(h):
    if h >= 50:
        return 0
    moves = [game(i) for i in [h + 2, h * 3]]
    loses = [i for i in moves if i <= 0]
    if loses:
        return -max(loses) + 1
    else:
        return -max(moves)


for i in range(1, 50):
    print(i, game(i))


"""
а) 15
б) 3
в) 11 12
"""