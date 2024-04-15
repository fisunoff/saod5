def count_sort(mas: list) -> list:
    """
    Сортировка подсчетом
    """
    maxx = max(mas)
    tmp = [0 for i in range(maxx + 1)]
    res = []
    for i in mas:
        tmp[i] += 1
    for n, cnt in enumerate(tmp):
        if cnt:
            res.extend([n for _ in range(cnt)])
    return res
