INF = 10**18
test_matrix = [
    [INF, 1, 2, 3],
    [INF, INF, 5, 6],
    [20, 30, INF, 8],
    [INF, INF, INF, INF],
]

test_tree = [
    [INF, 1, INF, INF, INF, INF, INF, INF, 1],
    [1, INF, 1, 1, INF, INF, INF, INF, INF],
    [INF, 1, INF, INF, INF, INF, INF, INF, INF],
    [INF, 1, INF, INF, 1, INF, INF, INF, 1],
    [INF, INF, INF, 1, INF, 1, 1, INF, INF],
    [INF, INF, INF, INF, 1, INF, INF, INF, INF],
    [INF, INF, INF, INF, 1, INF, INF, 1, INF],
    [INF, INF, INF, INF, INF, INF, 1, INF, INF],
    [1, INF, INF, 1, INF, INF, INF, INF, INF],
]

test_list = [
    [0, 2, 8],
    [0, 5, 7],
    [5, 3, 1],
    [3, 8, 55],
]

a = [(13, 0, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]


orgraph = {  # (номер, вес)
    0: ((1, 5), (2, 3), (3, 1)),
    1: ((5, 30), ),
    2: ((4, 4), ),
    3: ((2, 1), (4, 10)),
    4: ((5, 1), ),
    5: (),
}