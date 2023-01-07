def f(s):
    ans = ''
    for i in s:
        if i == '0':
            ans += '1'
        else:
            ans += '0'
    ind = ans.find('1')
    return ans[ind:]

#
# def x(i):
#     N = i
#     N_bin = bin(N)[2:]
#     N_bin_invert = f(N_bin)
#     R = int(N_bin_invert, 2)
#     result = N - R
#     return result


for i in range(1, 10 ** 5):
    N = i
    N_bin = bin(N)[2:]
    N_bin_invert = f(N_bin)
    R = int(N_bin_invert, 2)
    result = N - R
    if result == 979:
        print(N)

# print(x(22))
#
# print(f('1110010'))
