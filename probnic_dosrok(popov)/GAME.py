from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a + b >= 223:
        return 0
    moves = [game(a + 1, b), game(a * 2, b), game(a, b + 1), game(a, b * 2)]
    lose = []
    for i in moves:
        if i <= 0:
            lose.append(i)
    if len(lose) == 0:
        return -max(moves)
    else:
        return -max(lose) + 1

for b in range(1, 206):
    print(b, game(17, b))

