from const import a as test_data, INF
from prima import prima

answer = []
visited = []


def dfs(tree, node, end, depth=0):
    global stack, answer, visited
    visited[node] = True
    answer.append(node)
    for i, n in enumerate(tree[node]):
        if depth > 1 and n != INF and i == end:
            return True
        if n != INF and not visited[i]:
            if dfs(tree, i, end, depth+1):
                return True
    answer.remove(node)
    return False


def find_loop(data: list[list | tuple] | tuple[list | tuple], start: int):
    """
    Поиск первого попавшегося цикла
    :param data: Матрица смежности
    :param start: вершина, которая должна быть в цикле
    :return:
    """
    global answer, visited
    n = len(data)

    ostov = set(prima(data))
    extra = set(data) - ostov  # ребра, не входящие в остовное дерево
    for extra_edge in extra:  # по очереди добавляем одно ребро в дерево и ищем получившийся цикл
        now = ostov | {extra_edge}
        matrix = [[INF for _ in range(n)] for _ in range(n)]  # теперь строим матрицу, тут удобнее так
        for l, x, y in now:
            matrix[x][y] = l
            matrix[y][x] = l
        visited = [False for _ in range(n)]
        visited[start] = True
        answer = []
        dfs(matrix, extra_edge[1], extra_edge[1])  # начинаем с вершины дополнительного ребра
        print(answer)


find_loop(test_data, 0)
