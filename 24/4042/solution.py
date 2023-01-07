def load_data(file_path: str) -> list:
    strings = []
    with open(file_path) as file:
        for string in file:
            strings.append(string.strip())
    return strings


def main() -> int:
    strings = load_data('data.txt')
    max_len = 0
    for string in strings:
        data = {i: None for i in 'qwertyiuopasdfghjklzxcvbnm'.upper()}
        if string.count('E') < 20:
            for i in range(len(string)):
                if data[string[i]] is None: data[string[i]] = i
                else: max_len = max(max_len, i - data[string[i]])
    return max_len


if __name__ == '__main__':
    print(main())