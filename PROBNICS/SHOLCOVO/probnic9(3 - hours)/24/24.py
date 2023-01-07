def f(s):
    if len(s) != 11:
        return False
    if s[:2] != '43':
        return False
    if s[4:6] != '78':
        return False
    if s[9:] != '34':
        return False
    return True


with open('24.txt') as file:
    s = file.read().strip()

answer = []
numbers = s.split('KK')
for number in numbers:
    if number.isdigit():
        if f(number):
            answer.append(int(number))

print(max(answer))