with open('24.txt') as file:
    s = file.read().strip()

itog_s = ''
for i in s:
    if '0' <= i <= '9':
        itog_s += i
    else:
        itog_s += '*'

numbers = [int(i) for i in itog_s.split('*') if i != '']
print(max(numbers))