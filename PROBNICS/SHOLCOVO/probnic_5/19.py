from functools import lru_cache
from sys import setrecursionlimit



@lru_cache(None)
def game(h1, h2):
    if h1 + h2 >= 122:
        return 0
    next = [game(h1 + 2, h2), game(h1 * 2, h2), game(h1, h2 + 2), game(h1, h2 * 2)]
    loses = [i for i in next if i <= 0]
    if len(loses) != 0:
        return -max(loses) + 1
    else:
        return -max(next)


for i in range(1, 118):
    print(f'S = {i}: {game(3, i)}')

