from random import randint

from countsort import test_count
from digit import test_digit
from heapsort import test_heap
from insertion import test_insertion
from list_merge import test_list_merge_sort
from merge import test_merge
from quicksort import test_quicksort, test_quicksort_iter
from shellsort import test_shell

n = 10**7
max_value = 10*10

mas = [randint(0, max_value) for _ in range(n)]

# print('Сортировка вставками в связанный список:\t', test_insertion(mas))

print('Сортировка Шелла:\t', test_shell(mas))

print('Быстрая сортировка (рекурсивно):\t', test_quicksort(mas))

print('Быстрая сортировка (итерации):', test_quicksort_iter(mas))

print('Цифровая сортировка:', test_digit(mas))

print('Пирамидальная сортировка:', test_heap(mas))

print('Сортировка подсчетом:', test_count(mas))
print('Сортировка слиянием:', test_merge(mas))
# print('Сортировка слиянием (списки):', test_list_merge_sort(mas))
