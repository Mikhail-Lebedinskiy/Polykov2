i = "8" * 86
a = "1111"
b = "8888"


while a in i or b in i:
    if a in i:
        i = i.replace(a, "8", 1)
    elif b in i:
        i = i.replace(b, "11", 1)
    if a not in i and b not in i:
        print(i)