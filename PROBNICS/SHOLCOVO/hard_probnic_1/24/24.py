s = open('24__wi32.txt').read().strip()
start_a = 0
for i in s:
    if i == 'a':
        start_a += 1
    else:
        break

end_a = 0
for i in s[::-1]:
    if i == 'a':
        end_a += 1
    else:
        break

ss = s[start_a: -end_a]

if ss == ss[::-1]:
    print(end_a - start_a)
else:
    print(-1)