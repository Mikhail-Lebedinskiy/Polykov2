from math import ceil


bit_to_symbol = 3
bit_to_password = 6 * bit_to_symbol
byte_to_user = ceil(bit_to_password / 8) + 10
print(byte_to_user * 100)

