from functools import lru_cache


@lru_cache(None)
def f(s):
    max_len = 0
    cur_len = 0
    for i in range(0, len(s) - 2, 3):
        if s[i:i+3] == '110':
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            return max(max_len, f(s[i + 1:]), f(s[i + 2:]), f(s[i + 3:]))


with open('24.txt') as file:
    s = file.read().strip()

s.replace('A', '1')
s.replace('O', '0')
s.replace('C', '0')
s.replace('D', '0')
s.replace('F', '0')

print(f(s))