from functools import lru_cache


@lru_cache(None)
def game(h1, h2):
    if h1 + h2 >= 99:
        return 0
    moves = [game(h1 + 2, h2), game(h1 * 3, h2), game(h1, h2 + 2), game(h1, h2 * 3)]
    loses = [i for i in moves if i <= 0]
    if loses:
        return -max(loses) + 1
    else:
        return -max(moves)


for h2 in range(1, 99):
    # print(h2, game(5, h2))
    if game(5, h2) == -2:
        print(h2)