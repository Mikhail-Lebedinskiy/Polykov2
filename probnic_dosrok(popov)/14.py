def ff(n):
    answer = ""
    while n != 0:
        answer += str(n % 4)
        n //= 4
    return answer[::-1]

n = 3*16**2018-2*8**1028-3*4**1100-2**1050-2022
a = ff(n)
print(a.count("3"))
