def main():
    with open('26.txt') as file:
        N = int(file.readline())
        costs = [int(i) for i in file]
    costs.sort()
    discounts = [int(i * 0.75) for i in costs if i > 240]
    print(discounts)
    discounts_real = discounts[:len(discounts) // 2]
    print(discounts_real)
    print('len')
    print(len(discounts))
    print(len(discounts_real))
    print(sum(costs) - sum(discounts_real))
    for i in costs:
        if int(i * 0.75) == 3864:
            print(i)


main()
#  5153
