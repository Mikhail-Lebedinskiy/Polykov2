def f(n):
    return len(str(n)) == 3 and n > 0 and n % 100 == 12


file = open("17-202.txt", 'r')
data = list(file)
data = [int(i) for i in data if i[-2] != '.']
data = [data[i - 1] + data[i] + data[i + 1] for i in range(1, len(data) - 1) if f(data[i]) and not(f(data[i + 1])) and not(f(data[i - 1]))]
file.close()
print(len(data))
print(max(data))