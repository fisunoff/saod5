from const import a, INF
from utils import get_nodes_from_nodes_list


def get_min(R, U):
    rm = (INF, -1, -1)
    rr = min(
        R, key=lambda x: x[0] if (x[1] in U and x[2] not in U) or (x[2] in U and x[1] not in U) else INF
    )
    if rm[0] > rr[0]:
        rm = rr
    if rm[1] in U and rm[2] in U:
        raise NotImplementedError('Граф не является связным')
    return rm


def prima(graph):
    """

    :param graph: список ребер
    :return: список ребер
    """
    nodes = get_nodes_from_nodes_list(graph)
    n = len(nodes)
    u = {0}
    t = []

    while len(u) < n:
        r = get_min(graph, u)
        if r[0] == INF:
            raise NotImplementedError('Граф не является связным')

        t.append(r)
        u.add(r[1])
        u.add(r[2])
    return t


if __name__ == '__main__':
    print(*prima(a))
