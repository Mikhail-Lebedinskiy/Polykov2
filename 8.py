arr = ['Щ', 'О', 'Г', 'Б', 'А']
i = 1
print(4 + 2 * 5 + 4 * 5 *5 + 3 * 5**4 + 5**5)
for x1 in arr:
    for x2 in arr:
        for x3 in arr:
            for x4 in arr:
                for x5 in arr:
                    for x6 in arr:
                        if x1 + x2 + x3 + x4 + x5 + x6 == "ОБЩАГА":
                            print(i)
                            exit(0)

                        i += 1

