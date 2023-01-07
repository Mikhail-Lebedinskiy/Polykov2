# минут 30
def load_data():
    with open('curs.txt') as file:
        curses = {}
        for line in file:
            _, id_val, date, curs = line.split()
            i, f = curs.split(',')
            curs = float(f'{i}.{f}')
            if id_val not in curses.keys():
                curses[id_val] = {date: curs}
            else:
                curses[id_val][date] = curs
    with open('postupleniy.txt') as file:
        postupleniy = []
        for line in file:
            _, id_chet, id_val, date, value = line.split()
            try:
                i, f = value.split(',')
            except ValueError:
                i = value
                f = '0'
            value = float(f'{i}.{f}')
            postupleniy.append({"id_chet": id_chet, "date": date, "id_val": id_val, "value": value})

    return curses, postupleniy


def main():
    cheta = {str(i): 0 for i in range(1, 1001)}
    curses, postupleniy = load_data()
    for p in postupleniy:
        id_chet = p['id_chet']
        date = p['date']
        id_val = p['id_val']
        value = p['value']
        cheta[id_chet] += value * curses[id_val][date]
    max_sum, min_sum = -1, 10 ** 5
    for chet in cheta:
        max_sum = max(max_sum, cheta[chet])
        min_sum = min(min_sum, cheta[chet])
    print(min_sum, max_sum)
    print(max_sum - min_sum)


main()