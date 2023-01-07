n = 1
mod = 1
while True:
    mod = (mod * 10 + 1) % 999983
    n += 1
    if mod == 0:
        print(n)
        break


print(int('7' * 999982) % 999983)