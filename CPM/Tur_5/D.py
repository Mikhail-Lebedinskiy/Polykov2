def get_pare(a, k):
    cur_v = 1
    last_v = 0
    cur_k = k - 1
    while True:
        if cur_v == a:
            break
        last_v = cur_v
        if cur_v + 2 ** cur_k - 1 < a:
            cur_v = cur_v + 2 ** cur_k
        else:
            cur_v = cur_v + 1
        cur_k -= 1
    return last_v + 1, last_v + 2 ** (cur_k + 1), cur_k

print(get_pare(18, 5))