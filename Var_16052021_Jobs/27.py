def load_data(file_path: str) -> list:
    data = []
    with open(file_path) as file:
        file.readline()
        for line in file:
            data.append(int(i) for i in line.strip().split())
    return data


def main():
    data = load_data('data/Задание 27/27-A.txt')
    arr = {}
    for num1, num2 in data:
        delta_5 = -abs(num1 - num2) % 5
        delta_3 = abs(num1 - num2) % 3
        try:
            data[(delta_3, delta_5)] = min(data[(delta_3, delta_5)], abs(num1 - num2))
        except KeyError:
            data[(delta_3, delta_5)] = abs(num1 - num2)

