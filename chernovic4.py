from dataclasses import dataclass


def write_answer(output_file_name, answers):
    with open(output_file_name, 'w') as file:
        for answer in answers:
            file.write(f'{answer}\n')


def load_data(file_name="input.txt"):
    with open(file_name, 'r') as file:
        n = int(file.readline())
        rating = [int(i) for i in file.readline().split()]
        m = int(file.readline())
        queries = []
        for i in range(m):
            query_type, v1, v2 = file.readline().split()
            v1, v2 = int(v1), int(v2)
            queries.append((query_type, v1, v2))
    return n, m, rating, queries


@dataclass
class Node:
    pref: int = 0
    suf: int = 0
    max: int = 0
    flag: bool = False  # (pref == suf == segment_len)

    def __str__(self):
        return f'({self.pref}, {self.max}, {self.suf}, {self.flag})'


N = 5 * 10 ** 5
# N = 10
a = [1] * N
t = [Node()] * (4 * N)


def make_data(val):
    if val == 0:
        return Node(1, 1, 1, True)
    else:
        return Node(0, 0, 0, False)


def merge(response_l, response_r):
    response = Node()
    if (not response_l.flag) and (not response_r.flag):
        response.pref = response_l.pref
        response.suf = response_r.suf
        response.max = max(response_l.suf + response_r.pref, response_l.max)
        response.max = max(response.max, response_r.max)
        response.flag = False
    elif response_l.flag and response_r.flag:
        response.pref = response_l.pref + response_r.pref
        response.suf = response_l.suf + response_r.suf
        response.max = response_l.max + response_r.max
        response.flag = True
    elif response_l.flag:
        response.pref = response_l.pref + response_r.pref
        response.suf = response_r.suf
        response.flag = False
        response.max = max(response_l.pref + response_r.pref, response_r.max)
    elif response_r.flag:
        response.pref = response_l.pref
        response.suf = response_l.suf + response_r.suf
        response.max = max(response_l.suf + response_r.suf, response_l.max)
        response.flag = False
    return response


def build(v, l, r):
    if r - l == 1:
        t[v] = make_data(a[l])
    else:
        m = (r + l) // 2
        left = 2 * v + 1
        right = 2 * v + 2
        build(left, l, m)
        build(right, m, r)
        t[v] = merge(t[left], t[right])


def update(v, l, r, pos, x):
    if r - l == 1:
        t[v] = make_data(x)
    else:
        m = (r + l) // 2
        left = 2 * v + 1
        right = 2 * v + 2
        if pos < m:
            update(left, l, m, pos, x)
        else:
            update(right, m, r, pos, x)
        t[v] = merge(t[left], t[right])


def query(v, l, r, ql, qr):
    if ql >= r or qr <= l:
        return make_data(1)
    elif ql <= l and qr >= r:
        return t[v]
    else:
        m = (r + l) // 2
        left = 2 * v + 1
        right = 2 * v + 2
        return merge(query(left, l, m, ql, qr), query(right, m, r, ql, qr))


def main_fast(output_file_name='output_fast.txt'):
    n, m, rating, queries = load_data()
    for i in range(N):
        a[i] = 1
    for i in range(n):
        a[i] = rating[i]
    build(0, 0, N)
    # answers = []
    for cur_query in queries:
        query_type = cur_query[0]
        if query_type == "QUERY":
            l, r = cur_query[1] - 1, cur_query[2]
            response = query(0, 0, N, l, r)
            # answers.append((cur_query, response.max))
            print(response.max)
        else:
            i, x = cur_query[1] - 1, cur_query[2]
            update(0, 0, N, i, x)
    # write_answer(output_file_name, answers)


main_fast()
