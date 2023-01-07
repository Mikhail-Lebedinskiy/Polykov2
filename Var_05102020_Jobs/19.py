from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a + b >= 44:
        return 0
    moves = [game(a + b, b), game(a, a + b)]
    loses = [i for i in moves if i <= 0]
    if len(loses) == 0:
        return -max(moves)
    else:
        return -max(loses) + 1


for s in range(1, 44):
    if game(s, s) == 2:
        print(s)
print(game(7, 7))
