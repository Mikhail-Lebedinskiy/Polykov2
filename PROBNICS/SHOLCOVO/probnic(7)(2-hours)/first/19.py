from functools import lru_cache


@lru_cache(None)
def game(h):
    if h >= 165:
        return 0
    moves = [game(h + 1), game(h * 2)]
    loses = [i for i in moves if i <= 0]
    if loses:
        return -max(loses) + 1
    else:
        return -max(moves)


for h in range(1, 165):
    # print(h, game(h))
    if game(h) == -2:
        print(h)