def load_data():
    def from_str_to_float(n_str):
        N, R = n_str.split(',')
        return int(N) + int(R) / 10 ** len(R)
    data = []
    with open('9.txt') as file:
        for line in file.readlines():
            data.extend([from_str_to_float(i) for i in line.split()])
    return data


def main():
    data = load_data()
    print(min(data) - sum(data) / len(data))


main()
