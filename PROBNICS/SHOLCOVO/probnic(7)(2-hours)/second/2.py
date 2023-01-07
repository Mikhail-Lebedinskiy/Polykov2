from itertools import product, permutations


def arr_mask(arr, mask):
    """Возвращает элементы массива, в соответсвие с порядком который указан в маске"""
    #  [0, 0, 1, 0], [1, 2, 3, 0] -> [0, 0, 0, 1]
    answer = [0] * len(arr)
    for i, ind in enumerate(mask):
        answer[ind] = arr[i]
    return answer


def get_all_matching_rows(rows_mask):
    """  '1?' -> ['10', '11']  """

    def replace_question(s, substitution):
        """  ('1??1', [10]) -> [1, 1, 0, 1]  """
        answer = []
        question_count = 0
        for chr in s:
            if chr == '?':
                answer.append(substitution[question_count])
                question_count += 1
            else:
                answer.append(int(chr))
        return answer

    answer = []
    for substitution in product([0, 1], repeat=rows_mask.count('?')):
        answer.append(replace_question(rows_mask, substitution))
    return answer


def logical_expression(x, y, z, w):
    """Введите сюда ваше логическое выражение (не забудьте преобразовать его к типу int!)"""
    v1 = z <= y
    nx = not x
    v2 = nx <= w
    v3 = z == w
    v4 = y and nx
    z1 = v1 and v2
    z2 = v3 or v4
    itog = z1 <= z2
    return int(itog)


def get_true_false_table(number_of_args):
    true_false_table = []
    for args in product([0, 1], repeat=number_of_args):
        true_false_table.append([*args, logical_expression(*args)])
    return true_false_table


def is_good_permutation(args_permutation, all_true_false_table, partial_true_false_table):
    """проверяет подходит ли данный порядок аргументов"""

    def is_can_make_table(table):
        """Можно ли составить из строк table таблицу без повторяющихся строк"""
        ranges = []
        for line in table:
            ranges.append(range(len(line)))
        variants = product(*ranges)
        for variant in variants:
            arr = [tuple(table[i][variant[i]]) for i in range(len(variant))]
            if len(arr) == len(set(arr)):
                return True
        return False

    flag = True
    table = [[] for i in range(len(partial_true_false_table))]  # здесь будут храниться подходящие строки
    for i, line in enumerate(partial_true_false_table):
        for line_variant in get_all_matching_rows(line):
            if arr_mask(line_variant, args_permutation + [len(line) - 1]) in all_true_false_table:
                flag = False
                table[i].append(line_variant)
    if flag:
        return False
    if is_can_make_table(table):
        return True
    return False


def main():
    """Введите параметры вашей задачи"""
    number_of_args = 4  # количество переменных в вашем логическом выражении
    args_names = 'xyzw'
    partial_true_false_table = ['00?00', '0???0', '1?110']  # знак вопрос означает пропущенное значение(формат xyzwf(x, y, z, w))

    all_true_false_table = get_true_false_table(number_of_args)
    for args_permutation in permutations(range(number_of_args)):
        if is_good_permutation(list(args_permutation), all_true_false_table, partial_true_false_table):
            print(' '.join([args_names[i] for i in args_permutation]))


main()
print(*get_true_false_table(4), sep='\n')