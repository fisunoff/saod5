import copy
from datetime import datetime


def heapsort(mas):
    build_max_heap(mas)
    for i in range(len(mas) - 1, 0, -1):
        mas[0], mas[i] = mas[i], mas[0]
        max_heapify(mas, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(mas, index, size):
    l = left(index)
    r = right(index)
    if l < size and mas[l] > mas[index]:
        largest = l
    else:
        largest = index
    if r < size and mas[r] > mas[largest]:
        largest = r
    if largest != index:
        mas[largest], mas[index] = mas[index], mas[largest]
        max_heapify(mas, largest, size)


def test_heap(mas):
    mas_t = copy.copy(mas)
    start = datetime.now()
    heapsort(mas_t)
    end = datetime.now()
    return end - start
