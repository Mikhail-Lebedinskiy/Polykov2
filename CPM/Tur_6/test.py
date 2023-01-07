from random import randint
import sys


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



def check_answer(answer):
    print(f'YOUR ANSWER = {answer}')
    print(f'REAL ANSWER = {arr}')
    if answer[2:] == arr:
        print('GOOD')
    else:
        print('BAD')
    print('____________________\n')
    return 'Y'



def question(i):
    global counter
    print(f'YOUR QUESTION - {i} Number_of_question = {counter}')
    if counter % 10 == 1:
        num_op = randint(0, 3)
        if num_op == 0:
            print('НИЧЕГО НЕ ДЕЛАНЬЕ')
        if num_op == 1:
            print('ИНВЕРСИЯ')
            invers_arr()
        if num_op == 2:
            print('СИММЕТРИЯ')
            sym_arr()
        if num_op == 3:
            print('ИНВЕРСИЯ + СИММЕТРИЯ')
            invers_arr()
            sym_arr()
        print(f'arr = {arr}')
    print(f'ОТВЕТ - {arr[i - 1]}')
    counter += 1
    return int(arr[i - 1])







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
        x = check_answer(answer)
        sys.stdout.flush()
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
        x = check_answer(answer)
        sys.stdout.flush()
    if x == 'N':
        exit(228)


