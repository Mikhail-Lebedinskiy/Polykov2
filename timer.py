from time import time


def convert_time(all_time: int) -> str:
    """Получает время в секундах возращае в формате hh:mm:ss"""
    all_time_hours = str(all_time // 3600)
    all_time_hours = '0' * (2 - len(all_time_hours)) + all_time_hours  # 2 преобразует в 02
    all_time_min = str((all_time % 3600) // 60)
    all_time_min = '0' * (2 - len(all_time_min)) + all_time_min
    all_time_second = str(all_time % 60)
    all_time_second = '0' * (2 - len(all_time_second)) + all_time_second
    all_time_str = f'{all_time_hours}:{all_time_min}:{all_time_second}'
    return all_time_str


tasks = {i: 0 for i in range(28)}
tasks.pop(20)
tasks.pop(21)
time_marks = {i: None for i in range(28)}
time_marks.pop(20)
time_marks.pop(21)


current_task = 0
while True:
    try:
        print("Введите номер задачи которую сейчас решаете или 'stop' чтобы завершить тест.")
        command = input()
        if time_marks[current_task] is not None:
            tasks[current_task] += (time() - time_marks[current_task])
        else:
            tasks[current_task] += time()

        if command == 'stop':
            for task, time in tasks.items():
                print(f'Номер {task} время - {int(convert_time(time))}.')
            break
        else:
            command = int(command)
            current_task = command
            time_marks[current_task] = time()
    except Exception as err:
        print(err)
