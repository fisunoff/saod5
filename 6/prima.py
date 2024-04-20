INF = 10**18


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
    nodes = set()
    for l, x, y in graph:
        nodes.add(x)
        nodes.add(y)
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


a = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]

print(*prima(a))
