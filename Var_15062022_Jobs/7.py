size = 192 * 960
mem = size * 11
mem_on_pc = 180 * 2**10 * 8
bit = mem - mem_on_pc
print(bit / mem * 100)
print(mem - mem_on_pc)
print(mem * 0.73 / 2 ** 13)
