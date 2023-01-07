f = open('data/24/24.txt')
s = [str(i) for i in f][0].strip()
max_len = 0
current_len = 0
for i in range(0, len(s) - 1, 2):
    if s[i] in 'BCD' and s[i + 1] in 'AO':
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 0

for i in range(1, len(s) - 1, 2):
    if s[i] in 'BCD' and s[i + 1] in 'AO':
        current_len += 1
    else:
        max_len = max(max_len, current_len)
        current_len = 0

print(max_len)
f.close()
