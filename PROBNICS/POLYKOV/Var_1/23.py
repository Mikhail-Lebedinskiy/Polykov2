def f(cur, finish, history):
    if cur > finish:
        return 0
    if cur == finish:
        for i in range(2, len(history)):
            if (history[i - 2] + history[i - 1] + history[i]) % 11 == 0:
                return 1
        return 0
    return f(cur + 2, finish, history + [cur + 2]) + f(cur * 3, finish, history + [cur * 3]) + \
           f(cur * 4, finish, history + [cur * 4])


print(f(1, 600, [1]))