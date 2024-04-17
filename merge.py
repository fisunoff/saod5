import copy
from datetime import datetime


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def test_merge(mas):
    mas_t = copy.copy(mas)
    start = datetime.now()
    mergesort(mas_t)
    end = datetime.now()
    return end - start


class Node:
    value = None
    next_elem = None

    def __init__(self, value):
        self.value = value

    @property
    def data(self):
        return self.value


def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next_elem and fast.next_elem.next_elem:
        slow = slow.next_elem
        fast = fast.next_elem.next_elem

    return slow


class List:
    start = None

    def __init__(self, values):
        self.start = Node(values[0])
        now = self.start
        for value in values[1:]:
            new_elem = Node(value)
            now.next_elem = new_elem
            now = new_elem

    def __getitem__(self, key):
        i = 0
        tmp = self.start
        while i < key:
            tmp = tmp.next_elem
            i += 1
        return tmp

    def __str__(self):
        return ' '.join(str(i) for i in self)

    def __len__(self):
        tmp = self.start
        i = 1
        while tmp.next_elem:
            i += 1
            tmp = tmp.next_elem
        return i

    def __iter__(self):
        tmp = self.start
        while tmp:
            yield tmp.value
            tmp = tmp.next_elem

    def sort(self):
        self.start = self.merge_sort(self.start)

    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next_elem = self.sorted_merge(left.next_elem, right)
        else:
            result = right
            result.next_elem = self.sorted_merge(left, right.next_elem)
        return result

    def merge_sort(self, h):
        if h is None or h.next_elem is None:
            return h

        middle = get_middle(h)
        next_to_middle = middle.next_elem
        middle.next_elem = None

        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)

        sortedlist = self.sorted_merge(left, right)
        return sortedlist


def merge_list_sort(mas: list):
    a = List(mas)
    a.sort()
