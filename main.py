import copy
import datetime
from random import randint

from algo import *

n = 10**3
max_value = 10*10

mas = [randint(0, max_value) for _ in range(n)]

print('Сортировка Шелла:', test_sort(shell, mas))

print('Быстрая сортировка (рекурсивно):', test_sort(quicksort, mas))


print('Быстрая сортировка (итерации):', test_sort(quicksort_iter, mas))

print('Цифровая сортировка:', test_sort(digit_sort, mas))

print('Пирамидальная сортировка:', test_sort(heapsort, mas))

print('Сортировка подсчетом:', test_sort(count_sort, mas))

print('Сортировка подсчетом (списки):', test_sort(merge_list_sort, mas))
