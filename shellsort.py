import copy
from datetime import datetime


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


def test_shell(mas):
    mas_t = copy.copy(mas)
    start = datetime.now()
    shell(mas_t)
    end = datetime.now()
    return end - start
