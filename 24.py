file = open("24-178.txt", 'r')
s = file.readline()
answer = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[j] < s[i]:
            answer = max(j - i - 1, answer)
print(answer)
