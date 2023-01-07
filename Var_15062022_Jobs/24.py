with open('24.txt') as file:
    s = file.readline().strip()
i = 0
max_len = 0
cur_len = 0
indexes = []
while i < len(s):
    if s[i] == 'A':
        if i + 1 < len(s) and s[i + 1] == 'B':
            cur_len += 2
            i += 2
        else:
            max_len = max(max_len, cur_len)
            cur_len = 0
            i += 1
    elif s[i] == 'C':
        if i + 2 < len(s) and s[i + 1: i + 3] == 'AC':
            cur_len += 3
            i += 3
            indexes.append(i + 2)
        else:
            max_len = max(max_len, cur_len)
            cur_len = 0
            i += 1
    else:
        max_len = max(max_len, cur_len)
        cur_len = 0
        i += 1

print(max_len)
