def get_nodes_from_nodes_list(lst) -> set:
    """
    Все вершины по списку смежности (вес, x, y)
    :param lst: Список смежности
    :return: множество вершин
    """
    nodes = set()
    for l, x, y in lst:
        nodes.add(x)
        nodes.add(y)
    return nodes
