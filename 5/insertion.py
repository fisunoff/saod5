import copy
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Node:
    value: int
    next = None

    def __str__(self):
        return f'{self.value}, {self.next}' if self.next else str(self.value)

    def push_back(self, value):
        if not self.next:
            self.next = Node(value)
        else:
            self.next.push_back(value)


class InsertionSearcher:
    head = None

    def __init__(self, mas):
        for elem in mas:
            self.push_back(elem)

    def sort(self):
        res = Node(self.head.value)
        self.head = self.head.next
        tmp_res = None
        start = self.head
        while start:
            if start.value < res.value:
                tmp_res = Node(start.value)
                tmp_res.next = res
                res = tmp_res
                start = start.next
                continue
            tmp_res = res
            while tmp_res.next and start.value > tmp_res.next.value:
                tmp_res = tmp_res.next
            tmp2 = tmp_res.next
            tmp_res.next = Node(start.value)
            tmp_res.next.next = tmp2
            start = start.next
        self.head = res

    def push_back(self, value):
        if self.head:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(value)
        else:
            self.head = Node(value)

    def __str__(self):
        return str(self.head)


def test_insertion(mas):
    mas_t = copy.copy(mas)
    t = InsertionSearcher(mas_t)
    start = datetime.now()
    t.sort()
    end = datetime.now()
    return end - start
