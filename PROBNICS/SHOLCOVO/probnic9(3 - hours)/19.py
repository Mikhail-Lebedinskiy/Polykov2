from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10 ** 4)


@lru_cache(None)
def game(h1, h2):
    if h1 + h2 >= 75:
        return 0
    moves = [game(h1 + 2, h2), game(h1 * 2, h2), game(h1, h2 + 2), game(h1, h2 * 2)]
    loses = [i for i in moves if i <= 0]
    if loses:
        return -max(loses) + 1
    else:
        return -max(moves)


for h2 in range(1, 66):
    if game(9, h2) == -2:
        print(h2)