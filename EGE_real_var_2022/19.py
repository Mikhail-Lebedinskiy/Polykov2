from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a + b >= 259:
        return 0
    moves = [game(a + 1, b), game(a, b + 1), game(a * 2, b), game(a, b * 2)]
    wins = [i for i in moves if i <= 0]
    if len(wins) == 0:
        return -max(moves)
    else:
        return -max(wins) + 1


for s in range(1, 259):
    if game(17, s) == -2:
        print(s)
    # print(s, game(17, s))
