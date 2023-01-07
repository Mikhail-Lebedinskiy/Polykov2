from functools import lru_cache


@lru_cache(None)
def game(n):
    if n >= 74:
        return 0
    moves = [game(n + 1), game(n + 2), game(n * 3)]
    loses = [i for i in moves if i <= 0]
    if len(loses) == 0:
        return -max(moves)
    else:
        return -max(loses) + 1


for n in range(1, 74):
    if game(n) == -2:
        print(n, game(n))