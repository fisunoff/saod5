"""
b) матрица инциденций
c) список ребер
переводить туда и обратно
Будем делать для ориентированных графов
"""

from const import INF, test_matrix, test_list


def matrix_to_list(m):
    lst = []
    for i, row in enumerate(m):
        for j, elem in enumerate(row):
            if elem != INF:
                lst.append([i, j])
    return lst


def list_to_matrix(lst):
    n = max((max(x, y) for x, y, l in lst)) + 1
    matrix = [[INF for _ in range(n)] for _ in range(n)]
    for x, y, l in lst:
        matrix[x][y] = l
    return matrix


print(*matrix_to_list(test_matrix))
print(list_to_matrix(test_list))
