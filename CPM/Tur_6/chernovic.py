def invers(arr):
    d = {0: 1, 1: 0}
    for i in range(len(arr)):
        arr[i] = (d[arr[i][0]], d[arr[i][0]], arr[i][2])


def print_answer(symmetrical_pairs, sym_invers, unsymmetrical_pairs, unsyme_invers, mid):
    if mid is None:
        pairs = symmetrical_pairs + unsymmetrical_pairs
        pairs.sort(key=(lambda x: x[2]))
        answer = '! '
        for pair in pairs:
            answer += str(pair[0])
            # print(pair[0], end='')
        for pair in pairs[::-1]:
            answer += str(pair[1])
            # print(pair[1], end='')
        print(answer)

    else:
        pairs = symmetrical_pairs + unsymmetrical_pairs
        pairs.sort(key=(lambda x: x[2]))
        # print('! ', end='')
        answer = '! '
        for pair in pairs:
            answer += str(pair[0])
            # print(pair[0], end='')
        answer += str(mid)
        for pair in pairs[::-1]:
            answer += str(pair[1])
            # print(pair[1], end='')
        print(answer)

    x = input()
    if x == 'N':
        exit(228)


def main(str_len):
    symmetrical_pairs = []
    unsymmetrical_pairs = []
    left = 0
    right = str_len - 1
    number_of_questions = 1
    while True:
        if left > right:
            print_answer(symmetrical_pairs, 0, unsymmetrical_pairs, 0, None)
        if right == left:
            if number_of_questions % 10 != 1:
                print(f'? {left}')

                mid = int(input())
                print_answer(symmetrical_pairs, 0, unsymmetrical_pairs, 0, mid)
                break
            else:
                print(f'? {left}')

                mid = int(input())
                if symmetrical_pairs == []:  #
                    print(f'? {unsymmetrical_pairs[0][2]}')

                    x = int(input())
                    if x != unsymmetrical_pairs[0][2]:
                        invers(unsymmetrical_pairs)
                    number_of_questions += 1
                elif unsymmetrical_pairs == []:
                    print(f'? {symmetrical_pairs[0][2]}')

                    x = int(input())
                    if x != symmetrical_pairs[0][2]:
                        invers(symmetrical_pairs)
                    number_of_questions += 1
                else:
                    print(f'? {unsymmetrical_pairs[0][2]}')

                    x = int(input())
                    if x != unsymmetrical_pairs[0][2]:
                        invers(unsymmetrical_pairs)
                    print(f'? {symmetrical_pairs[0][2]}')

                    x = int(input())
                    if x != symmetrical_pairs[0][2]:
                        invers(symmetrical_pairs)
                    number_of_questions += 2
                print_answer(symmetrical_pairs, 0, unsymmetrical_pairs, 0, mid)
                break
        if number_of_questions % 10 != 1 and number_of_questions % 10 != 0:
            print(f'? {left}')

            x1 = int(input())
            print(f'? {right}')

            x2 = int(input())
            if x1 == x2:
                symmetrical_pairs.append((x1, x2, right))
            else:
                unsymmetrical_pairs.append((x1, x2, right))
            number_of_questions += 2
            right -= 1
            left += 1
        elif number_of_questions % 10 == 1:
            if symmetrical_pairs == [] and unsymmetrical_pairs == []:
                print(f'? {left}')

                x1 = int(input())
                print(f'? {right}')

                x2 = int(input())
                if x1 == x2:
                    symmetrical_pairs.append((x1, x2, right))
                else:
                    unsymmetrical_pairs.append((x1, x2, right))
                number_of_questions += 2
                right -= 1
                left += 1
            elif symmetrical_pairs == []:
                print(f'? {unsymmetrical_pairs[0][2]}')

                x = int(input())
                if x != unsymmetrical_pairs[0][2]:
                    invers(unsymmetrical_pairs)
                number_of_questions += 1
            elif unsymmetrical_pairs == []:
                print(f'? {symmetrical_pairs[0][2]}')

                x = int(input())
                if x != symmetrical_pairs[0][2]:
                    invers(symmetrical_pairs)
                number_of_questions += 1
            else:
                print(f'? {unsymmetrical_pairs[0][2]}')

                x = int(input())
                if x != unsymmetrical_pairs[0][2]:
                    invers(unsymmetrical_pairs)
                print(f'? {symmetrical_pairs[0][2]}')

                x = int(input())
                if x != symmetrical_pairs[0][2]:
                    invers(symmetrical_pairs)
                number_of_questions += 2
        elif number_of_questions % 10 == 0:
            print(f'? {left}')

            x = int(input())
            number_of_questions += 1
            if symmetrical_pairs == [] and unsymmetrical_pairs == []:
                print(f'? {left}')

                x1 = int(input())
                print(f'? {right}')

                x2 = int(input())
                if x1 == x2:
                    symmetrical_pairs.append((x1, x2, right))
                else:
                    unsymmetrical_pairs.append((x1, x2, right))
                number_of_questions += 2
                right -= 1
                left += 1
            elif symmetrical_pairs == []:
                print(f'? {unsymmetrical_pairs[0][2]}')

                x = int(input())
                if x != unsymmetrical_pairs[0][2]:
                    invers(unsymmetrical_pairs)
                number_of_questions += 1
            elif unsymmetrical_pairs == []:
                print(f'? {symmetrical_pairs[0][2]}')

                x = int(input())
                if x != symmetrical_pairs[0][2]:
                    invers(symmetrical_pairs)
                number_of_questions += 1
            else:
                print(f'? {unsymmetrical_pairs[0][2]}')

                x = int(input())
                if x != unsymmetrical_pairs[0][2]:
                    invers(unsymmetrical_pairs)
                print(f'? {symmetrical_pairs[0][2]}')

                x = int(input())
                if x != symmetrical_pairs[0][2]:
                    invers(symmetrical_pairs)
                number_of_questions += 2


T, str_len = [int(i) for i in input().split()]
for _ in range(T):
    main(str_len)