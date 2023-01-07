def f(cur, end):
    if cur == end:
        return 1
    if int(cur, 2) < int(end, 2):
        return 0
    if '1' in cur[1:]:
        return f(bin(int(cur, 2) - 1)[2:], end) + f('1' + '0' * (len(cur) - 1), end)
    else:
        return f(bin(int(cur, 2) - 1)[2:], end)


print(f('1000000', '1000'))