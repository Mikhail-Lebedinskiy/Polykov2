N, K = [int(i) for i in input().split()]
number_of_A, number_of_C = 0, 0
s = []
cur_chr = 'W'
cur_chr_count = 0
for chr in input():
    if chr == cur_chr:
        if cur_chr == 'A':
            number_of_A += 1
        if cur_chr == 'C':
            number_of_C += 1
        cur_chr_count += 1
    elif chr == "W":
        s.append((cur_chr_count, cur_chr))
        cur_chr = 'W'
        cur_chr_count = 1
    elif chr == "A":
        number_of_A += 1
        s.append((cur_chr_count, cur_chr))
        cur_chr = 'A'
        cur_chr_count = 1
    elif chr == "C":
        number_of_C += 1
        s.append((cur_chr_count, cur_chr))
        cur_chr = 'C'
        cur_chr_count = 1
s.append((cur_chr_count, cur_chr))

print(s)
answer = 0
cur_number_of_A, cur_number_of_C = number_of_A, number_of_C
for i, el1 in enumerate(s):
    if el1[1] == 'A':
        cur_number_of_A -= el1[0]
    if el1[1] == 'C':
        cur_number_of_C -= el1[0]
    if el1[1] == 'W':
        cur2_number_of_C = cur_number_of_C
        for el2 in s[i + 1:]:
            if el2[1] == 'C':
                cur2_number_of_C -= el2[0]
            if el2[1] == 'A':
                if K % 2 == 0:
                    n = (K - 2) // 2
                    answer += el1[0] * el2[0] * (cur2_number_of_C * (K * (K + 1) // 2) + number_of_C * (n*(2*n-1)*(2*n+1)//3))
                else:
                    n = (K - 1) // 2
                    answer += el1[0] * el2[0] * (cur2_number_of_C * (K * (K + 1) // 2) + number_of_C * 4 * (n * (n + 1) * (2*n + 1) // 6))

print(answer)
