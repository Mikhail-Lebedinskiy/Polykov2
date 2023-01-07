MOD = 10 ** 9 + 7


def is_good(a, d, m):
    if int(a) % m != 0:
        return 0
    even_digits = str(a)[1::2]
    odd_digits = str(a)[::2]
    if str(d) in odd_digits:
        return 0
    if len(even_digits) == 0:
        return 1
    if str(d) not in even_digits:
        return 0
    if len(set(str(even_digits))) == 1:
        return 1
    return 0


def f(x, d, m):
    x = '0' + x
    # dp[len(x)][m][0/1/2]
    dp = []
    for i in range(len(x)):
        dp.append([[0] * 3 for j in range(m)])
    for digit in range(1, 10):
        if digit == d:
            continue
        if digit < int(x[1]):
            dp[1][digit % m][0] += 1
        elif digit == int(x[1]):
            dp[1][digit % m][1] += 1
        else:
            dp[1][digit % m][2] += 1
    for pref_len in range(2, len(x)):
        if pref_len % 2 == 1:
            for mod in range(m):
                for digit in range(10):
                    if digit == d:
                        continue
                    # update 0 - type
                    dp[pref_len][(mod * 10 + digit) % m][0] += dp[pref_len - 1][mod][0]
                    if digit < int(x[pref_len]):
                        dp[pref_len][(mod * 10 + digit) % m][0] += dp[pref_len - 1][mod][1]
                    # update 1 - type
                    if digit == int(x[pref_len]):
                        dp[pref_len][(mod * 10 + digit) % m][1] += dp[pref_len - 1][mod][1]
                    # update 2 - type
                    dp[pref_len][(mod * 10 + digit) % m][2] += dp[pref_len - 1][mod][2]
                    if digit > int(x[pref_len]):
                        dp[pref_len][(mod * 10 + digit) % m][2] += dp[pref_len - 1][mod][1]
        else:
            if d < int(x[pref_len]):
                for mod in range(m):
                    # update 0 - type
                    dp[pref_len][(mod * 10 + d) % m][0] += dp[pref_len - 1][mod][0]
                    dp[pref_len][(mod * 10 + d) % m][0] += dp[pref_len - 1][mod][1]
                    # update 2 - type
                    dp[pref_len][(mod * 10 + d) % m][2] += dp[pref_len - 1][mod][2]
            elif d > int(x[pref_len]):
                for mod in range(m):
                    # update 0 - type
                    dp[pref_len][(mod * 10 + d) % m][0] += dp[pref_len - 1][mod][0]
                    # update 2 - type
                    dp[pref_len][(mod * 10 + d) % m][2] += dp[pref_len - 1][mod][2]
                    dp[pref_len][(mod * 10 + d) % m][2] += dp[pref_len - 1][mod][1]
            else:
                for mod in range(m):
                    # update 0 - type
                    dp[pref_len][(mod * 10 + d) % m][0] += dp[pref_len - 1][mod][0]
                    # update 1 - type
                    dp[pref_len][(mod * 10 + d) % m][1] += dp[pref_len - 1][mod][1]
                    # update 2 - type
                    dp[pref_len][(mod * 10 + d) % m][2] += dp[pref_len - 1][mod][2]
    res = 0
    for pref_len in range(len(x) - 1):
        res += dp[pref_len][0][0]
        res += dp[pref_len][0][1]
        res += dp[pref_len][0][2]
    res += dp[len(x) - 1][0][0]
    res += dp[len(x) - 1][0][1]
    for line in dp:
        print(line)
    print('*' * 500)
    return res


def main():
    m, d = [int(i) for i in input().split()]
    a = input()
    b = input()
    # print(f(a, d, m))
    # # print((f(b, d, m) - f(a, d, m)) % MOD)
    print(f(b, d, m))
    print(f(a, d, m))
    # print(f('10', 2, 6))
    answer = f(b, d, m) - f(a, d, m) + is_good(a, d, m)

main()