def main(str_len):
    symmetrical_pairs = []
    unsymmetrical_pairs = []
    left = 0
    right = str_len - 1
    number_of_questions = 1


    while True:

        # print(f'number_of_questions = {number_of_questions}')
        # print(f'left = {left}, right = {right}')
        # print(f'sym_pairs = {symmetrical_pairs}')
        # print(f'unsym_pairs = {unsymmetrical_pairs}')



        if left > right:
            print_answer(symmetrical_pairs, 0, unsymmetrical_pairs, 0, None)
            break
        if right == left:
            if number_of_questions % 10 != 1:
                mid = question(left + 1)
                sys.stdout.flush()
                print_answer(symmetrical_pairs, 0, unsymmetrical_pairs, 0, mid)
                break
            else:
                # print(f'? {left + 1}')
                mid = question(left + 1)
                sys.stdout.flush()
                # mid = int(input())
                if symmetrical_pairs == []:  #
                    # print(f'? {unsymmetrical_pairs[0][2] + 1}')
                    x = question(unsymmetrical_pairs[0][2] + 1)
                    sys.stdout.flush()
                    # x = int(input())
                    if x != unsymmetrical_pairs[0][0]:
                        invers(unsymmetrical_pairs)
                    number_of_questions += 1
                elif unsymmetrical_pairs == []:
                    # print(f'? {symmetrical_pairs[0][2] + 1}')
                    x = question(symmetrical_pairs[0][2] + 1)
                    sys.stdout.flush()
                    # x = int(input())
                    if x != symmetrical_pairs[0][0]:
                        invers(symmetrical_pairs)
                    number_of_questions += 1
                else:
                    # print(f'? {unsymmetrical_pairs[0][2] + 1}')
                    x = question(unsymmetrical_pairs[0][2] + 1)
                    sys.stdout.flush()
                    # x = int(input())
                    if x != unsymmetrical_pairs[0][0]:
                        invers(unsymmetrical_pairs)
                    # print(f'? {symmetrical_pairs[0][2] + 1}')
                    x = question(symmetrical_pairs[0][2] + 1)
                    sys.stdout.flush()
                    # x = int(input())
                    if x != symmetrical_pairs[0][0]:
                        invers(symmetrical_pairs)
                    number_of_questions += 2
                print_answer(symmetrical_pairs, 0, unsymmetrical_pairs, 0, mid)
                break
        if number_of_questions % 10 != 1 and number_of_questions % 10 != 0:
            # print(f'? {left + 1}')
            x1 = question(left + 1)
            sys.stdout.flush()
            # x1 = int(input())
            # print(f'? {right + 1}')
            x2 = question(right + 1)
            sys.stdout.flush()
            # x2 = int(input())
            if x1 == x2:
                symmetrical_pairs.append((x1, x2, left))
            else:
                unsymmetrical_pairs.append((x1, x2, left))
            number_of_questions += 2
            right -= 1
            left += 1
        elif number_of_questions % 10 == 1:
            if symmetrical_pairs == [] and unsymmetrical_pairs == []:
                # print(f'? {left + 1}')
                x1 = question(left + 1)
                sys.stdout.flush()
                # x1 = int(input())
                # print(f'? {right + 1}')
                x2 = question(right + 1)
                sys.stdout.flush()
                # x2 = int(input())
                if x1 == x2:
                    symmetrical_pairs.append((x1, x2, left))
                else:
                    unsymmetrical_pairs.append((x1, x2, left))
                number_of_questions += 2
                right -= 1
                left += 1
            elif symmetrical_pairs == []:
                # print(f'? {unsymmetrical_pairs[0][2] + 1}')
                x = question(unsymmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != unsymmetrical_pairs[0][0]:
                    invers(unsymmetrical_pairs)
                number_of_questions += 1
            elif unsymmetrical_pairs == []:
                # print(f'? {symmetrical_pairs[0][2] + 1}')
                x = question(symmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != symmetrical_pairs[0][0]:
                    invers(symmetrical_pairs)
                number_of_questions += 1
            else:
                # print(f'? {unsymmetrical_pairs[0][2] + 1}')
                x = question(unsymmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != unsymmetrical_pairs[0][0]:
                    invers(unsymmetrical_pairs)
                # print(f'? {symmetrical_pairs[0][2] + 1}')
                x = question(symmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != symmetrical_pairs[0][0]:
                    invers(symmetrical_pairs)
                number_of_questions += 2
        elif number_of_questions % 10 == 0:
            # print(f'? {left + 1}')
            x = question(left + 1)
            sys.stdout.flush()
            # x = int(input())
            number_of_questions += 1
            if symmetrical_pairs == [] and unsymmetrical_pairs == []:
                # print(f'? {left + 1}')
                x1 = question(left + 4)
                sys.stdout.flush()
                # x1 = int(input())
                # print(f'? {right + 1}')
                x2 = question(right + 1)
                sys.stdout.flush()
                # x2 = int(input())
                if x1 == x2:
                    symmetrical_pairs.append((x1, x2, left))
                else:
                    unsymmetrical_pairs.append((x1, x2, left))
                number_of_questions += 2
                right -= 1
                left += 1
            elif symmetrical_pairs == []:
                # print(f'? {unsymmetrical_pairs[0][2] + 1}')
                x = question(unsymmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != unsymmetrical_pairs[0][0]:
                    invers(unsymmetrical_pairs)
                number_of_questions += 1
            elif unsymmetrical_pairs == []:
                # print(f'? {symmetrical_pairs[0][2] + 1}')
                x = question(symmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != symmetrical_pairs[0][0]:
                    invers(symmetrical_pairs)
                number_of_questions += 1
            else:
                # print(f'? {unsymmetrical_pairs[0][2] + 1}')
                x = question(unsymmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != unsymmetrical_pairs[0][0]:
                    invers(unsymmetrical_pairs)
                # print(f'? {symmetrical_pairs[0][2] + 1}')
                x = question(symmetrical_pairs[0][2] + 1)
                sys.stdout.flush()
                # x = int(input())
                if x != symmetrical_pairs[0][2]:
                    invers(symmetrical_pairs)
                number_of_questions += 2


T = 100
str_len = 30
for _ in range(T):
    counter = 1
    print(f'ТЕСТ НОМЕР {_ + 1}')
    arr = ''.join([str(randint(0, 1)) for i in range(30)])
    print(f'arr = {arr}')
    main(str_len)