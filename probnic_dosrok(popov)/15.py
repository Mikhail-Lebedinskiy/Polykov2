def f(a, b):
    if a % b == 0:
        return True
    else:
        return False



for x in range(10000):
    t = False
    for a in range(10000):
        if ((f(x, 3) <= (not f(x, 5))) or (x + a >= 70)) == 1:
            print(a)
            t = True
            break
    if t:
        break

for a in range(1, 10000):
    for x in range(1, 10000):
        if ((f(x, 3) <= (not f(x, 5))) or (x + a >= 70)) == False:
            break
    else:
        print(a)
        break




