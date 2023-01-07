from math import ceil, log2


num_of_symbols = 26 * 2 + 10 + 4
print(num_of_symbols)
bit_for_one_symbols = ceil(log2(num_of_symbols))
bit_for_one_password = bit_for_one_symbols * 11
byte_for_one_password = ceil(bit_for_one_password / 8)

num_of_symbols = 26 + 3
bit_for_one_symbols = ceil(log2(num_of_symbols))
bit_for_one_email = bit_for_one_symbols * 20
byte_for_one_email = ceil(bit_for_one_password / 8)

byte_for_one_user = 600 / 20
byte_for_personal_inf = byte_for_one_user - byte_for_one_email - byte_for_one_password
print(byte_for_personal_inf)

