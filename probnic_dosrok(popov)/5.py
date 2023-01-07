for i in range(1000):
    nbin = bin(i)[2::]
    if i % 2 == 0:
        nbin = nbin + "10"
    else:
        nbin = "1" + nbin + "01"
    nint = int(nbin, 2)
    if int(nint) > 516:
        print(i)
        break