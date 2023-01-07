from random import randint

from dataclasses import dataclass


@dataclass
class Node:
    pref: int = 0
    suf: int = 0
    max: int = 0
    flag: bool = False  # (pref == suf == segment_len)

    def __str__(self):
        return f'({self.pref}, {self.max}, {self.suf}, {self.flag})'


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


def make_data(val):
    if val == 0:
        return Node(1, 1, 1, True)
    else:
        return Node(0, 0, 0, False)


c1, c2 = make_data(0), make_data(1)
v1 = merge(c2, c2)
v2 = merge(c1, c1)
v3 = merge(c1, c2)
print(v1)
print(v2)
print(v3)