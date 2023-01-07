num_symbols = 1234 + 10
bit_to_symbols = 11

byt_to_ind = int(2050 * 2 ** 10 / 65536)
bit_to_ind = byt_to_ind * 8
print(bit_to_ind / bit_to_symbols)