import copy
import random
import datetime


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class ListMergeSort:
    def __init__(self):
        self.root = Node(random.randint(0, 10))
        self.size = 0

    def set_list(self, mas):
        self.size = len(mas)
        self.root.val = mas[0]
        temp = self.root
        for i in range(1, self.size):
            node = Node(mas[i])
            temp.next = node
            temp = temp.next

    def merge(self, l, r):
        left = self.root
        for i in range(l):
            left = left.next
        if r <= l:
            return left

        mid = (r+l)//2
        leftRoot = self.merge(l, mid)
        rightRoot = self.merge(mid+1, r)
        i = l
        j = mid+1

        if leftRoot.val < rightRoot.val:
            result = Node(leftRoot.val)
            i += 1
            leftRoot = leftRoot.next
        else:
            result = Node(rightRoot.val)
            j += 1
            rightRoot = rightRoot.next
        resultRoot = result
        while i <= mid and j <= r:
            if leftRoot.val < rightRoot.val:
                result.next = Node(leftRoot.val)
                i += 1
                result = result.next
                leftRoot = leftRoot.next
            else:
                result.next = Node(rightRoot.val)
                j += 1
                result = result.next
                rightRoot = rightRoot.next
        while i <= mid:
            result.next = Node(leftRoot.val)
            i += 1
            result = result.next
            leftRoot = leftRoot.next
        while j <= r:
            result.next = Node(rightRoot.val)
            j += 1
            result = result.next
            rightRoot = rightRoot.next
        return resultRoot

    def sort(self):
        self.root = self.merge(0, self.size-1)

    def show(self):
        temp = self.root
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next
        print()


def test_list_merge_sort(mas):
    mas_t = copy.copy(mas)
    lst = ListMergeSort()
    lst.set_list(mas_t)
    start = datetime.datetime.now()
    lst.sort()
    end = datetime.datetime.now()
    return end - start
