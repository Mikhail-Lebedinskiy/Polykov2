from tqdm import tqdm


def load_data(file_path: str) -> tuple[int, int, list]:
    response = []
    with open(file_path) as file:
        count_of_containers, x = [int(i) for i in file.readline().split()]
        for line in file:
            response.append(int(line.strip()))
    return count_of_containers, x, response


def main() -> int:
    count_of_containers, x, container_sizes = load_data('B.txt')
    min_len = 10**10
    for i in tqdm(range(count_of_containers)):
        current_size = container_sizes[i]
        current_len = 1
        j = i + 1
        while current_size <= x:
            if current_size == x:
                min_len = min(min_len, current_len)
                break
            current_size += container_sizes[j % count_of_containers]
            current_len += 1
            j += 1
    return min_len


if __name__ == '__main__':
    print(main())



