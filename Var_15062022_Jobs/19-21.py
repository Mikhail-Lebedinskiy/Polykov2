from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a + b >= 231:
        return 0
    moves = [game(a + 2, b), game(a, b + 2), game(a * 2, b), game(a, b * 2)]
    loses = [i for i in moves if i <= 0]
    if len(loses) != 0:
        return -max(loses) + 1
    else:
        return -max(moves)


for s in range(1, 213):
    x = game(17, s)
    #print(s, game(17, s))
    if x == -2:
        print(s)
