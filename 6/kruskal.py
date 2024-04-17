import copy

a = [
    [1, 2, 7],
    [1, 3, 8],
    [2, 3, 11],
    [2, 4, 2],
    [3, 4, 6],
    [3, 5, 9],
    [4, 5, 11],
    [4, 6, 9],
    [5, 6, 10],
]


def kruskal(m: list):
    mas = copy.deepcopy(m)
    mas.sort(key=lambda i: i[2])
    need_nodes = set()
    for x, y, l in mas:
        need_nodes.add(x)
        need_nodes.add(y)
    res = []
    min_len = 0
    for x, y, l in mas:
        if x in need_nodes or y in need_nodes:
            min_len += l
            need_nodes.discard(x)
            need_nodes.discard(y)
            res.append([x, y])
        if not need_nodes:
            break
    return res


print('Список ребер:', *a)
print('Минимальное остовное дерево:', *kruskal(a))
