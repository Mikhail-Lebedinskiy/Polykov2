from itertools import product


for x1 in '0123456789':
    for x2 in '0123456789':
        if int(f'1{x1}954{x2}21') % 3023 == 0:
            print(f'1{x1}954{x2}21')

for x2 in '0123456789':
    if int(f'1{x2}95421') % 3023 == 0:
        print(f'1{x2}95421')

for i in product('0123456789', repeat=2):
    for x1 in '0123456789':
        x2 = ''.join(i)
        if int(f'1{x1}954{x2}21') % 3023 == 0:
            print(f'1{x1}954{x2}21')

for i in product('0123456789', repeat=3):
    for x1 in '0123456789':
        x2 = ''.join(i)
        if int(f'1{x1}954{x2}21') % 3023 == 0:
            print(f'1{x1}954{x2}21')

# for i in product('0123456789', repeat=3):
#     for x1 in '0123456789':
#         x2 = ''.join(i)
#         if int(f'1{x1}954{x2}21') % 3023 == 0:
#             print(f'1{x1}954{x2}21')