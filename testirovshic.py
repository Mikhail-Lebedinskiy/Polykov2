from termcolor import cprint


def calculate_score(right_answers):
    scores_for_tasks = [1] * 28
    scores_for_tasks[0] = 0
    scores_for_tasks[25] = 2
    scores_for_tasks[26] = 2
    scores_for_tasks[27] = 2
    score = 0
    for number in right_answers:
        score += scores_for_tasks[int(number)]
    return score


def convert_primary_scores_to_secondary(primary_score):
    scale = {
        0: 0,
        1: 8,
        2: 15,
        3: 22,
        4: 29,
        5: 37,
        6: 43,
        7: 46,
        8: 48,
        9: 50,
        10: 53,
        11: 55,
        12: 57,
        13: 60,
        14: 62,
        15: 65,
        16: 67,
        17: 69,
        18: 71,
        19: 74,
        20: 76,
        21: 78,
        22: 81,
        23: 84,
        24: 85,
        25: 88,
        26: 90,
        27: 93,
        28: 95,
        29: 98,
        30: 100
    }
    return scale[primary_score]


true_answers_file = open('Var_05102020_Jobs/real_answers.txt', 'r', encoding='utf-8')

true_answers = {}

for line in true_answers_file:
    task_number, answer = line.split()
    task_number = task_number[:-1]
    true_answers[task_number] = answer

true_answers_file.close()


user_answers_file = open('Var_05102020_Jobs/my_answers.txt', 'r', encoding='utf-8')

user_answers = {}

for line in user_answers_file:
    task_number, answer = line.split()
    task_number = task_number[:-1]
    user_answers[task_number] = answer
print(user_answers)

user_answers_file.close()


right_answers = []
wrong_answers = []
for key in true_answers.keys():
    if true_answers[key] == user_answers[key]:
        right_answers.append(key)
    else:
        wrong_answers.append(key)

len_test = len(user_answers.keys())
percent_right_answers = round(len(right_answers) / len_test * 100, 0)
primary_score = calculate_score(right_answers)
secondary_score = convert_primary_scores_to_secondary(primary_score)
cprint(f'ИТОГ: {percent_right_answers}%', color='blue')
cprint(f'Вы на брали {primary_score} баллов из {30} первичных баллов.', color='blue')
cprint(f'Вы на брали {secondary_score} баллов из {100} вторичных баллов.', color='blue')
cprint("ВАШИ ОШИБКИ:", color='red')
for key in wrong_answers:
    cprint(f'\t{key})', end=' ', color='red')
    cprint(f'Ваш ответ - {user_answers[key]}.', end=' ', color='red')
    cprint(f'Правильный ответ - {true_answers[key]}.', color='green')

