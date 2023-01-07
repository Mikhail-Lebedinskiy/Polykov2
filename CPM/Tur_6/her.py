arr = '0001'

def invers_arr():
    global arr
    d = {'0': '1', '1': '0'}
    itog = ''
    for i in arr:
        itog += d[i]
    arr = itog


def sym_arr():
    global arr
    arr = arr[::-1]


sym_arr()
print(arr)