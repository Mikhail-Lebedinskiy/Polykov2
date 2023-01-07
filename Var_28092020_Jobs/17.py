good_numbers = []
for n in range(333666, 700000):
    n_str = str(n)
    if n_str.count('7') >= 2 and n % 17 == 0:
        good_numbers.append(n)
print(max(good_numbers))
print(len(good_numbers))
