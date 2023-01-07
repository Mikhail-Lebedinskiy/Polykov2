number_of_pix = 1024 * 768
koef = 6
number_of_im = 32
dop_inf = 54 * 2 ** 13
sum_memory = 6 * 2 ** 23
bit_to_one_pix = (sum_memory - dop_inf * number_of_im) * koef / number_of_im / number_of_pix
print(2 ** int(bit_to_one_pix))