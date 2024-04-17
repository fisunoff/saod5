"""
b) матрица инциденций
c) список ребер
переводить туда и обратно
Будем делать для ориентированных графов
"""

INF = 10**9

test_matrix = [
    [INF, 1, 2, 3],
    [INF, INF, 5, 6],
    [20, 30, INF, 8],
    [INF, INF, INF, INF],
]

test_list = [
    [0, 2, 8],
    [0, 5, 7],
    [5, 3, 1],
    [3, 8, 55],
]


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
