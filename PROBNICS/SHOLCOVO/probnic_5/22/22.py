def load_data():
    with open('22.txt') as file:
        data = {}
        for i in file.readlines():
            id, time, relations = i.split()
            time = int(time)
            id = int(id)
            relations = [int(i) for i in relations.split(';')]
            data[id] = {'relations': relations, 'time': time}
        return data


def main():
    data = load_data()
    print(data)
    time = [[] for i in range(500)]
    completes_processes = set()
    completes_processes.add(0)
    for cur_time in range(0, 5000):
        for complete_process in time[cur_time]:
            completes_processes.add(complete_process)
        if len(data) == 0:
            t = cur_time
            for p in range(cur_time, len(time)):
                if len(time[p]) != 0:
                    t = p
            print(t)
            break
        keys_to_delete = []
        for process in data.keys():
            for relation in data[process]['relations']:
                if relation not in completes_processes:
                    break
            else:
                print(cur_time, process)
                time[cur_time + data[process]['time']].append(process)
                keys_to_delete.append(process)
        for key in keys_to_delete:
            del(data[key])



main()