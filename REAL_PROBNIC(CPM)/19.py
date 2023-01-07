from functools import lru_cache


@lru_cache(None)
def game(h):
    if h >= 151:
        return 0
    moves = [h + 1, h + 2, h * 2]
    moves = [i for i in moves if i % 3 != 0]
    results = [game(i) for i in moves]
    loses = [i for i in results if i <= 0]
    if loses:
        return -max(loses) + 1
    else:
        return -max(results)


for h in range(1, 150):
    if h % 3 == 0:
        continue
    # print(f'h = {h} f({h}) = {game(h)}')
    if game(h) == -2:
        print(h)