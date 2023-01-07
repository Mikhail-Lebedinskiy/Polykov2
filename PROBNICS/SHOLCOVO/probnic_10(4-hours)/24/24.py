def main():
    with open('24.txt') as file:
        s = file.read().strip()
    max_len = -1
    cur_len = 1
    last_chr = s[0]
    bit = 0
    for chr in s[1:]:
        if bit == 0:
            if chr < last_chr:
                cur_len += 1
                bit = 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
                bit = 0
        else:
            if chr > last_chr:
                cur_len += 1
                bit = 0
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
                bit = 0
        last_chr = chr
    return max(max_len, cur_len)


print(main())

