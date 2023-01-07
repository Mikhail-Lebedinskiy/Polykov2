def load_data(file_path):
    data = {}
    with open(file_path) as file:
        for line in file:
            process_id, time, relations = line.split()
            process_id = int(process_id)
            time = int(time)
            relations = [int(i) for i in relations.split(';')]
            relations = [i for i in relations if i != 0]
            data[process_id] = {'time': time, 'relations': relations}
    return data


def solve(data):
    count_off_processes = len(data.keys())
    finished_processes = set()
    current_processes = []
    time = 0
    while len(finished_processes) != count_off_processes:
        # print(finished_processes)
        current_processes_new = []
        for process_id, time in current_processes:
            if (time - 1) != 0:
                current_processes_new.append([process_id, time - 1])
            else:
                finished_processes.add(process_id)
        current_processes = current_processes_new.copy()
        for process_id in data:
            for relation_process_id in data[process_id]['relations']:
                if relation_process_id not in finished_processes:
                    break
            else:
                current_processes.append([process_id, data[process_id]['time']])
    return time


def main():
    data = load_data('data.txt')
    print(solve(data))


if __name__ == '__main__':
    main()
