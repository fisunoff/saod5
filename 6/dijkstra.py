from const import INF, orgraph

start = 0
s = set()
all_nodes = orgraph.keys()
n = len(all_nodes)
d = [(INF, []) for _ in range(n)]
d[start] = (0, [])
now = start

for _ in range(n):
    min_val = min_index = INF
    for i in range(n):
        if d[i][0] < min_val and i not in s:
            min_val = d[i][0]
            min_index = i
    s.add(min_index)
    for edge, length in orgraph[min_index]:
        if min_val + length < d[edge][0]:
            d[edge] = [min_val + length, d[min_index][1] + [min_index]]
for i, row in enumerate(d):
    print(i, row)
