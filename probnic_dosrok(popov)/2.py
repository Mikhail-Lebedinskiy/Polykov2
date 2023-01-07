for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((not (x <= z)) or (y == w) or not y) == False:
                    print(x, y, w, z)