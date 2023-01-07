
def load_data():
    with open('22.txt') as file:
        processes = []
        for line in file:
            process_id, time, zav = line.split()
            processes.append({'process_id': int(process_id), 'time': int(time), 'zav': set([int(i) for i in zav.split(';')])})
        return processes


def main():
    processes = load_data()
    print(processes)
    cur_processes = set()
    finished_processes = {0}
    ost_processes = processes.copy()
    cur_time = 0
    while len(ost_processes) != 0 or len(cur_processes) != 0:
        # print('ost_processes' , ost_processes)
        # print('finished_pr', finished_processes)
        cur_time += 1
        cur_processes_ = set()
        for process in cur_processes:
            if process[1] == 1:
                finished_processes.add(process[0])
            else:
                cur_processes_.add((process[0], process[1] - 1))
        cur_processes = cur_processes_.copy()

        ost_processes_ = []
        for process in ost_processes:
            if all(i in finished_processes for i in process['zav']):
                cur_processes.add((process['process_id'], process['time']))
            else:
                ost_processes_.append(process)
        ost_processes = ost_processes_.copy()
    print(cur_time - 1)


if __name__ == '__main__':
    main()