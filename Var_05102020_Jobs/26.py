def load_data(file_path: str) -> list:
    data = []
    with open(file_path) as file:
        for line in file:
            data.append(int(line.strip()))
    return sorted(data)


def main() -> None:
    data = load_data('data/Задание 26/26.txt')
    size_of_compressed_files = 0.8 * sum(data)
    max_size = 0.9 * sum(data)
    size_of_not_compressed_files = 0
    index_of_last_file = 0
    size_of_last_file = 0

    for i, size in enumerate(data):
        if size_of_not_compressed_files + 0.2 * size + size_of_compressed_files <= max_size:
            size_of_not_compressed_files -= 0.8 * size
            size_of_not_compressed_files += size
        else:
            index_of_last_file = i - 1
            size_of_last_file = data[i - 1]
            print(f'Количество не сжатых файлов: {i}')
            break

    for size in data[index_of_last_file + 1:]:
        if size_of_not_compressed_files - 0.2 * size_of_last_file + size_of_compressed_files + 0.2 * size <= max_size:
            size_of_not_compressed_files = size_of_not_compressed_files - size_of_last_file + size
            size_of_compressed_files = size_of_compressed_files - 0.8 * size + 0.8 * size_of_last_file
            size_of_last_file = size
        else:
            print(f'Максимальный размер файла: {size_of_last_file}')
            break


main()