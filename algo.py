import copy
import datetime

from insertion import InsertionSearcher
from shellsort import shell
from quicksort import quicksort, qsort as quicksort_iter
from digit import digit_sort
from heapsort import heapsort
from countsort import count_sort
from merge import mergesort
from list_merge import test_list_merge_sort


def test_sort(algo, mas):
    mas_copy = copy.copy(mas)
    start = datetime.datetime.now()
    algo(mas_copy)
    end = datetime.datetime.now()
    return end - start
