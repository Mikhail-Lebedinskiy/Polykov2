
min_len = 10 ** 5
min_str_len = 10 ** 5

for str_len in range(101, 3000):
    s = '4' * str_len
    while '4444' in s:
        s = s.replace('444', '333', 1)
        s = s.replace('33', '44', 1)
    count_4 = s.count('4')
    if count_4 % 2 == 0 and count_4 < min_len:
        print('00')
        min_len = count_4
        min_str_len = str_len

print(min_len, min_str_len)