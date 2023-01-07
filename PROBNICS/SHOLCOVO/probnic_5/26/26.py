def main():
    with open('26__x9cd.txt') as file:
        disk_size, file_count = [int(i) for i in file.readline().split()]
        files = []
        for i in range(file_count):
            files.append(int(file.readline()))
    files.sort()
    max_count = 0
    max_size = 0
    cur_size = 0
    for file_size in files:
        if cur_size + file_size <= disk_size:
            max_count += 1
            max_size = file_size
            cur_size += file_size
    for i in range(max_count, file_count):
        if cur_size - max_size + files[i] <= disk_size:
            cur_size = cur_size - max_size + files[i]
            max_size = files[i]
    print(max_count, max_size)


main()
