def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return n // i - i
    return 0


def main():
    for n in range(850001, 10 ** 7):
        fn = f(n)
        if fn != 0 and fn % 3 == 0:
            print(n, fn)
main()