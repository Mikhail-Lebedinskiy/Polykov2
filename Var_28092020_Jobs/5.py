for N in range(1, 128):
    N_8_bit = bin(N)[2:]
    N_8_bit = '0' * (8 - len(N_8_bit)) + N_8_bit
    N_8_bit_invert = ''
    for i in N_8_bit:
        if i == '0':
            N_8_bit_invert += '1'
        else:
            N_8_bit_invert += '0'
    result = int(N_8_bit_invert, 2) + 1
    if result == 221:
        print(N)
        break
