import random
from random import choice
from collections import deque


def quicksort(mas):
    """
    Рекурсивный quicksort
    """
    if len(mas) <= 1:
        return mas
    else:
        q = choice(mas)
        left = []
        mid = []
        right = []
        for elem in mas:
            if elem < q:
                left.append(elem)
            elif elem > q:
                right.append(elem)
            else:
                mid.append(elem)
        return quicksort(left) + mid + quicksort(right)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def partition(a, start, end):
    pivot = a[end]
    p_index = start

    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, p_index)
            p_index = p_index + 1
    swap(a, p_index, end)

    return p_index


def quicksort_iter(mas):
    stack = deque()
    start = 0
    end = len(mas) - 1
    stack.append((start, end))

    while stack:
        start, end = stack.pop()
        pivot = partition(mas, start, end)
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))

    return mas

MAXSTACK = 2048

def qsort(mas):
    size = len(mas)
    lbstack = [0 for _ in range(MAXSTACK)]
    ubstack = [0 for _ in range(MAXSTACK)]
    stackpos = 1

    lbstack[1] = 0
    ubstack[1] = size - 1
    while stackpos != 0:
        lb = lbstack[stackpos]
        ub = ubstack[stackpos]
        stackpos -= 1
        while lb < ub:
            ppos = (lb + ub) // 2
            i = lb
            j = ub
            pivot = mas[ppos]
            while i <= j:
                while mas[i] < pivot:
                    i += 1
                while pivot < mas[j]:
                    j -= 1
                if i <= j:
                    temp = mas[i]
                    mas[i] = mas[j]
                    mas[j] = temp
                    i += 1
                    j -=1
            if i < ppos:
                if i < ub:
                    stackpos += 1
                    lbstack[stackpos] = i
                    ubstack[stackpos] = ub
                ub = j
            else:
                if j > lb:
                    stackpos += 1
                    lbstack[stackpos] = lb
                    ubstack[stackpos] = j
                lb = i
    return mas


qsort([random.randint(1, 10**7) for _ in range(10**6)])
