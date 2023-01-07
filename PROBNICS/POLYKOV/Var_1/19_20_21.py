from functools import lru_cache


@lru_cache(None)
def game(h1, h2):
    if h1 + h2 >= 231:
        return 0
    moves = [game(h1 + 2, h2), game(h1 * 2, h2), game(h1, h2 + 2), game(h1, h2 * 2)]
    loses = [i for i in moves if i <= 0]
    if loses:
        return -max(loses) + 1
    else:
        return -max(moves)


for s in range(1, 214):
    res = game(17, s)
    if res == -2:
        print(s, game(17, s))


